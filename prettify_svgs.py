import os
import xml.dom.minidom

glyph_dir = 'glyphs'
for fname in os.listdir(glyph_dir):
    if fname.endswith('.svg'):
        path = os.path.join(glyph_dir, fname)
        with open(path, 'r') as f:
            svg = f.read()
        pretty = xml.dom.minidom.parseString(svg).toprettyxml()
        with open(path, 'w') as f:
            f.write(pretty)
print('SVG files prettified.') 