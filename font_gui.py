import tkinter as tk
from tkinter import messagebox
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

def generate_font(prompt, output_callback):
    pairs = [p.strip() for p in prompt.split(',') if ':' in p]
    glyphs = {}
    for pair in pairs:
        glyph, shape = [x.strip().upper() if i == 0 else x.strip().lower() for i, x in enumerate(pair.split(':', 1))]
        path = shape_to_svg_path(shape)
        if path:
            glyphs[glyph] = path
        else:
            output_callback(f"Unknown shape '{shape}' for glyph '{glyph}', skipping.\n")

    if not glyphs:
        output_callback("No valid glyphs found. Exiting.\n")
        return

    os.makedirs('glyphs', exist_ok=True)
    for glyph, path in glyphs.items():
        with open(f'glyphs/{glyph}.svg', 'w') as f:
            f.write(f'<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1000\" height=\"1000\" viewBox=\"0 0 1000 1000\">\n')
            f.write(f'  <path d=\"{path}\" fill=\"black\"/>\n')
            f.write('</svg>\n')
        output_callback(f"Generated SVG for {glyph} as {path}.\n")

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

    output_callback("Generating TTF font with FontForge...\n")
    try:
        subprocess.run(['fontforge', '-script', fontforge_script], check=True)
        output_callback("Done! Font is in PromptFont.ttf\n")
    except Exception as e:
        output_callback(f"Error running FontForge: {e}\n")

class FontGUI:
    def __init__(self, root):
        self.root = root
        root.title("TTF Font Maker GUI")
        root.geometry("500x350")

        self.label = tk.Label(root, text="Enter glyph-shape pairs (e.g., A: triangle, B: square):")
        self.label.pack(pady=10)

        self.text_entry = tk.Text(root, height=4, width=50)
        self.text_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Font", command=self.on_generate)
        self.generate_button.pack(pady=10)

        self.output = tk.Text(root, height=10, width=60, state='disabled', bg='#f0f0f0')
        self.output.pack(pady=5)

    def append_output(self, msg):
        self.output.config(state='normal')
        self.output.insert(tk.END, msg)
        self.output.see(tk.END)
        self.output.config(state='disabled')

    def on_generate(self):
        prompt = self.text_entry.get("1.0", tk.END).strip()
        self.output.config(state='normal')
        self.output.delete("1.0", tk.END)
        self.output.config(state='disabled')
        if not prompt:
            messagebox.showwarning("Input required", "Please enter glyph-shape pairs.")
            return
        self.append_output(f"Processing: {prompt}\n")
        self.root.after(100, lambda: generate_font(prompt, self.append_output))

if __name__ == "__main__":
    root = tk.Tk()
    app = FontGUI(root)
    root.mainloop() 