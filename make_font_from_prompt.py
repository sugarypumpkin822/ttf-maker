import os
import subprocess

def shape_to_svg_path(shape):
    if shape == 'triangle':
        return "M500,200 L800,800 L200,800 Z"
    elif shape == 'square':
        return "M250,250 L750,250 L750,750 L250,750 Z"
    elif shape == 'circle':
        return "M500,200 A300,300 0 1,1 499,200 Z"
    else:
        return None

def main():
    prompt = input("Describe your font (e.g., 'A: triangle, B: square, C: circle'): ")
    pairs = [p.strip() for p in prompt.split(',') if ':' in p]
    glyphs = {}
    for pair in pairs:
        glyph, shape = [x.strip().upper() if i == 0 else x.strip().lower() for i, x in enumerate(pair.split(':', 1))]
        path = shape_to_svg_path(shape)
        if path:
            glyphs[glyph] = path
        else:
            print(f"Unknown shape '{shape}' for glyph '{glyph}', skipping.")

    if not glyphs:
        print("No valid glyphs found. Exiting.")
        return

    os.makedirs('glyphs', exist_ok=True)
    for glyph, path in glyphs.items():
        with open(f'glyphs/{glyph}.svg', 'w') as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000" viewBox="0 0 1000 1000">\n')
            f.write(f'  <path d="{path}" fill="black"/>\n')
            f.write('</svg>\n')
        print(f"Generated SVG for {glyph} as {path}.")

    # Generate FontForge script dynamically
    fontforge_script = 'make_font_from_prompt_ff.py'
    with open(fontforge_script, 'w') as ff:
        ff.write('import fontforge\n')
        ff.write('import os\n')
        ff.write('font = fontforge.font()\n')
        ff.write('font.fontname = "PromptFont"\n')
        ff.write('font.familyname = "PromptFont"\n')
        ff.write('font.fullname = "PromptFont"\n')
        for glyph in glyphs:
            ff.write(f"glyph = font.createChar(ord('{glyph}'), '{glyph}')\n")
            ff.write(f"glyph.importOutlines(os.path.join('glyphs', '{glyph}.svg'))\n")
            ff.write("glyph.width = 1000\n")
        ff.write('font.generate("PromptFont.ttf")\n')
        ff.write('print("PromptFont.ttf generated.")\n')

    print("Generating TTF font with FontForge...")
    subprocess.run(['fontforge', '-script', fontforge_script], check=True)
    print("Done! Font is in PromptFont.ttf")

if __name__ == "__main__":
    main() 