move .\BasicUtilities\BasicUtilities.py BasicUtilities.py
del /s /f /q .\BasicUtilities\*
rmdir .\BasicUtilities\.temp
.\pyinstaller --icon=bu.ico --version-file=vf.txt --noconfirm BasicUtilities.py
.\pyinstaller --icon=bu.ico --version-file=vf.txt --onefile BasicUtilities.py
xcopy /s /e .\dist\BasicUtilities .\BasicUtilities
