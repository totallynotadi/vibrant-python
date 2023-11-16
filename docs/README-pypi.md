
<p align="center">
<img src="https://github.com/totallynotadi/vibrant-python/blob/main/docs/vibrant-logo.svg?raw=true"/>

<div align="center">

# Vibrant

#### Python port for [node-vibrant](https://github.com/Vibrant-Colors/node-vibrant) to extract color palettes from images in format similar to palettes in Android.

</div>
</p>

### Installation

```bash
python -m pip install vibrant-python
```

### Features
- [X] Color palette extraction
- [X] Fully typed codebase
- [X] Color space conversion utilities
- [ ] Contrast ration calculation

This library is a one-to-one port of the [node-vibrant](https://github.com/Vibrant-Colors/node-vibrant) package which itself is port of [Vibrant.js](https://github.com/jariz/vibrant.js). They all aim to produce color palette from images in format similar to the [Palette](https://developer.android.com/develop/ui/views/graphics/palette-colors#extract-color-profiles) module in Android. The primary use-case of this for me was to produce colors from album cover arts (simply extracting the most prominent colors isn't always the best fit in most cases and requires a more sophisticated solution) where such color palettes work well.

The Python codebase is fully typed so great editor support is expected for intuitive use. Check out Docs for more info.

### Demo


```py
from vibrant import Vibrant

v = Vibrant()

palette = v.get_palette('/path/to/image')

color = palette.dark_muted

print(color.rgb)
```

<p align="center">
<img src="https://github.com/totallynotadi/vibrant-python/blob/main/docs/demo.png?raw=true" width="480" style="margin-top: 10px"/>
</p>
