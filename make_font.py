import fontforge
import os

font = fontforge.font()
font.fontname = "MyFont"
font.familyname = "MyFont"
font.fullname = "MyFont"

# Map glyphs to Unicode codepoints
glyph_map = {
    'A': ord('A'),
    'B': ord('B'),
    'C': ord('C'),
}

for glyph_name, codepoint in glyph_map.items():
    svg_path = os.path.join('glyphs', f'{glyph_name}.svg')
    if os.path.exists(svg_path):
        glyph = font.createChar(codepoint, glyph_name)
        glyph.importOutlines(svg_path)
        glyph.width = 1000
    else:
        print(f'SVG for {glyph_name} not found!')

font.generate('MyFont.ttf')
print("MyFont.ttf generated with glyphs A, B, C.") 