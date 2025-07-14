# Logo Placement Instructions

## Where to add your logo:

Place your logo image file in this folder: `static/images/`

## File requirements:

- **Filename**: `logo.png` (recommended)
- **Format**: PNG, JPG, or SVG (PNG recommended for best quality)
- **Size**: Recommended 150x150 pixels or larger (will be automatically resized)
- **Background**: Transparent background recommended for best appearance

## How it works:

1. The login page will automatically look for `logo.png` in this folder
2. If the logo file exists, it will be displayed above the login form
3. If no logo file is found, a stylish placeholder with "75 FLOW" text will be shown instead
4. The logo will have a nice hover effect and rounded corners

## Example:

```
static/
└── images/
    └── logo.png  ← Place your logo here
```

## Supported formats:

- PNG (recommended)
- JPG/JPEG
- SVG
- GIF

The logo will be automatically resized to fit the design while maintaining aspect ratio. 