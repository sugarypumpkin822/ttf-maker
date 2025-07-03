# Usage Guide: TTF Font Maker GUI

## How to Use

1. Run the GUI:
   - With Python: `python font_gui.py`
   - Or, run the compiled `.exe` if provided.

2. In the text box, enter glyph-shape pairs, e.g.:
   ```
   A: triangle, B: square, C: circle
   ```

3. Click "Generate Font". The font file `PromptFont.ttf` will be created in the same folder.

## Supported Shapes
- triangle
- square
- circle

## Requirements
- Python 3
- Pillow (for icon generation)
- FontForge (must be installed and in your PATH)

## Compiling to .exe
- Install PyInstaller: `pip install pyinstaller`
- Run: `pyinstaller --onefile --windowed --icon=icon.ico font_gui.py`

## Troubleshooting
- If FontForge is not found, ensure it is installed and available in your system PATH. 