# One job boundary shared by GitHub Actions and fresh local checkouts.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$repo = Split-Path -Parent $PSScriptRoot
$previousLocation = Get-Location
$evidenceDirectory = Join-Path $repo '.tools/ci'
$transcribing = $false
$exitCode = 1
$record = [ordered]@{
    timestamp_utc = [DateTime]::UtcNow.ToString('o')
    status = 'failed'
    source_revision = $null
    runner_os = $env:RUNNER_OS
    runner_arch = $env:RUNNER_ARCH
    image_os = $env:ImageOS
    image_version = $env:ImageVersion
    run_id = $env:GITHUB_RUN_ID
    run_attempt = $env:GITHUB_RUN_ATTEMPT
    cold_paths_absent = [ordered]@{}
    stages = @()
}
function Invoke-Stage([string]$Name, [string]$Program, [string[]]$Arguments) {
    Write-Output "CI: $Name"
    & $Program @Arguments
    $stageExit = $LASTEXITCODE
    $record.stages += [ordered]@{ name = $Name; exit_code = $stageExit }
    if ($stageExit -ne 0) { throw "$Name failed (exit $stageExit). See job.log and verifier evidence." }
}
try {
    Set-Location -LiteralPath $repo
    foreach ($name in @('.tools','.venv','node_modules')) {
        $record.cold_paths_absent[$name] = !(Test-Path -LiteralPath (Join-Path $repo $name))
    }
    New-Item -ItemType Directory -Force -Path $evidenceDirectory | Out-Null
    Start-Transcript -LiteralPath (Join-Path $evidenceDirectory 'job.log') -Force | Out-Null
    $transcribing = $true
    if ($record.cold_paths_absent.Values -contains $false) {
        throw 'CI requires a fresh checkout without .tools, .venv or node_modules. Use Verify.cmd for an existing environment.'
    }
    $record.source_revision = (& git rev-parse HEAD)
    if ($LASTEXITCODE -ne 0) { throw 'Cannot identify source revision.' }
    Invoke-Stage 'bootstrap and required checks' (Join-Path $repo 'Bootstrap.cmd') @()
    $python = Join-Path $repo '.venv/Scripts/python.exe'
    Invoke-Stage 'planning and Markdown refusal probes' $python @('scripts/ci_refusal_probe.py')
    # A clean CI checkout has no working-tree diff; inspect the submitted commit
    # range as well as the verifier's normal working-tree whitespace gate.
    $diffBase = $env:CI_DIFF_BASE
    if ($diffBase -match '^[a-fA-F0-9]{40}$' -and $diffBase -notmatch '^0{40}$') {
        $record.diff_base = $diffBase
        Invoke-Stage 'submitted diff whitespace' 'git' @('diff','--check',$diffBase,'HEAD')
    } else {
        $record.diff_base = 'HEAD commit (no event base)'
        Invoke-Stage 'submitted commit whitespace' 'git' @('show','--check','--format=','--diff-merges=first-parent','HEAD')
    }
    $record.status = 'passed'
    $exitCode = 0
    Write-Output 'PASS: automated accepted checks and refusal probes.'
} catch {
    $record.error = $_.Exception.Message
    Write-Output "CI FAILED: $($record.error)"
} finally {
    $record.exit_code = $exitCode
    $record | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $evidenceDirectory 'job.json') -Encoding UTF8
    if ($transcribing) { Stop-Transcript | Out-Null }
    Set-Location -LiteralPath $previousLocation
}
exit $exitCode
