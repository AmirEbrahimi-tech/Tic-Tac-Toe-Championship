#define MyAppName "Tic Tac Toe Championship"
#define MyAppVersion "1.0"
#define MyAppPublisher "Amir Ebrahimi"
#define ProjectRoot "C:\Personal files\Amir\Personal Projects\tiktaktoe-python"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputBaseFilename=tic_tac_toe_setup
OutputDir={#ProjectRoot}\installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
DisableStartupPrompt=yes
UninstallDisplayIcon={app}\main.exe
SetupIconFile=C:\Personal files\Amir\Personal Projects\tiktaktoe-python\src\media\icons\favicon.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "{#ProjectRoot}\dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#ProjectRoot}\src\media\*"; DestDir: "{app}\media"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\main.exe"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"

[Run]
Filename: "{app}\main.exe"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent