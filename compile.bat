move .\BasicUtilities\BasicUtilities.py BasicUtilities.py
del /s /f /q .\BasicUtilities\*
rmdir .\BasicUtilities\.temp
.\pyinstaller --icon=bu.ico --version-file=vf.txt --noconfirm BasicUtilities.py
.\pyinstaller --icon=bu.ico --version-file=vf.txt --onefile BasicUtilities.py
xcopy /s /e .\dist\BasicUtilities .\BasicUtilities
copy bu.ico .\BasicUtilities\bu.ico
copy turtle.ico .\BasicUtilities\turtle.ico
"C:\Program Files (x86)\Inno Setup 6\iscc.exe" bu.iss
del /s /f /q .\BasicUtilities\*
rmdir /s /q .\BasicUtilities\
mkdir BasicUtilities
move BasicUtilities.py .\BasicUtilities\BasicUtilities.py