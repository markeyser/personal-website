# Initial release verification

Reviewed on October 1, 2026 in Chromium.

- Visually inspected the desktop page at 1440px and mobile page at 390px.
- Checked layouts at 320px, 390px, 768px, and 1440px with no horizontal overflow.
- Switched among all three research tabs; confirmed selected state and visible panel.
- Verified keyboard navigation from the evaluation tab to the agents tab, including focus transfer.
- Expanded all three diagrams and confirmed image decoding.
- Downloaded both résumé PDFs through the browser successfully.
- Disabled JavaScript and verified that all three research tracks remain visible.
- Checked local asset references, fragment links, unique IDs, JavaScript syntax, and browser console errors.
- Preserved source distinctions between production delivery, implemented prototypes, and planned formal-methods research.

The static site has no server-side application, data collection, authentication, or third-party runtime dependencies.

## Diagram theme update — October 1, 2026

- Exported all three research diagrams as SVGs using the website's color and font tokens; refreshed the PNG copies.
- Compared every exported text label against its editable Excalidraw source and checked text widths for clipping.
- Visually inspected all three rendered diagrams and the expanded desktop and mobile page views.
- Checked every research track at 1440px, 390px, and 320px: images decode and the page has no horizontal overflow.
- Verified that mobile diagrams scroll within their own regions and support keyboard arrow navigation.
