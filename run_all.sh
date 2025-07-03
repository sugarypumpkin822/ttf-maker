#!/bin/bash
set -e

echo "Building C++ SVG generator..."
g++ generate_glyphs.cpp -o generate_glyphs

echo "Generating SVG glyphs..."
./generate_glyphs

echo "Generating TTF font with FontForge..."
fontforge -script make_font.py

echo "Done! Font is in MyFont.ttf" 