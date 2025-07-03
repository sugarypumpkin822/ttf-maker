#include <iostream>
#include <fstream>
#include <filesystem>

void write_svg(const std::string& filename, const std::string& path_data) {
    std::ofstream file(filename);
    file << "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1000\" height=\"1000\" viewBox=\"0 0 1000 1000\">\n";
    file << "  <path d='" << path_data << "' fill='black'/>\n";
    file << "</svg>\n";
}

int main() {
    std::filesystem::create_directory("glyphs");
    // Simple 'A' shape
    write_svg("glyphs/A.svg", "M200,800 L500,200 L800,800 L650,800 L500,450 L350,800 Z");
    // Simple 'B' shape
    write_svg("glyphs/B.svg", "M250,200 L250,800 Q500,800 500,600 Q500,400 250,400 L500,400 Q750,400 750,600 Q750,800 500,800 L250,800 Z");
    // Simple 'C' shape
    write_svg("glyphs/C.svg", "M750,300 Q600,200 400,200 Q200,200 200,500 Q200,800 400,800 Q600,800 750,700");
    std::cout << "SVG glyphs generated in the 'glyphs' directory.\n";
    return 0;
} 