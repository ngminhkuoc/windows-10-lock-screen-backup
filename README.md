# windows-10-lock-screen-backup
This tool is to backup all lock screens of  Windows 10 Spotlight to a local folder

The implementation is just 1 simple file windows-lock-screen-backup.py. I compiled to exe file by using these below script:
```
pip install pyinstaller
pyinstaller -F windows-lock-screen-backup.py
```
I use Windows Task Scheduler to setup a daily task:

The action should be 
```
"[local_folder_path]\windows-lock-screen-backup.exe" [username] [local_output_folder]
```