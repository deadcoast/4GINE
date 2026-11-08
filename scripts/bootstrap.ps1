param([switch]$ToolsOnly)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$repo = Split-Path -Parent $PSScriptRoot
$previousLocation = Get-Location
$savedEnvironment = @{}
$environmentKeys = @('PATH','TEMP','TMP','UV_CACHE_DIR','UV_PYTHON_INSTALL_DIR','UV_PYTHON_BIN_DIR',
    'UV_PROJECT_ENVIRONMENT','UV_NO_CONFIG','npm_config_cache','npm_config_userconfig',
    'npm_config_globalconfig','PYTHONNOUSERSITE','PYTHONDONTWRITEBYTECODE')
$inheritedKeys = @([Environment]::GetEnvironmentVariables('Process').Keys | Where-Object {
    $_ -match '^(UV_|PYTHON|NPM_CONFIG_)' -or $_ -in @('VIRTUAL_ENV','NODE_OPTIONS','NODE_PATH')
})
foreach ($key in ($environmentKeys + $inheritedKeys | Select-Object -Unique)) {
    $savedEnvironment[$key] = [Environment]::GetEnvironmentVariable($key, 'Process')
}
function Run-Native([string]$Program, [string[]]$Arguments) {
    & $Program @Arguments
    if ($LASTEXITCODE -ne 0) { throw "$Program failed (exit $LASTEXITCODE)" }
}
function Archive-Hash([string]$Path) {
    $stream = [IO.File]::OpenRead($Path)
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($hasher.ComputeHash($stream))).Replace('-','').ToLowerInvariant() }
    finally { $stream.Dispose(); $hasher.Dispose() }
}
function Install-Archive($Record, [string]$Destination, [string]$Executable) {
    if (Test-Path -LiteralPath $Executable) { return }
    $archive = Join-Path $repo ('.tools/downloads/' + [IO.Path]::GetFileName($Record.url))
    if (!(Test-Path -LiteralPath $archive)) {
        Write-Output "Downloading $($Record.url)"
        Invoke-WebRequest -UseBasicParsing -Uri $Record.url -OutFile $archive -TimeoutSec 120
    }
    if ((Archive-Hash $archive) -ne $Record.sha256) {
        throw "Archive integrity check failed: $archive. Remove this cached archive and retry."
    }
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $destinationRoot = [IO.Path]::GetFullPath($Destination).TrimEnd('\') + '\'
    $zip = [IO.Compression.ZipFile]::OpenRead($archive)
    try {
        foreach ($entry in $zip.Entries) {
            $target = [IO.Path]::GetFullPath((Join-Path $Destination $entry.FullName))
            if (!$target.StartsWith($destinationRoot,[StringComparison]::OrdinalIgnoreCase)) {
                throw 'Archive entry escapes its installation directory.'
            }
            if ($entry.Name) {
                [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($target)) | Out-Null
                [IO.Compression.ZipFileExtensions]::ExtractToFile($entry,$target,$true)
            }
        }
    } finally { $zip.Dispose() }
    if (!(Test-Path -LiteralPath $Executable)) { throw "Archive did not provide $Executable" }
}
try {
    Set-Location -LiteralPath $repo
    foreach ($key in $inheritedKeys) {
        [Environment]::SetEnvironmentVariable($key, $null, 'Process')
    }
    if ([Environment]::OSVersion.Platform -ne 'Win32NT' -or
        $env:PROCESSOR_ARCHITECTURE -ne 'AMD64') {
        throw 'This bootstrap qualifies Windows x64 only; use 64-bit PowerShell.'
    }
    $pythonVersion = (Get-Content -LiteralPath '.python-version' -Raw).Trim()
    $nodeVersion = (Get-Content -LiteralPath '.node-version' -Raw).Trim()
    $project = Get-Content -LiteralPath 'pyproject.toml' -Raw
    $uvMatch = [regex]::Match($project, '(?m)^required-version\s*=\s*"==([0-9.]+)"')
    if (!$uvMatch.Success) { throw 'An exact tool.uv.required-version is required.' }
    $uvVersion = $uvMatch.Groups[1].Value
    $package = Get-Content -LiteralPath 'package.json' -Raw | ConvertFrom-Json
    $artifacts = Get-Content -LiteralPath 'scripts/toolchain-artifacts.json' -Raw | ConvertFrom-Json
    if ($package.engines.node -ne $nodeVersion -or
        $package.packageManager -ne ('npm@' + $package.engines.npm)) {
        throw 'Node/npm pins disagree between version file and package.json.'
    }
    if ($artifacts.uv.url -ne "https://releases.astral.sh/github/uv/releases/download/$uvVersion/uv-x86_64-pc-windows-msvc.zip" -or
        $artifacts.node.url -ne "https://nodejs.org/dist/v$nodeVersion/node-v$nodeVersion-win-x64.zip") {
        throw 'Artifact versions do not match declared pins; review URLs and hashes together.'
    }
    if (!$ToolsOnly) {
        foreach ($lock in @('uv.lock','package-lock.json')) {
            if (!(Test-Path -LiteralPath $lock)) { throw "Missing $lock; bootstrap will not resolve a new lockfile." }
        }
    }
    New-Item -ItemType Directory -Force -Path '.tools/downloads','.tools/cache','.tools/tmp' | Out-Null
    $env:TEMP = Join-Path $repo '.tools/tmp'
    $env:TMP = $env:TEMP
    $env:PYTHONNOUSERSITE = '1'
    $env:PYTHONDONTWRITEBYTECODE = '1'
    # Project-only fields such as package stay in pyproject.toml. This explicit
    # config prevents user/system uv settings from changing the reference run.
    [IO.File]::WriteAllText((Join-Path $repo '.tools/uv.toml'),"required-version = `"==$uvVersion`"`n")
    $uvDirectory = Join-Path $repo ".tools/uv-$uvVersion"
    $uv = Join-Path $uvDirectory 'uv.exe'
    $nodeDirectory = Join-Path $repo ".tools/node-v$nodeVersion-win-x64"
    $node = Join-Path $nodeDirectory 'node.exe'
    Install-Archive $artifacts.uv $uvDirectory $uv
    Install-Archive $artifacts.node (Join-Path $repo '.tools') $node
    $npm = Join-Path $nodeDirectory 'node_modules/npm/bin/npm-cli.js'
    if ((& $uv --version) -notmatch ('^uv ' + [regex]::Escape($uvVersion) + '(\s|$)')) {
        throw 'Local uv version does not match its pin.'
    }
    if ((& $node --version) -ne "v$nodeVersion") { throw 'Local Node version mismatch.' }
    if ((& $node $npm --version) -ne $package.engines.npm) { throw 'Bundled npm version mismatch.' }
    if ($ToolsOnly) { Write-Output 'Pinned tools ready; environment installation was not requested.'; exit 0 }
    $env:PATH = "$nodeDirectory;$uvDirectory;$env:PATH"
    $env:UV_CACHE_DIR = Join-Path $repo '.tools/cache/uv'
    $env:UV_PYTHON_INSTALL_DIR = Join-Path $repo '.tools/python'
    $env:UV_PYTHON_BIN_DIR = Join-Path $repo '.tools/python-bin'
    $env:UV_PROJECT_ENVIRONMENT = Join-Path $repo '.venv'
    $env:UV_NO_CONFIG = '1'
    # Use the explicit project config; disregard machine-wide npm settings.
    $env:npm_config_cache = Join-Path $repo '.tools/cache/npm'
    $env:npm_config_userconfig = Join-Path $repo '.tools/empty-user.npmrc'
    $env:npm_config_globalconfig = Join-Path $repo '.tools/empty-global.npmrc'
    Run-Native $uv @('python','install',$pythonVersion,'--no-bin','--no-registry','--config-file','.tools/uv.toml')
    Run-Native $uv @('sync','--locked','--managed-python','--config-file','.tools/uv.toml')
    Run-Native $node @($npm,'ci','--ignore-scripts','--no-audit','--no-fund')
    Run-Native (Join-Path $repo '.venv/Scripts/python.exe') @('scripts/verify.py')
    Write-Output 'Bootstrap and verification passed.'
} catch {
    [Console]::Error.WriteLine("BOOTSTRAP FAILED: $($_.Exception.Message)")
    exit 1
} finally {
    foreach ($key in $savedEnvironment.Keys) {
        [Environment]::SetEnvironmentVariable($key, $savedEnvironment[$key], 'Process')
    }
    Set-Location -LiteralPath $previousLocation
}
