move .\BasicUtilities\BasicUtilities.py BasicUtilities.py
move .\BasicUtilities\scupdate.py scupdate.py
del /s /f /q .\BasicUtilities\*
del .\dist\BasicUtilities.exe
rmdir .\BasicUtilities\.temp
rmdir .\BasicUtilities\crash_reports
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
move scupdate.py .\BasicUtilities\scupdate.py