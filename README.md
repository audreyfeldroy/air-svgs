# Air SVG Assets

Official logo assets for [Air](https://github.com/feldroy/air), the Python web framework.

## Quick Start

```bash
git clone https://github.com/feldroy/air-svgs.git
```

Or download individual files from the `static/` directory.

## Available Logos

### Core Logos

| File | Description | Use Case |
|------|-------------|----------|
| `air.svg` | Black wordmark, light blue dot | Light backgrounds |
| `air-dark.svg` | White wordmark, light blue dot | Dark backgrounds |

### Style Variants

| File | Description |
|------|-------------|
| `air-mono.svg` | Single color (dark gray) |
| `air-mono-white.svg` | Single color (white) |
| `air-gradient.svg` | Modern gradient (sky blue to purple) |
| `air-knockout.svg` | Knocked out of dark background |
| `air-watermark.svg` | 12% opacity for watermarks |

### Animated Variants

All animations respect `prefers-reduced-motion` for accessibility.

| File | Animation |
|------|-----------|
| `air-animated-pulse.svg` | Gentle breathing dot |
| `air-animated-hover.svg` | Interactive hover effect |
| `air-animated-spinner.svg` | Loading state with orbiting dot |
| `air-animated-float.svg` | Weightless drifting motion |
| `air-animated-shimmer.svg` | Light sweep across dot |

Dark theme versions available with `-dark-` prefix (e.g., `air-dark-animated-pulse.svg`).

## Usage

### HTML

```html
<img src="air.svg" alt="Air" width="200">
```

### Inline SVG

```html
<svg role="img" aria-labelledby="air-logo">
  <title id="air-logo">Air</title>
  <!-- SVG content -->
</svg>
```

### CSS Background

```css
.logo {
  background: url('air.svg') no-repeat center;
  background-size: contain;
}
```

## Accessibility

All SVGs include:
- `role="img"` attribute
- `<title>` element with "Air" text
- `aria-labelledby` linking to the title
- `prefers-reduced-motion` support (animated variants)

## Dimensions

- Viewbox: `0 0 393.187 188.368`
- Default size: 1486 x 712 px
- Aspect ratio: ~2.1:1

## Development

Preview the logos locally:

```bash
just run
```

Visit http://localhost:8000 to see the gallery.

## License

See [usage-policy.md](pages/usage-policy.md) for trademark and usage guidelines.
