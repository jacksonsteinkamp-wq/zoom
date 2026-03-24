# Center Zoom Magnifier

#TODO remove this section
this is just for me and idrk why I did this I ofc wont turn it in. I will only turn in the launch.py

Basically the program zooms in on the center of the monitor using a Windows API ([MagSetFullscreenTransform](https://learn.microsoft.com/en-us/windows/win32/api/magnification/nf-magnification-magsetfullscreentransform)). The user can set up settings so they can use multiple keys to zoom in at different multipliers, and can also save these settings. The goal of the program is to make it easier to inspect small on-screen details and improve accessibility for users who need larger text or visuals. It is a simple, customizable, open source program. The default Windows magnifier has multi-key hotkeys that are slow, clunky, and non-customizable, and the zoom isn't stationary (it moves with the mouse, which can be annoying). This program always zooms in on the center, since most content doesn't go all the way to the edges of the screen. (Think articles)

---

## Preset Format

Presets are stored in `presets.txt` in the following format:

`name | keycount (Mode : key : zoom)(Mode : key : zoom) <>`

- `name` — the name of the preset
- `keycount` — the number of key bindings
- Each `(Mode : key : zoom)` defines one key binding
- `<>` appears only on the most recently run preset 
- For examples, check presets.txt

---

## Valid Key Names

Standard keyboard keys (e.g. `p`, `F5`) as well as mouse buttons:

- `left`
- `right`
- `middle`
- `x`
- `x2` #TODO check which keys these are and list it here

---

## Modes

- **Hold** — Zooms in while the key is held, returns to 1x on release
- **Toggle** (coming soon) — Toggles zoom on/off with a keypress
- **AWP** (coming soon) — Cycles through a list of zoom levels with each keypress

---

## Monitor

Currently this only supports the main monitor. If you want to zoom in on a different one, you will have to change your main monitor in the windows settings. It works no matter the resolution and scale. #TODO check this

---
## Planned Features

### Key Enable/Disable Toggle
A designated key will be able to toggle all zoom keys on or off within a preset session. When toggled off, zoom keys are ignored even if pressed. When toggled back on, they resume working normally. A visual and/or audio notification will play when toggling on or off so you always know the current state.

### Toggle Mode
A key binding mode where pressing the key once zooms in and pressing it again returns to 1x, instead of requiring the key to be held.

### AWP / Cycle Mode
A key binding mode that cycles through a list of zoom levels with each press (e.g. 1x → 2x → 3x → 1x). Useful for stepping through zoom levels without holding a key.

### Executable (.exe)
Package the program as a standalone `.exe` so it can be run without a Python installation.

### Zoom Offset
Change presets to have a custom offset, meaning the zoom isn't the center of the monitor.

---

## Likely Impossible

### Multi-Monitor Support
Currently the program targets the main monitor. Future support for additional monitor configurations is planned. This may end up being impossible.

### DPI
Currently your DPI is the same when zoomed in, making the mouse appear to move faster. Future support for scaling DPI with sensitivity. This is likely impossible.

### On-Keypress Input (No Enter Required)
Menu navigation currently requires pressing Enter after each input. The plan is to make selections register instantly on keypress, making the UI faster and more responsive.

### Multi Monitor Support
The ability to use multiple monitors and choose which one you want to use on launch every time. Likely impossible.