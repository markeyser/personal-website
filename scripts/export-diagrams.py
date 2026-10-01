"""Export the existing Excalidraw scenes as website-themed, accessible SVGs.

Only presentation changes: source text, coordinates, connectors, and research
status are preserved. Theme tokens come from the website stylesheet.
"""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / 'styles.css').read_text()
TOKENS = dict(re.findall(r'--([\w-]+):([^;}]+)', CSS.split('}', 1)[0]))


def render(source):
    scene = json.loads(source.read_text())
    elements = [e for e in scene['elements'] if not e.get('isDeleted')]
    xs, ys = [], []
    for e in elements:
        if e['type'] in ('line', 'arrow'):
            xs.extend(e['x'] + p[0] for p in e['points'])
            ys.extend(e['y'] + p[1] for p in e['points'])
        else:
            xs.extend((e['x'], e['x'] + e['width']))
            ys.extend((e['y'], e['y'] + e['height']))
    x, y = min(xs) - 44, min(ys) - 40
    width, height = max(xs) - x + 44, max(ys) - y + 40
    title = next(e['text'] for e in elements if e['id'].endswith('-title'))
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:g}" height="{height:g}" viewBox="{x:g} {y:g} {width:g} {height:g}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{escape(title)}</title>',
           '<desc id="desc">Research evolution diagram. Solid connectors show capability development; dashed connectors mark research extensions. Read the adjacent webpage for the text overview.</desc>',
           '<style>',
           f'text{{font-family:{TOKENS["sans"]};font-size:22px;fill:{TOKENS["muted"]};font-weight:400}}',
           f'.title,.heading,.subheading{{font-family:{TOKENS["serif"]};fill:{TOKENS["ink"]}}}',
           '.title{font-size:42px;letter-spacing:-1px}.heading{font-size:29px;letter-spacing:-.3px}.subheading{font-size:26px}',
           f'.subtitle{{font-family:{TOKENS["mono"]};font-size:16px;fill:{TOKENS["green"]};letter-spacing:.3px}}',
           f'.footer,.caption{{font-size:19px;fill:{TOKENS["green"]}}}',
           f'.accent{{fill:{TOKENS["green"]}}}',
           '</style>',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="'+TOKENS['green']+'" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>',
           f'<rect x="{x:g}" y="{y:g}" width="{width:g}" height="{height:g}" fill="{TOKENS["paper"]}"/>']
    for e in elements:
        ident = escape(e['id'], quote=True)
        ex, ey, w, h = e['x'], e['y'], e['width'], e['height']
        dashed = ' stroke-dasharray="7 7"' if e.get('strokeStyle') == 'dashed' else ''
        if e['type'] in ('line', 'arrow'):
            points = ' '.join(f'{ex+p[0]:g},{ey+p[1]:g}' for p in e['points'])
            arrow = ' marker-end="url(#arrow)"' if e.get('endArrowhead') else ''
            color = TOKENS['line'] if 'divider' in ident else '#8ca08b'
            out.append(f'<polyline id="{ident}" points="{points}" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"{dashed}{arrow}/>')
        elif e['type'] == 'ellipse':
            fill = TOKENS['paper'] if dashed else TOKENS['green']
            out.append(f'<ellipse id="{ident}" cx="{ex+w/2:g}" cy="{ey+h/2:g}" rx="{w/2:g}" ry="{h/2:g}" fill="{fill}" stroke="{TOKENS["green"]}" stroke-width="1.5"{dashed}/>')
        elif e['type'] == 'rectangle':
            out.append(f'<rect id="{ident}" x="{ex:g}" y="{ey:g}" width="{w:g}" height="{h:g}" rx="4" fill="{TOKENS["soft"]}" stroke="{TOKENS["line"]}" stroke-width="1.5"{dashed}/>')
        elif e['type'] == 'text':
            lines = e['text'].split('\n')
            cls, size = '', 22
            if ident.endswith('-title'): cls, size = 'title', 42
            elif ident.endswith('-subtitle'): cls, size = 'subtitle', 16
            elif ident.endswith('-heading'): cls, size = 'heading', 29
            elif 'footer' in ident: cls, size = 'footer', 19
            elif ident == 'reference-link-label': cls, size = 'caption', 19
            elif ident == 'example-verdict': cls = 'accent'
            anchor = e.get('textAlign', 'left')
            tx = ex + w/2 if anchor == 'center' else ex
            anchor = 'middle' if anchor == 'center' else 'start'
            line_height = max(26, e['fontSize'] * e.get('lineHeight', 1.25))
            out.append(f'<text id="{ident}" class="{cls}" text-anchor="{anchor}" data-source-width="{w:g}" data-source-x="{ex:g}">')
            for index, line in enumerate(lines):
                line_class = ' class="subheading"' if ident.endswith('-text') and index == 0 else ''
                baseline = ey + size + index * line_height
                out.append(f'<tspan x="{tx:g}" y="{baseline:g}"{line_class}>{escape(line)}</tspan>')
            out.append('</text>')
        else:
            raise ValueError(f'Unsupported scene element: {e["type"]}')
    out.append('</svg>')
    target = ROOT / 'assets' / f'{source.stem}-journey.svg'
    target.write_text('\n'.join(out) + '\n')
    print(f'{target.name}: {width:g} × {height:g}')


if __name__ == '__main__':
    for source in sorted((ROOT / 'diagrams').glob('*.excalidraw')):
        render(source)
