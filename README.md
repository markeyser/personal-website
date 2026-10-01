# Marcos Keyser — personal website

A minimalist professional portfolio for applied AI science and engineering, built with semantic HTML, CSS, and a small progressive-enhancement script. No dependencies, build step, analytics, cookies, or backend.

**Website:** https://markeyser.github.io/personal-website/

## Edit

- `index.html`: public-facing content, research tracks, links, and search metadata.
- `styles.css`: responsive layout, typography, accessibility, and print styles.
- `script.js`: accessible research tabs and footer year.
- `assets/`: research diagrams, résumés, and favicon.
- `diagrams/`: editable Excalidraw source scenes for the research diagrams.
- `scripts/export-diagrams.py`: exports those scenes to SVG using the website's palette and font stacks. Run `python3 scripts/export-diagrams.py` after changing a scene or theme; refresh the PNG exports when needed.

Content is based on Marcos's professional account. Keep production delivery, implemented research prototypes, and planned research extensions distinct. Do not introduce unsupported metrics or claims.

## Preview

Serve the repository root with any static HTTP server, or open `index.html` directly in a browser. For example, `python3 -m http.server 8000` provides a local preview at `http://localhost:8000`.

## Publish

GitHub Pages publishes the root of `main`. Push a reviewed commit to `main` to update the site. `.nojekyll` disables Jekyll processing; all asset references work under the `/personal-website/` project path.

The GitHub repository is public. Commit only website content and files intended for public distribution.

## Review checklist

- Check desktop and narrow mobile layouts, keyboard navigation, and research tabs.
- Expand each diagram and verify résumé downloads.
- Check contact links and any updated external sources.
- Keep all research content readable when JavaScript is disabled.
- Confirm the GitHub Pages deployment matches the published commit.
