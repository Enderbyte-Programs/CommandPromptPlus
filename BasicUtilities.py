SYSVERSION = "3.0.2"
VERID = 245
HASINTERNET = False

ASSEMBLEDVERSION = f"Basic Utilities {SYSVERSION}"
print(ASSEMBLEDVERSION,"(c) 2021-2022 Enderbyte Programs LLC")
import logging
logging.basicConfig(filename="C:\\ProgramData\\BasicUtilities.log",filemode="a+",level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
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
import libread
from shlex import split as parse_args
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


args = sys.argv[1:]
def interpret(cmd: str) -> int:
    command = cmd.split(" ")[0]
    commanddata = parse_args(cmd)
    if command.replace(" ","") == "":
        return 0
    elif command == "help" or command == "?":
        if len(commanddata) > 1:
            _cd = commanddata[1]
            libread.read(appdatadir+f"\\docs\\{_cd}.book")
        else:
            print("Commands Reference:")
            print("     NAME      |          Description")
            print("help           | Prints concise Help Menu")
            print("docs           | Shows documentation")
            print("stop           | Stops Basic Utilities")
            print("setdir         | Set the working directory of this program.")
            print("dir            | Print the workign directory of this program")
            print("\nFor more information about a command run command <command name>")
        return 0
    elif command == "docs" :
        libread.read(appdatadir+"\\docs\\fullmanual.book")
        return 0
    elif command == "stop" or command == "exit":
        if len(cmd.split(" ")) < 1:
            _cd = cmd.split(" ")[1]
            if _cd == "-a":
                if ONWINDOWS:
                    os.system("taskkill /f /im BasicUtilities.exe")
                    return 0
                else:
                    raise NotImplementedError("This function is not available")
                    return -1
        else:
            sys.exit()
    elif command == "cd" or command == "setdir":
        if len(commanddata)==0 or not commanddata or commanddata == []:
            print(f"setdir failed: No path given.")
            return -1
        try:
            ldset = commanddata[1]
        except IndexError:
            print(f"setdir failed: No path given.")
            return -1
        try:
            os.chdir(ldset)
        except Exception as e:
            print(f"setdir failed: {str(e)}")
            return -1
        return 0
    elif command == "dir":
        print(os.getcwd())
        return 0
    return 0
if len(args) > 0:
    #Args
    if args[0] == "-c" or args[0] == "--command":
        try:
            largs = " ".join(args[1:])
        except:
            print("Incorrect use. Please run BasicUtilities -c <command>")
        else:
            interpret(largs)
            sys.exit()
    if os.path.isfile(args[0]):
        with open(args[0]) as f:
            d = f.read().splitlines()
        #print(d)
        d = [dx for dx in d if dx[0] != "#" and dx.replace(" ","") != ""]
        if d[0] == "!breakonerror":
            bone = True
        else:
            bone = False
        lcount = 0
        if bone:
            d = d[1:]
        for dline in d:
            lcount += 1
            lx = interpret(dline)
            if lx != 0:
                print(f"ERROR: Line {lcount} of {args[0]} failed with exit code {lx}")
                sys.exit(-1)
        sys.exit()

logging.info("Startup finished")

while True:
    cwd = os.getcwd()
    cmd = input(cwd+">")
    interpret(cmd)