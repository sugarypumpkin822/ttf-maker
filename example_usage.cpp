#include <ft2build.h>
#include FT_FREETYPE_H
#include <iostream>

int main() {
    FT_Library library;
    if (FT_Init_FreeType(&library)) {
        std::cerr << "Could not initialize FreeType library\n";
        return 1;
    }

    FT_Face face;
    if (FT_New_Face(library, "MyFont.ttf", 0, &face)) {
        std::cerr << "Could not open MyFont.ttf\n";
        FT_Done_FreeType(library);
        return 1;
    }

    FT_Set_Pixel_Sizes(face, 0, 64);
    if (FT_Load_Char(face, 'A', FT_LOAD_RENDER)) {
        std::cerr << "Could not load character 'A'\n";
    } else {
        std::cout << "Loaded glyph for 'A' (bitmap size: "
                  << face->glyph->bitmap.width << "x" << face->glyph->bitmap.rows << ")\n";
    }

    FT_Done_Face(face);
    FT_Done_FreeType(library);
    return 0;
} 