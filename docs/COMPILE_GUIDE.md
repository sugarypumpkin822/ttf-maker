# Compilation & Packaging Guide: TTF Font Maker GUI

This guide explains how to compile the TTF Font Maker GUI into a standalone Windows `.exe` and create an installer.

---

## 1. Prerequisites

- **Python 3.x** (https://www.python.org/downloads/)
- **Pip** (comes with Python)
- **FontForge** (https://fontforge.org/en-US/downloads/)
    - Must be installed and available in your system PATH
- **Pillow** (for icon generation)
- **PyInstaller** (for building the .exe)
- **Inno Setup** (for creating a Windows installer, optional)

---

## 2. Install Python Dependencies

Open a terminal (Command Prompt or PowerShell) in your project directory and run:

```sh
pip install -r requirements-gui.txt
pip install pyinstaller
```

---

## 3. Generate the Application Icon

Run the provided script to create `icon.ico`:

```sh
python make_icon.py
```

This will generate a multi-resolution Windows icon for your application.

---

## 4. Compile the GUI to a Standalone .exe

Use PyInstaller to bundle your GUI:

```sh
pyinstaller --onefile --windowed --icon=icon.ico font_gui.py
```

- The `--onefile` flag creates a single executable.
- The `--windowed` flag prevents a console window from appearing.
- The `--icon=icon.ico` flag sets your custom icon.
- The output `.exe` will be in the `dist/` folder.

---

## 5. Test the .exe

Navigate to the `dist/` folder and run `font_gui.exe` to ensure it works as expected.

---

## 6. (Optional) Create a Windows Installer

1. **Install Inno Setup:**
   - Download from https://jrsoftware.org/isinfo.php
2. **Edit `installer_script.iss` if needed.**
3. **Build the installer:**
   - Open `installer_script.iss` in Inno Setup Compiler
   - Click "Compile"
   - The installer `.exe` will be created in your project directory

---

## 7. Distribute

- Share the installer or the standalone `.exe` with users.
- Make sure to include instructions that FontForge must be installed and in the system PATH for font generation to work.

---

## Troubleshooting

- **FontForge not found:** Ensure FontForge is installed and its directory is added to your system PATH.
- **Missing DLLs:** If the `.exe` fails to run, try running it from the command line to see error messages. You may need to install additional Visual C++ Redistributables.
- **Icon not showing:** Ensure `icon.ico` exists and is specified in the PyInstaller command.

---

## Example Workflow

```sh
pip install -r requirements-gui.txt
pip install pyinstaller
python make_icon.py
pyinstaller --onefile --windowed --icon=icon.ico font_gui.py
```

Then test your `.exe` in the `dist/` folder! 