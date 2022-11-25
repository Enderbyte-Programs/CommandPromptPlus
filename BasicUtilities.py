SYSVERSION = "3.0.0"
VERID = 242
HASINTERNET = False

ASSEMBLEDVERSION = f"Basic Utilities {SYSVERSION}"
print("Basic Utilities",ASSEMBLEDVERSION,"(c) 2021-2022 Enderbyte Programs LLC")
import logging
logging.basicConfig(filename="BasicUtilities.log",filemode="a+",level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.info("Starting Basic Utilities")
import os
os.system("")
os.system("color")
import random
from traceback import format_tb
import datetime
import platform
ONWINDOWS = [True if platform.system() == "Windows" else False][0]
def handle_exception(type,value,traceback):
    global ASSEMBLEDVERSION
    if issubclass(type, KeyboardInterrupt):
        pass
    else:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        os.system("color 17")
        
        l = format_tb(traceback)
        x = ""
        for item in l:
            x += item
            x += "\n"
        try:
            logging.fatal(str(type).split(" ")[1].replace("'","").replace(">","")+'\n'+str(value)+'\n'+str(x))
        except:
            pass
        
        print(':(                              \n\nBasic Utilities has encountered a critical error. \nIf you didn\'t expect this, please send the following text to the developer:'+'\n'+str(type)+'\n'+str(value)+'\n'+x+"\nDir: "+os.getcwd()+"\nSystem: "+platform.platform())
        print("Preparing dump of variables...")
        crashtypes = ["Oh no, not again!","HA HA HA HA HA! I CRASH A LOT!","GEEGEGGEGEOOOGOOGA","An unhandled exception? I don't see any around here!","Basic Utilities: Completely free of crashes"]#These are from my little sister
        vars = globals().items()
        print("Creating crash report...")
        try:
            if not os.path.isdir(os.getenv("APPDATA")+"\\BasicUtilities\\crash_reports"):
                os.mkdir(os.getenv("APPDATA")+"\\BasicUtilities\\crash_reports")
            with open(os.getenv("APPDATA")+"\\BasicUtilities\\crash_reports\\"+str(datetime.datetime.now()).replace(":","").replace(" ","_")+".txt","w+") as f:
                f.write("-----Basic Utilities Crash Report-----\n")
                f.write(random.choice(crashtypes)+"\n\n")
                f.write("CWD: "+os.getcwd())
                f.write("\nPlatform: "+platform.system())
                f.write("\nPlatformVersion: "+platform.version()+"\n")
                f.write("Version: "+ASSEMBLEDVERSION+"\n")
                for item in list(vars):
                    f.write(str(item[0]))
                    f.write(" : ")
                    f.write(str(item[1]))
                    f.write("\n")
                f.write("End of crash report")
        except:
            print("Failed to create crash report")
        print("Crash report and variable dump complete")
        print("Find the crash report at",os.getenv("APPDATA")+"\\BasicUtilities\\crash_reports")
        del vars
        input("Press enter or return to exit")
        os.system("color 07")
import sys
sys.excepthook = handle_exception
import socket
import requests
import urllib
import json
import platform
import threading
import termcolor
try:
    urllib.request.urlretrieve("https://www.pastebin.com")
except:
    logging.error("No internet connection")
else:
    HASINTERNET = True
    TPDATA = requests.get("https://pastebin.com/raw/0kwEMYJj").json()
appdatadir = os.getenv("APPDATA")+"\\BasicUtilities"
if not os.path.isdir(appdatadir):
    os.mkdir(appdatadir)
defaultappdata = {
    "stats" : {
        "times_started" : 0,
        "commands_run" : 0
    },
    "config": {
        "allowDownloads" : True,
        "allowFormatting" : True,
        "username" : "DefaultUser"
    }
}
if not os.path.isfile(appdatadir + "\\appdata.json"):
    with open(appdatadir + "\\appdata.json","w+") as f:
        f.write(json.dumps(defaultappdata))
        APPDATA = defaultappdata
else:
    with open(appdatadir + "\\appdata.json","r+") as f:
        try:
            APPDATA = json.load(f)
        except:
            APPDATA = defaultappdata
            f.write(defaultappdata)
SERVERIP = TPDATA["serverip"]
def sd():
    try:
        s = socket.socket()
        s.connect((SERVERIP.split(":")[0],int(SERVERIP.split(":")[1])))
        s.sendall(bytearray(f"&&BU${str(SYSVERSION)}${platform.platform()}",'utf-8'))
    except Exception as e:
        logging.error(f"Failed to send data! {e}")
threading.Thread(target=sd).start()
if TPDATA["message"]["emergency"]:
    if APPDATA["config"]["allowFormatting"]:
        termcolor.cprint("URGENT MESSAGE: "+TPDATA["message"]["msg"],"red",attrs=["bold"])
    else:
        print("URGENT MESSAGE: "+TPDATA["message"]["msg"])

cwd = os.getcwd()

def interpret(cmd):
    command = cmd.split(" ")[0]
    if command.replace(" ","") == "":
        return
    elif command == "help":
        if len(cmd.split(" ")) < 1:
            _cd = cmd.split(" ")[1]
            if _cd == "help":
                print("Help Command Version 2.0\nPlaceholder")
            elif _cd == "stop":
                print("")
        else:
            print("Commands Reference:")
            print("help           | 2.0 | Prints Help Menu")
            print("stop           | 2.0 | Stops Basic Utilities")

            print("\nFor more information about a command run command <command name>")
    elif command == "stop":
        if len(cmd.split(" ")) < 1:
            _cd = cmd.split(" ")[1]
            if _cd == "-a":
                if ONWINDOWS:
                    os.system("taskkill /f /im BasicUtilities.exe")
                else:
                    raise NotImplementedError("This function is not available")
        else:
            sys.exit()

logging.info("Startup finished")

while True:
    cmd = input(cwd+">")
    interpret(cmd)