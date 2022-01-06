from tkinter import messagebox, Tk
import platform
import os
if str(platform.system()) == 'Windows':
    has_windows = True
else:
    has_windows = False
if not has_windows:
    Tk().withdraw()
    messagebox.showwarning('BUchk','You do not have the reccomended OS for this program. Some features may work incorrectly.')
    os.system('python3 -m pip install playsound')
    os.system('python3 -m pip install requests')
    os.system('python3 -m pip install keyboard')
    os.system('python3 -m pip install termcolor')
    os.system('python3 -m pip install packaging')
else:
    os.system('py -m pip install playsound')
    os.system('py -m pip install requests')
    os.system('py -m pip install winsound')
    os.system('py -m pip install keyboard')
    os.system('py -m pip install termcolor')
    os.system('py -m pip install packaging')
try:
    import pyutils39
except:
    Tk().withdraw()
    messagebox.showwarning('Basic Utilities dep','You do not have the custom library pyutils39 installed. Download it from the github repo!')
input('All Finished! Press enter to start Basic Utilities.')
try:
    os.startfile("BasicUtilities.py")
except:
    Tk().withdraw()
    messagebox.showerror('Error','Could not find BasicUtilities.py')
