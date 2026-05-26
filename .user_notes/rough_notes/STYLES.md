# **Retro 3D / Early Polygonal 3D Styles**

**Retro 3D**, **low-poly 3D**, **fifth-generation 3D**, **sixth-generation 3D**, **PSX-style**, **N64-style**, or **pre-shader-era 3D**.

But the useful names are more specific:

## Core style names you probably want

| Name / phrase                                | What it describes                                                                   | Common examples                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Low-poly 3D**                              | Sparse polygon models, angular silhouettes, simple geometry                         | *Super Mario 64*, *Tomb Raider*, *Virtua Fighter*           |
| **PSX-style / PS1-style 3D**                 | Low-poly models, low-res textures, texture wobble, dithering, vertex jitter         | *Metal Gear Solid*, *Silent Hill*, *Crash Bandicoot*        |
| **Affine texture mapping / texture warping** | The “wobbly” PS1 wall/floor texture distortion                                      | Very PS1-associated                                         |
| **Vertex jitter / polygon jitter**           | Vertices snap or wobble because of limited precision                                | PS1-style horror and action games                           |
| **Dithered 3D**                              | Grainy color blending caused by limited color depth                                 | PS1, Saturn, some PC/arcade looks                           |
| **Flat-shaded low poly**                     | Polygons have solid colors or very simple lighting, little texture detail           | *Virtua Racing*, *Star Fox*, early arcade 3D                |
| **Gouraud-shaded 3D**                        | Smooth vertex lighting across polygons, often plastic-looking                       | Arcade racers, Saturn/PS1/N64 games                         |
| **Texture-mapped low poly**                  | Low-poly geometry with painted image textures                                       | Most mid/late-90s 3D                                        |
| **Billboard sprite 3D**                      | 2D sprites placed in 3D worlds, often for trees, enemies, effects                   | *Doom*-descended games, *Mario Kart 64*, RPGs               |
| **Pre-rendered 3D backgrounds**              | Static rendered backgrounds with real-time characters                               | *Resident Evil*, *Final Fantasy VII–IX*                     |
| **Pre-rendered sprite 3D / CGI sprites**     | 3D models rendered into 2D sprites                                                  | *Donkey Kong Country*, *Killer Instinct*, some arcade games |
| **Voxel graphics**                           | 3D made from volume-like blocks/points rather than polygons                         | *Comanche*, *Outcast*                                       |
| **Cel-shaded 3D / toon-shaded 3D**           | Cartoon-like outlined or flat-color 3D                                              | *Jet Set Radio*, *The Wind Waker*                           |
| **Fixed-function 3D**                        | Early hardware pipeline before programmable shaders; very useful term for 1995–2005 | Dreamcast, PS2, GameCube, Xbox-era rendering                |
| **Early real-time CGI**                      | When games looked like playable toy-like CGI, often glossy/simple                   | Dreamcast/PS2/GameCube cutscene-adjacent look               |

## Console-flavored names

### PlayStation 1 / Saturn-adjacent look

Call this:

**PSX-style low-poly 3D**, **dithered low-poly 3D**, **affine-textured 3D**, or **warped-texture retro 3D**.

The telltale features are low-poly models, low-resolution textures, dithering, unstable texture perspective, polygon jitter, and heavy fog or darkness. Modern retro-dev discussions commonly identify PS1-style rendering by low-poly models, low-res textures, polygon jitter, lack of depth precision, warped textures, per-vertex lighting, and fog/depth cueing. ([David Colson’s Blog][1])

For the specific “PS1 walls are swimming/wobbling” look, the formal term is **affine texture mapping** or **affine texture warping**.

### Nintendo 64 look

Call this:

**N64-style low-poly 3D**, **filtered low-res 3D**, **mipmapped low-poly 3D**, **foggy low-poly 3D**, or **bilinear-filtered retro 3D**.

N64 has a different look from PS1: smoother/blurry textures, rounded cartoon forms, strong fog, chunky low-poly environments, and less of the PS1 “wobble.” N64 documentation uses terms like **MIP mapping** for distance-based texture handling, and the N64 look is strongly associated with texture filtering and fog. ([Ultra 64][2]) Some modern recreations specifically talk about N64’s distinctive texture filtering, including “3-point bilinear texture filtering.” ([itch.io][3])

