@echo off
setlocal enabledelayedexpansion

echo Building C++ SVG generator...
g++ generate_glyphs.cpp -o generate_glyphs.exe

if exist glyphs rmdir /s /q glyphs
mkdir glyphs

echo Generating SVG glyphs...
generate_glyphs.exe

echo Generating TTF font with FontForge...
fontforge -script make_font.py

echo Done! Font is in MyFont.ttf 