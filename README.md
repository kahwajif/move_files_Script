# move_files_Script
A script for Windows that moves downloaded files from my Downloads folder to their respective designated folder. 

Example: MP3 files -> Music Folder, PNG and JPEG -> Pictures Folder, MP4 -> Video Folders

Files with already existing names will have a random number generated and appended to them.

## Executing as Background Process And on Startup
1. Install pyinstaller `pip install pyinstaller`

1. Create executable file `pyinstaller --noconsole --onefile  move_files_script.py`

1. In the dist folder, create shortcut of `move_files_script.exe` in `C:\Users\feras\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`