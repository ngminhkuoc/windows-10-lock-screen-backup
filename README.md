# windows-10-lock-screen-backup
This tool is to backup all lock screens of  Windows 10 Spotlight to a local folder


I use Windows Task Scheduler to setup a daily task:

The action should be 
```
C:\Users\ [username]\AppData\Local\Programs\Python\Python38-32\python.exe "[ local folder path ]\main.py" "C:/Users/[username]/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets" "[local folder path to save image files]"
