; Sample Inno Setup script for TTF Font Maker GUI
[Setup]
AppName=TTF Font Maker
AppVersion=0.1.0
DefaultDirName={pf}\TTF Font Maker
DefaultGroupName=TTF Font Maker
OutputDir=.
OutputBaseFilename=TTF_Font_Maker_Installer
SetupIconFile=icon.ico

[Files]
Source: "dist\font_gui.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"

[Icons]
Name: "{group}\TTF Font Maker"; Filename: "{app}\font_gui.exe"; IconFilename: "{app}\icon.ico" 