Good search terms: **“N64-style 3D,” “3-point texture filtering,” “N64 bilinear filtering,” “low-res filtered textures,” “mipmapped low poly.”**

### Dreamcast look

Call this:

**Dreamcast-era 3D**, **early sixth-generation 3D**, **arcade-style 3D**, **fixed-function 3D**, or **clean low-poly 3D**.

Dreamcast often looks sharper and cleaner than N64/PS1: higher-res textures, smoother models, arcade lighting, colorful materials, and less fog. For *Jet Set Radio*, the specific term is **cel-shaded 3D** or **toon-shaded 3D**.

### PlayStation 2 look

Call this:

**PS2-era 3D**, **sixth-generation low-poly 3D**, **fixed-function 3D**, **vertex-lit 3D**, or **early 2000s real-time 3D**.

PS2 games often had denser models than PS1/N64, but still used painted textures, vertex lighting, bloom/fog tricks, low-resolution buffers, and stylized haze. Good descriptors include **dreamlike PS2 haze**, **post-process bloom**, **vertex-lit environments**, and **texture-heavy 3D**.

### GameCube look

Call this:

**GameCube-era 3D**, **stylized low-poly 3D**, **toon-shaded 3D**, **clean sixth-generation 3D**, or **early shaderless 3D**.

GameCube often had cleaner image quality than PS2, saturated colors, stylized forms, and strong art direction. For games like *The Wind Waker*, use **cel-shaded 3D**, **toon rendering**, or **non-photorealistic rendering**.

## The best “formal” taxonomy

Here’s the vocabulary I’d use when cataloging 1995–2005 3D game art:

1. **Low-poly 3D** — the broad modeling style.
2. **Texture-mapped low-poly 3D** — most console 3D from this era.
3. **Affine-textured 3D** — PS1-style warped textures.
4. **Dithered 3D** — grainy PS1/Saturn/early PC color look.
5. **Vertex-lit 3D** — lighting calculated at vertices, not per pixel.
6. **Gouraud-shaded 3D** — smooth-shaded polygonal lighting.
7. **Flat-shaded 3D** — hard polygon facets, often untextured.
8. **Billboarded 3D** — 2D sprites in a 3D scene.
9. **Pre-rendered 3D** — CGI backgrounds or sprites rendered offline.
10. **Fixed-function 3D** — pre-modern-shader hardware look.
11. **Cel-shaded / toon-shaded 3D** — cartoon rendering.
12. **Arcade 3D** — Model 2/Model 3/Naomi-style clean, bright 3D.
13. **Early real-time CGI** — toy-like, glossy, early-2000s 3D realism.
14. **Sixth-generation 3D** — PS2/GameCube/Dreamcast/Xbox-era look.
15. **Retro 3D** — modern umbrella term for recreating any of these.

## Search terms that will get you better results

Use combinations like:

**“PSX-style low poly”**
**“affine texture mapping aesthetic”**
**“dithered 3D graphics”**
**“vertex jitter PS1 graphics”**
**“N64-style low poly”**
**“3-point bilinear filtering N64”**
**“fixed-function pipeline game art”**
**“pre-shader era 3D graphics”**
**“fifth generation 3D game graphics”**
**“sixth generation 3D game graphics”**
**“pre-rendered backgrounds game art”**
**“billboard sprites in 3D games”**
**“Gouraud shaded low poly”**
**“flat shaded polygonal graphics”**
**“early real-time 3D aesthetic”**

The phrase I think best captures what you’re after overall is:

> **pre-shader-era low-poly 3D**

And when you want the dirtier PS1/N64-specific nostalgia:

**PSX/N64-style retro 3D** or **fifth-generation low-poly 3D**.

[1]: https://www.david-colson.com/2021/11/30/ps1-style-renderer.html?utm_source=chatgpt.com "Building a PS1 style retro 3D renderer - David Colson"
[2]: https://ultra64.ca/files/documentation/online-manuals/man/n64man/misc/glossaryGraphic.html?utm_source=chatgpt.com "N64 Graphics Terminology"
[3]: https://sittingduck.itch.io/n64-material-shader-for-gamemaker?utm_source=chatgpt.com "N64 Material Shader for GameMaker by SittingDuck - Itch.io"

---
