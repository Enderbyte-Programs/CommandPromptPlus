print('Basic Utilities Patch 2.23.1')
print('Starting Up')
SYSVERSION = '2.23.1'
from tkinter import messagebox, Tk
import os
def toplevelerror(message,title='Error'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showerror(title,message)
try:
    import pyutils39
except Exception as e:
    toplevelerror('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    from pytube import YouTube
except Exception as e:
    toplevelerror('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')
try:
    import keyboard
except Exception as e:
    toplevelerror('An error occured in Basic Utilities. ERROR:\n'+str(e)+'\nSome features may work incorrectly or fail')

from traceback import format_tb
import sys
def log(stuff_to_log):
    
    f = open('log_000.log','a+')

    f.write(str('['+str(datetime.datetime.now())+'] '+stuff_to_log)+'\n')
    f.close()
   
def handle_exception(type,value,traceback):
    if issubclass(type, KeyboardInterrupt):
        pass
    else:
        try:
            log('!UNCAUGHT EXCPEION!'+'\n'+str(type)+'\n'+str(value)+'\n'+str(format_tb(traceback)[0]))
        except:
            pass
        toplevelerror('A fatal exception occured in Basic Utilities. ERROR:\n'+str(type)+'\n'+str(value)+'\n'+str(format_tb(traceback)[0]))
        
        os.system('taskkill /F /PID '+str(os.getpid())+' /T')
from tkinter import *

import tarfile

iopqwe = 0

import datetime

    

sys.excepthook = handle_exception
iopqwe = 0
try:
    import winsound
except:
   print('Your device does not support Winsound. Some features may be broken.') 
iopqwe = 0
import os
iopqwe = 0
import webbrowser
iopqwe = 0
import platform
iopqwe = 0
import random
try:
    from packaging import version
except:
    print('The update command WILL NOT WORK. ')
    haspkg = False
else:
    haspkg = True

iopqwe = 0
from time import sleep
iopqwe = 0

iopqwe = 0
try:
    from playsound import playsound
except:
    print('Your device does not support playsound. Some features may be broken')
iopqwe = 0
import turtle
iopqwe = 0
import threading
iopqwe = 0

iopqwe = 0

iopqwe = 0
reqins = False

iopqwe = 0
from tkinter import filedialog
iopqwe = 0
import shutil
iopqwe = 0
import subprocess
iopqwe = 0
if str(platform.system()) == 'Windows':
    sysslash = '\\'
    sysslash = '/'
iopqwe = 0
print(os.getcwd())
sw = False
gamees_played = 0
gamees_won = 0
pi = 3.14
hasarg = True
playedg2 = False
hasarg2 = True
iopqwe = 0
pid = os.getpid()
print(pid)
def forcekill():
    log('Program stopped with exit code 0')
    global pid
    os.system('taskkill /F /PID '+str(pid)+' /T')
def forcekillnl():
    global pid
    os.system('taskkill /F /PID '+str(pid)+' /T')
try:
    arguments = sys.argv
    openfile_dir = arguments[1]
    xxx = arguments[2]
except:
    hasarg= False

try:
    arguments = sys.argv
    fto = sys.argv[1]
except:
    hasarg2 = False

if hasarg == True and xxx == 'translate':
    iopqwe = 0
    try:
        f = open(openfile_dir,'r')
        mes = f.read()
        print('')
        print("encoded message is",len(mes),"bytes")
    except:
        Tk().wihdraw()
        messagebox.showerror('Basic utilities','we culd not open the file for you. It may have been deleted, moved, unreadable, or we lack permissions.')
    else:
        tra = mes.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
    .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
    .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
    .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
    .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
    .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
    print('')
    print('Tranlation:',tra)
    print('size:',len(tra),'bytes')
    print("Do you want to write this to a txt file?(y/n)")
    wt = input()
    if wt == 'y':
        print('What folder to save to?')
        Tk().withdraw()
        fexx = filedialog.askdirectory()
        print("What should the file name be? (no extension needed)")
        fex = input()
        fex = fex + '.txt'
        
        fex = fexx + sysslash + fex
        try:
            f = open(fex,'x')
            f.write(tra)
            f.close()
            print("written to",fex)
        except:
            try:
                f = open(fex,'w')
                f.write(tra)
                f.close()
                print("written to",fex)
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Could not write')
    print('Press enter to quit program.')
    input()
    forcekill()


elif hasarg2 == True:
    iopqwe = 0
    cwd = os.getcwd()
    fto = sys.argv[1]
    if fto == 'new':
        
        def saveas():
            global txt
            global fname
            global prevsavedata
            global issy
            global menu1
            try:
                files = [('All Files','*.*')]
                file = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
            except:
                Tk().withdraw()
                messagebox.showerror('Could not write')
            else:
                try:
                    fname = file.name
                except:
                    q = 0
                else:
                    try:
                        file = open(fname,'w')
                        file.write(txt.get('1.0','end-1c'))
                        file.close()
                    except:
                        Tk().withdraw()
                        messagebox.showerror('notpad','Cannot Write data')
                    else:
                        root.title('Notpad-'+fname)
                        Tk().withdraw()
                        issy = True
                        menu1['menu'].entryconfigure(8,state='normal')
                        messagebox.showinfo('notpad','Writing sucessfull')
                        prevsavedata = txt.get('1.0','end-1c')
        def save():
            global txt
            global fname
            global prevsavedata
            
            try:
                file = open(fname,'w')
            except:
                saveas()
            else:
                file.write(txt.get('1.0','end-1c'))
                file.close()
                prevsavedata = txt.get('1.0','end-1c')

        def opennew():
            
            if os.path.isfile('BasicUtilities.exe'):
                Tk().withdraw()
                x = filedialog.askopenfilename()
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    
                CREATE_NEW_PROCESS_GROUP = 0x00000200
                DETACHED_PROCESS = 0x00000008
                
                p = subprocess.Popen(["BasicUtilities.exe", x],stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False,creationflags=subprocess.CREATE_NO_WINDOW | DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
            else:
                Tk().withdraw()
                messagebox.showerror('Notpad','Could not find BasicUtilities.exe. Did you delete or rename it?')

        def ats():
            global txt
            
            txt.insert(END,' '+str(datetime.datetime.now()))

        def canaconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('color','colour')
            data = data.replace('Color','Colour')
            data = data.replace('harbor','harbour')
            data = data.replace('Harbor','Harbour')
            data = data.replace('center','centre')
            data = data.replace('Center','Centre')
            data = data.replace('Armor','Armour')
            data = data.replace('armor','armour')
            data = data.replace('restroom','washroom')
            data = data.replace('Restroom','Washroom')
            txt.insert(END,data)

        def txconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('you','u')
            data = data.replace('You','u')
            data = data.replace('YOU','u')
            data = data.replace('are','r')
            data = data.replace('Are','r')
            data = data.replace('ARE','r')
            data = data.replace('skate','sk8')
            data = data.replace('Skate','sk8')
            data = data.replace('your','ur')
            data = data.replace('Your','ur')
            data = data.replace('YOUR','UR')
            data = data.replace('I','i')
            data = data.replace('i know right','ikr')
            data = data.replace('i know, right','ikr')
            data = data.replace('i Know Right','ikr')
            data = data.replace('i Know, Right','ikr')
            data = data.replace('in real life','irl')
            data = data.replace('in Real Life','irl')
            data = data.replace('laugh','lol')
            data = data.replace('Laugh','lol')
            txt.insert(END,data)

        def amconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('all of you',"y'all")
            data = data.replace('All of you',"Y'all")
            data = data.replace('you all',"y'all")
            data = data.replace('You all',"Y'all")
            data = data.replace('yes',"yes'm")
            data = data.replace('Yes',"Yes'm")
            data = data.replace('ng',"n'")
            data = data.replace('NG',"N'")
            data = data.replace('er than',"er than "+str(random.randint(1,20))+' '+random.choice(['pigs','cows','chickens','computers','dogs','cats','pythons'])+' in a '+random.choice(['pigpen','farm','doghouse','chicken coop','Root directory']))
            txt.insert(END,data)

        def owoconv():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            #Why did I make this????
            #WHY!?!?!?!?!?!
            data = data.replace('w','w-w')
            data = data.replace('W','w-w')
            data = data.replace('d','d-d')
            data = data.replace('D','d-d')
            data = data.replace('.','~')
            data = data.replace('dog','doggo')
            data = data.replace('pl','pw')
            data = data.replace('Pl','Pw')
            data = data.replace('r','w')
            data = data.replace('R','W')
            data = data.replace('l','w')
            data = data.replace('L','W')
            txt.insert(END,data)

        def terminat():
            global txt
            global prevsavedata
            global pid
            global istr
            data = txt.get('1.0','end-1c')
            if data == prevsavedata:
                istr = False
                forcekillnl()
            else:
                Tk().withdraw()
                x = messagebox.askyesnocancel('Text Editor','You have unsaved work. Do you want to save before closing?')
                if x == True:
                    if prevsavedata == '':
                        saveas()
                        if prevsavedata == '':
                            pass
                        else:
                            forcekillnl()
                    else:
                        save()
                        forcekillnl()
                elif x == False:
                    
                    forcekill()

        
        def scanautosave():
            try:
                global chkc
            except:
                pass
            global istr
            global issy
            while True:
                sleep(10)
                try:
                    if int(chkc.get()) == 1 and issy == True:
                        save()
                        
                except:
                    pass
                if istr == False:
                    break
        def encd():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
            .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
            .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
            .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
            .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
            .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')
            txt.insert(END,data)

        def dcd():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            data = data.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
            .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
            .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
            .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
            .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
            .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
            txt.insert(END,data)
        
        def dai():
            global ent
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            todel = ent.get()
            data = data.replace(todel,'')
            txt.insert(END,data)
        def dfw():
            global ent
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            todel = ' '+ent.get()+' '
            data = data.replace(todel,'')
            txt.insert(END,data)
        def repw():
            global ent
            global ent2
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete("1.0","end")
            
            data = data.replace(ent.get(),ent2.get())
            txt.insert(END,data)

        def cio():
            global ent3
            global txt
            data = txt.get('1.0','end-1c')
            messagebox.showinfo('Text Editor','Instances of '+str(ent3.get())+': '+str(data.count(ent3.get()))+' ('+(str(data.count(ent3.get())/(len(data)+1)*100)+'%)'))

        def writestat():
            try:
                global fname
                global txt
                data = txt.get('1.0','end-1c')
                file = open(fname+'stat','w+')
                file.write('Data for file '+fname+'\n')
                file.write('At '+str(datetime.datetime.now())+'\n')
                file.write('File Length: '+str(len(data))+' bytes\n')
                file.write('File size: '+str(os.path.getsize(fname))+' bytes\n')
                file.write('Instances of A: '+str((data.count('a')+data.count('A')))+' '+str((data.count('a')+data.count('A'))/len(data)*100)+'%\n')
                file.write('Instances of b: '+str((data.count('b')+data.count('B')))+' '+str((data.count('b')+data.count('B'))/len(data)*100)+'%\n')
                file.write('Instances of c: '+str((data.count('c')+data.count('C')))+' '+str((data.count('c')+data.count('C'))/len(data)*100)+'%\n')
                file.write('Instances of d: '+str((data.count('d')+data.count('D')))+' '+str((data.count('d')+data.count('D'))/len(data)*100)+'%\n')
                file.write('Instances of e: '+str((data.count('e')+data.count('E')))+' '+str((data.count('e')+data.count('E'))/len(data)*100)+'%\n')
                file.write('Instances of f: '+str((data.count('f')+data.count('F')))+' '+str((data.count('f')+data.count('F'))/len(data)*100)+'%\n')
                file.write('Instances of g: '+str((data.count('g')+data.count('G')))+' '+str((data.count('g')+data.count('G'))/len(data)*100)+'%\n')
                file.write('Instances of h: '+str((data.count('h')+data.count('H')))+' '+str((data.count('h')+data.count('H'))/len(data)*100)+'%\n')
                file.write('Instances of i: '+str((data.count('i')+data.count('I')))+' '+str((data.count('i')+data.count('I'))/len(data)*100)+'%\n')
                file.write('Instances of j: '+str((data.count('j')+data.count('J')))+' '+str((data.count('j')+data.count('J'))/len(data)*100)+'%\n')
                file.write('Instances of k: '+str((data.count('k')+data.count('K')))+' '+str((data.count('k')+data.count('K'))/len(data)*100)+'%\n')
                file.write('Instances of l: '+str((data.count('l')+data.count('L')))+' '+str((data.count('l')+data.count('L'))/len(data)*100)+'%\n')
                file.write('Instances of m: '+str((data.count('m')+data.count('M')))+' '+str((data.count('m')+data.count('M'))/len(data)*100)+'%\n')
                file.write('Instances of n: '+str((data.count('n')+data.count('N')))+' '+str((data.count('n')+data.count('N'))/len(data)*100)+'%\n')
                file.write('Instances of o: '+str((data.count('o')+data.count('O')))+' '+str((data.count('o')+data.count('O'))/len(data)*100)+'%\n')
                file.write('Instances of p: '+str((data.count('p')+data.count('P')))+' '+str((data.count('p')+data.count('P'))/len(data)*100)+'%\n')
                file.write('Instances of q: '+str((data.count('q')+data.count('Q')))+' '+str((data.count('q')+data.count('Q'))/len(data)*100)+'%\n')
                file.write('Instances of r: '+str((data.count('r')+data.count('R')))+' '+str((data.count('r')+data.count('R'))/len(data)*100)+'%\n')
                file.write('Instances of s: '+str((data.count('s')+data.count('S')))+' '+str((data.count('s')+data.count('S'))/len(data)*100)+'%\n')
                file.write('Instances of t: '+str((data.count('t')+data.count('T')))+' '+str((data.count('t')+data.count('T'))/len(data)*100)+'%\n')
                file.write('Instances of u: '+str((data.count('u')+data.count('U')))+' '+str((data.count('u')+data.count('U'))/len(data)*100)+'%\n')
                file.write('Instances of v: '+str((data.count('v')+data.count('V')))+' '+str((data.count('v')+data.count('V'))/len(data)*100)+'%\n')
                file.write('Instances of w: '+str((data.count('w')+data.count('W')))+' '+str((data.count('w')+data.count('W'))/len(data)*100)+'%\n')
                file.write('Instances of x: '+str((data.count('x')+data.count('X')))+' '+str((data.count('x')+data.count('X'))/len(data)*100)+'%\n')
                file.write('Instances of y: '+str((data.count('y')+data.count('Y')))+' '+str((data.count('y')+data.count('Y'))/len(data)*100)+'%\n')
                file.write('Instances of z: '+str((data.count('z')+data.count('Z')))+' '+str((data.count('z')+data.count('Z'))/len(data)*100)+'%\n')
                file.write('Instances of NUM: '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9')))+' '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9'))/len(data)*100)+'%\n')
                file.write('Instances of SPACE: '+str(data.count(' '))+' '+str(data.count(' ')/len(data)*100)+'%\n')
                file.write('Instances of SYM: '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.')))+' '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.'))/len(data)*100)+'%\n')
                
                
                file.close()
            except:
                try:
                    file.close()
                except:
                    pass
                Tk().withdraw()
                messagebox.showerror('Text Editor','Failed to write statistics file')
            else:
                Tk().withdraw()
                messagebox.showinfo('Text Editor','Wrote Statistics file to '+fname+'stat')

        def reverse():
            global txt
            data = txt.get('1.0','end-1c')
            txt.delete('1.0',"end")
            datalen = len(data)
            data = data[datalen::-1]
            txt.insert(END,data)
                
        

        prevsavedata = ''
        istr = True
        issy = False
        keyboard.add_hotkey('ctrl+q',terminat)
        keyboard.add_hotkey('ctrl+shift+s',saveas)
        keyboard.add_hotkey('ctrl+s',save)
        keyboard.add_hotkey('ctrl+alt+o',opennew)
        scaus = threading.Thread(target=scanautosave)
        scaus.start()
        root = Tk()
        root.title('Notpad [new file]')
        root.state('zoomed')
        def chk_menu1(val):
            global OptionVar0
            OptionVar0.set('File Options')
            if val == 'Exit (ctrl+q)':
                terminat()
            elif val == 'Save As (ctrl+shift+s)':
                saveas()
            elif val == 'Save (ctrl+s)':
                save()
            elif val == 'Open (ctrl+alt+o)':
                opennew()
            
        
        scr = Scrollbar(root)
        scr.pack(side='right',fill='y',expand=False)

        OptionVar0 = StringVar(root)
        OptionVar0.set('File Options')
        menu = OptionMenu(root,OptionVar0,"Exit (ctrl+q)","Save As (ctrl+shift+s)","Save (ctrl+s)","Open (ctrl+alt+o)","All key shortcuts used WILL AFFECT TO ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",command=chk_menu1)
        menu.pack(side=TOP,anchor=NW)
        menu['menu'].entryconfigure(4,state='disabled')
        def chk_menu2(val):
            global OptionVar1
            OptionVar1.set('Text Options')
            if val == 'Append Time Stamp (alt+s)':
                ats()
            elif val == 'Reverse (ctrl+alt+r)':
                reverse()
            elif val == 'Convert to Canadian English (alt+c)':
                canaconv()
            elif val == 'Convert to Text Slang (alt+t)':
                txconv()
            elif val == 'Convert to American English (alt+a)':
                amconv()
            elif val == 'Convert to Owo Text (alt+o)':
                owoconv()
            elif val == 'Encode (alt+e)':
                encd()
            elif val == 'Decode (alt+d)':
                dcd()
            elif val == 'Write Statistics File (ctrl+alt+w)':
                writestat()

        keyboard.add_hotkey('alt+s',ats)
        keyboard.add_hotkey('ctrl+alt+r',reverse)
        keyboard.add_hotkey('alt+c',canaconv)
        keyboard.add_hotkey('alt+t',txconv)
        keyboard.add_hotkey('alt+a',amconv)
        keyboard.add_hotkey('alt+o',owoconv)
        keyboard.add_hotkey('alt+e',encd)
        keyboard.add_hotkey('alt+d',dcd)
        keyboard.add_hotkey('ctrl+alt+w',writestat)
        
        OptionVar1 = StringVar(root)
        OptionVar1.set('Text Options')

        menu1 = OptionMenu(root,OptionVar1,"Append Time Stamp (alt+s)","Reverse (ctrl+alt+r)",'Convert to Canadian English (alt+c)','Convert to Text Slang(alt+t)',
        "Convert to American English (alt+a)",
        "Convert to Owo Text (alt+o)",
        "Encode (alt+e)",
        "Decode (alt+d)",
        "Write Statistics File (ctrl+alt+w)",
        "All key shortcuts used WILL AFFECT ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",
        command=chk_menu2)
        menu1['menu'].entryconfigure(8,state='disabled')
        menu1['menu'].entryconfigure(9,state='disabled')
        menu1.pack(side=TOP,anchor=NW)

        txt = Text(root,wrap=NONE)
        txt.pack(expand=True,fill='both')

       
        chkc = IntVar(root)
        chkbx = Checkbutton(root,text='Autosave (10 s)',variable=chkc)
        chkbx.place(x=390,y=30)
        
        txt.config(yscrollcommand=scr.set)
        scr.config(command=txt.yview)
        scr1 = Scrollbar(root,orient='horizontal')
        scr1.pack(side='bottom',fill='x',expand=False)
        txt.config(xscrollcommand=scr1.set)
        scr1.config(command=txt.xview)
        lbl = Label(root,text='Regular save will save to the directory in the title.')
        lbl.place(x=120,y=30)
        ent = Entry(root,width=20)
        ent.place(x=120,y=0)
        btn11 = Button(root,text='Delete all instances',command=dai,bg='skyblue')
        btn11.place(x=250,y=0)
        btn12 = Button(root,text='Delete full words only',command=dfw,bg='blue',fg='white')
        btn12.place(x=360,y=0)
        btn13 = Button(root,text='Replace with',bg='black',fg='white',command=repw)
        ent2 = Entry(root,width=20)
        btn13.place(x=500,y=0)
        ent2.place(x=600,y=0)
        ent3 = Entry(root,width=10)
        ent3.place(x=510,y=30)
        btn14 = Button(root,text='Count instances of',command=cio)
        btn14.place(x=580,y=30)
        
        
        root.mainloop()
        istr = False
        forcekillnl()
    else:
        try:
            f = open(fto)
        except:
            Tk().withdraw()
            messagebox.showerror('notpad','Could not open file. May not exist, access denied, or unreadable.')
        else:
            def saveas():
                global txt
                global fname
                global prevsavedata
                try:
                    files = [('All Files','*.*')]
                    file = filedialog.asksaveasfile(filetypes=files,defaultextension=files)
                except:
                    Tk().withdraw()
                    messagebox.showerror('Could not write')
                else:
                    try:
                        fname = file.name
                    except:
                        q = 0
                    else:
                        try:
                            file = open(fname,'w')
                            file.write(txt.get('1.0','end-1c'))
                            file.close()
                        except:
                            Tk().withdraw()
                            messagebox.showerror('notpad','Cannot Write data')
                        else:
                            
                            Tk().withdraw()
                            messagebox.showinfo('notpad','Writing sucessfull')
                            prevsavedata = txt.get('1.0','end-1c')

            def save():
                global txt
                global fto
                global prevsavedata
                try:
                    file = open(fto,'w')
                except:
                    saveas()
                else:
                    file.write(txt.get('1.0','end-1c'))
                    file.close()
                    prevsavedata = txt.get('1.0','end-1c')

            def ats():
                global txt
            
                txt.insert(END,' '+str(datetime.datetime.now()))

            def canaconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('color','colour')
                data = data.replace('Color','Colour')
                data = data.replace('harbor','harbour')
                data = data.replace('Harbor','Harbour')
                data = data.replace('center','centre')
                data = data.replace('Center','Centre')
                data = data.replace('Armor','Armour')
                data = data.replace('armor','armour')
                data = data.replace('restroom','washroom')
                data = data.replace('Restroom','Washroom')
                txt.insert(END,data)

            def txconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('you','u')
                data = data.replace('You','u')
                data = data.replace('YOU','u')
                data = data.replace('are','r')
                data = data.replace('Are','r')
                data = data.replace('ARE','r')
                data = data.replace('skate','sk8')
                data = data.replace('Skate','sk8')
                data = data.replace('your','ur')
                data = data.replace('Your','ur')
                data = data.replace('YOUR','UR')
                data = data.replace('I','i')
                data = data.replace('i know right','ikr')
                data = data.replace('i know, right','ikr')
                data = data.replace('i Know Right','ikr')
                data = data.replace('i Know, Right','ikr')
                data = data.replace('in real life','irl')
                data = data.replace('in Real Life','irl')
                data = data.replace('laugh','lol')
                data = data.replace('Laugh','lol')
                txt.insert(END,data)

            def amconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('all of you',"y'all")
                data = data.replace('All of you',"Y'all")
                data = data.replace('you all',"y'all")
                data = data.replace('You all',"Y'all")
                data = data.replace('yes',"yes'm")
                data = data.replace('Yes',"Yes'm")
                data = data.replace('er than',"er than "+str(random.randint(1,20))+' '+random.choice(['pigs','cows','chickens','computers','dogs','cats','pythons'])+' in a '+random.choice(['pigpen','farm','doghouse','chicken coop','Root directory']))
                txt.insert(END,data)

            def owoconv():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                #Why did I make this????
                #WHY!?!?!?!?!?!
                data = data.replace('w','w-w')
                data = data.replace('W','w-w')
                data = data.replace('d','d-d')
                data = data.replace('D','d-d')
                data = data.replace('.','~')
                data = data.replace('dog','doggo')
                data = data.replace('pl','pw')
                data = data.replace('Pl','Pw')
                data = data.replace('r','w')
                data = data.replace('R','W')
                data = data.replace('l','w')
                data = data.replace('L','W')
                txt.insert(END,data)

            def terminat():
                global txt
                global prevsavedata
                data = txt.get('1.0','end-1c')
                if data == prevsavedata:
                    forcekillnl()
                else:
                    Tk().withdraw()
                    x = messagebox.askyesnocancel('Text Editor','You have unsaved work. Do you want to save before closing?')
                    if x == True:
                        save()
                        forcekillnl()
                    elif x == False:
                        forcekillnl()

            def scanautosave():
                try:
                    global chkc
                except:
                    pass
                global istr
                global issy
                while True:
                    sleep(10)
                    try:
                        if int(chkc.get()) == 1 and issy == True:
                            save()
                            
                    except:
                        pass
                    if istr == False:
                        break
            def encd():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
                .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
                .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
                .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
                .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
                .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')
                txt.insert(END,data)

            def dcd():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                data = data.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
                .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
                .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
                .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
                .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
                .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
                txt.insert(END,data)

            def dai():
                global ent
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                todel = ent.get()
                data = data.replace(todel,'')
                txt.insert(END,data)
            def dfw():
                global ent
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                todel = ' '+ent.get()+' '
                data = data.replace(todel,'')
                txt.insert(END,data)
            def repw():
                global ent
                global ent2
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete("1.0","end")
                
                data = data.replace(ent.get(),ent2.get())
                txt.insert(END,data)

            def cio():
                global ent3
                global txt
                data = txt.get('1.0','end-1c')
                messagebox.showinfo('Text Editor','Instances of '+str(ent3.get())+': '+str(data.count(ent3.get()))+' ('+(str(data.count(ent3.get())/len(data)*100)+'%)'))

            def writestat():
                try:
                    global fto
                    global txt
                    data = txt.get('1.0','end-1c')
                    file = open(fto+'stat','w+')
                    file.write('Data for file '+fto+'\n')
                    file.write('At '+str(datetime.datetime.now())+'\n')
                    file.write('File Length: '+str(len(data))+' bytes\n')
                    file.write('File size: '+str(os.path.getsize(fto))+' bytes\n')
                    file.write('Instances of A: '+str((data.count('a')+data.count('A')))+' '+str((data.count('a')+data.count('A'))/len(data)*100)+'%\n')
                    file.write('Instances of b: '+str((data.count('b')+data.count('B')))+' '+str((data.count('b')+data.count('B'))/len(data)*100)+'%\n')
                    file.write('Instances of c: '+str((data.count('c')+data.count('C')))+' '+str((data.count('c')+data.count('C'))/len(data)*100)+'%\n')
                    file.write('Instances of d: '+str((data.count('d')+data.count('D')))+' '+str((data.count('d')+data.count('D'))/len(data)*100)+'%\n')
                    file.write('Instances of e: '+str((data.count('e')+data.count('E')))+' '+str((data.count('e')+data.count('E'))/len(data)*100)+'%\n')
                    file.write('Instances of f: '+str((data.count('f')+data.count('F')))+' '+str((data.count('f')+data.count('F'))/len(data)*100)+'%\n')
                    file.write('Instances of g: '+str((data.count('g')+data.count('G')))+' '+str((data.count('g')+data.count('G'))/len(data)*100)+'%\n')
                    file.write('Instances of h: '+str((data.count('h')+data.count('H')))+' '+str((data.count('h')+data.count('H'))/len(data)*100)+'%\n')
                    file.write('Instances of i: '+str((data.count('i')+data.count('I')))+' '+str((data.count('i')+data.count('I'))/len(data)*100)+'%\n')
                    file.write('Instances of j: '+str((data.count('j')+data.count('J')))+' '+str((data.count('j')+data.count('J'))/len(data)*100)+'%\n')
                    file.write('Instances of k: '+str((data.count('k')+data.count('K')))+' '+str((data.count('k')+data.count('K'))/len(data)*100)+'%\n')
                    file.write('Instances of l: '+str((data.count('l')+data.count('L')))+' '+str((data.count('l')+data.count('L'))/len(data)*100)+'%\n')
                    file.write('Instances of m: '+str((data.count('m')+data.count('M')))+' '+str((data.count('m')+data.count('M'))/len(data)*100)+'%\n')
                    file.write('Instances of n: '+str((data.count('n')+data.count('N')))+' '+str((data.count('n')+data.count('N'))/len(data)*100)+'%\n')
                    file.write('Instances of o: '+str((data.count('o')+data.count('O')))+' '+str((data.count('o')+data.count('O'))/len(data)*100)+'%\n')
                    file.write('Instances of p: '+str((data.count('p')+data.count('P')))+' '+str((data.count('p')+data.count('P'))/len(data)*100)+'%\n')
                    file.write('Instances of q: '+str((data.count('q')+data.count('Q')))+' '+str((data.count('q')+data.count('Q'))/len(data)*100)+'%\n')
                    file.write('Instances of r: '+str((data.count('r')+data.count('R')))+' '+str((data.count('r')+data.count('R'))/len(data)*100)+'%\n')
                    file.write('Instances of s: '+str((data.count('s')+data.count('S')))+' '+str((data.count('s')+data.count('S'))/len(data)*100)+'%\n')
                    file.write('Instances of t: '+str((data.count('t')+data.count('T')))+' '+str((data.count('t')+data.count('T'))/len(data)*100)+'%\n')
                    file.write('Instances of u: '+str((data.count('u')+data.count('U')))+' '+str((data.count('u')+data.count('U'))/len(data)*100)+'%\n')
                    file.write('Instances of v: '+str((data.count('v')+data.count('V')))+' '+str((data.count('v')+data.count('V'))/len(data)*100)+'%\n')
                    file.write('Instances of w: '+str((data.count('w')+data.count('W')))+' '+str((data.count('w')+data.count('W'))/len(data)*100)+'%\n')
                    file.write('Instances of x: '+str((data.count('x')+data.count('X')))+' '+str((data.count('x')+data.count('X'))/len(data)*100)+'%\n')
                    file.write('Instances of y: '+str((data.count('y')+data.count('Y')))+' '+str((data.count('y')+data.count('Y'))/len(data)*100)+'%\n')
                    file.write('Instances of z: '+str((data.count('z')+data.count('Z')))+' '+str((data.count('z')+data.count('Z'))/len(data)*100)+'%\n')
                    file.write('Instances of NUM: '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9')))+' '+str((data.count('0')+data.count('1')+data.count('2')+data.count('3')+data.count('4')+data.count('5')+data.count('6')+data.count('7')+data.count('8')+data.count('9'))/len(data)*100)+'%\n')
                    file.write('Instances of SPACE: '+str(data.count(' '))+' '+str(data.count(' ')/len(data)*100)+'%\n')
                    file.write('Instances of SYM: '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.')))+' '+str((data.count('!')+data.count('@')+data.count('#')+data.count('$')+data.count('%')+data.count('^')+data.count('&')+data.count('*')+data.count('(')+data.count(')')+data.count('-')+data.count('_')+data.count('/')+data.count(';')+data.count(',')+data.count('.'))/len(data)*100)+'%\n')
                    
                    
                    file.close()
                except:
                    try:
                        file.close()
                    except:
                        pass
                    Tk().withdraw()
                    messagebox.showerror('Text Editor','Failed to write statistics file')
                else:
                    Tk().withdraw()
                    messagebox.showinfo('Text Editor','Wrote Statistics file to '+fto+'stat')
            def reverse():
                global txt
                data = txt.get('1.0','end-1c')
                txt.delete('1.0',"end")
                datalen = len(data)
                data = data[datalen::-1]
                txt.insert(END,data)
            try:
                prevsavedata = f.read()
            except:
                Tk().withdraw()
                messagebox.showerror('Text Editor','Could not read file')
                forcekillnl()

            istr = True
            issy = True
            keyboard.add_hotkey('ctrl+q',terminat)
            keyboard.add_hotkey('ctrl+shift+s',saveas)
            keyboard.add_hotkey('ctrl+s',save)
            
            scaus = threading.Thread(target=scanautosave)
            scaus.start()
            root = Tk()
            root.title('Notpad [new file]')
            root.state('zoomed')
            def chk_menu1(val):
                global OptionVar0
                OptionVar0.set('File Options')
                if val == 'Exit (ctrl+q)':
                    terminat()
                elif val == 'Save As (ctrl+shift+s)':
                    saveas()
                elif val == 'Save (ctrl+s)':
                    save()
                
                
            
            scr = Scrollbar(root)
            scr.pack(side='right',fill='y',expand=False)

            OptionVar0 = StringVar(root)
            OptionVar0.set('File Options')
            menu = OptionMenu(root,OptionVar0,"Exit (ctrl+q)","Save As (ctrl+shift+s)","Save (ctrl+s)","All key shortcuts used WILL AFFECT TO ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",command=chk_menu1)
            menu.pack(side=TOP,anchor=NW)
            menu['menu'].entryconfigure(3,state='disabled')

            def chk_menu2(val):
                global OptionVar1
                OptionVar1.set('Text Options')
                if val == 'Append Time Stamp (alt+s)':
                    ats()
                elif val == 'Reverse (ctrl+alt+r)':
                    reverse()
                elif val == 'Convert to Canadian English (alt+c)':
                    canaconv()
                elif val == 'Convert to Text Slang (alt+t)':
                    txconv()
                elif val == 'Convert to American English (alt+a)':
                    amconv()
                elif val == 'Convert to Owo Text (alt+o)':
                    owoconv()
                elif val == 'Encode (alt+e)':
                    encd()
                elif val == 'Decode (alt+d)':
                    dcd()
                elif val == 'Write Statistics File (ctrl+alt+w)':
                    writestat()

            keyboard.add_hotkey('alt+s',ats)
            keyboard.add_hotkey('ctrl+alt+r',reverse)
            keyboard.add_hotkey('alt+c',canaconv)
            keyboard.add_hotkey('alt+t',txconv)
            keyboard.add_hotkey('alt+a',amconv)
            keyboard.add_hotkey('alt+o',owoconv)
            keyboard.add_hotkey('alt+e',encd)
            keyboard.add_hotkey('alt+d',dcd)
            keyboard.add_hotkey('ctrl+alt+w',writestat)
            
            OptionVar1 = StringVar(root)
            OptionVar1.set('Text Options')

            menu1 = OptionMenu(root,OptionVar1,"Append Time Stamp (alt+s)","Reverse (ctrl+alt+r)",'Convert to Canadian English (alt+c)','Convert to Text Slang(alt+t)',
            "Convert to American English (alt+a)",
            "Convert to Owo Text (alt+o)",
            "Encode (alt+e)",
            "Decode (alt+d)",
            "Write Statistics File (ctrl+alt+w)",
            "All key shortcuts used WILL AFFECT ALL OTHER COPIES OF THIS PROGRAM CURRENTLY RUNNING",
            command=chk_menu2)
            
            menu1['menu'].entryconfigure(9,state='disabled')
            menu1.pack(side=TOP,anchor=NW)

            txt = Text(root,wrap=NONE)
            txt.pack(expand=True,fill='both')
            try:
                txt.insert(END,prevsavedata)
            except:
                Tk().withdraw()
                messagebox.showerror('Notpad','Could not read file')
                forcekillnl()

        
            chkc = IntVar(root)
            chkbx = Checkbutton(root,text='Autosave (10 s)',variable=chkc)
            chkbx.place(x=390,y=30)
            
            txt.config(yscrollcommand=scr.set)
            scr.config(command=txt.yview)
            scr1 = Scrollbar(root,orient='horizontal')
            scr1.pack(side='bottom',fill='x',expand=False)
            txt.config(xscrollcommand=scr1.set)
            scr1.config(command=txt.xview)
            lbl = Label(root,text='Regular save will save to the directory in the title.')
            lbl.place(x=120,y=30)
            ent = Entry(root,width=20)
            ent.place(x=120,y=0)
            btn11 = Button(root,text='Delete all instances',command=dai,bg='skyblue')
            btn11.place(x=250,y=0)
            btn12 = Button(root,text='Delete full words only',command=dfw,bg='blue',fg='white')
            btn12.place(x=360,y=0)
            btn13 = Button(root,text='Replace with',bg='black',fg='white',command=repw)
            ent2 = Entry(root,width=20)
            btn13.place(x=500,y=0)
            ent2.place(x=600,y=0)
            ent3 = Entry(root,width=10)
            ent3.place(x=510,y=30)
            btn14 = Button(root,text='Count instances of',command=cio)
            btn14.place(x=580,y=30)
            
            root.mainloop()
            try:
                f.close()
                
            except:
                ool = []
            istr = False
            forcekillnl()
      
log('program started')
try:
    from requests import get
except:
    print('Some features may be broken because you dont have requests installed.')
else:
    try:
        SYSVERDATA = get('https://pastebin.com/raw/htCBGFXf').text
        reqins = True
    except:
        Tk().withdraw()
        messagebox.showerror('Error','Some features may work improperly or fail because you are not connected to the internet. (ip, ip6, update)')
xae = True
tcrash = False
accessdenied = False
cmd_run = 0
iopqwe = 0
try:
    f = open("appdata.txt","r")
    besttime = f.read()
    try:
        besttime = int(besttime)
    except:
        a_file = open("appdata.txt", "r")

        list_of_lines = a_file.readlines()

        list_of_lines[0] = "0\n"

        besttime = 0
        a_file = open("appdata.txt", "w")

        a_file.writelines(list_of_lines)

        a_file.close()
except:
    try:
        f = open("appdata.txt","x")
        f.write("0")
        besttime = 0
        f.close()
    except:
        accessdenied = True
finally:
    f.close()
iopqwe = 0
try:
    f = open('bcount.txt')
    bootcount = f.read()
    try:
        bootcount = int(bootcount)
    except:
        f.close
        f = open('bcount.txt','w')
        bootcount = 0
        f.write(str(bootcount+1))
        f.close()
except:
    f = open('bcount.txt','x')
    bootcount = 0
    f.write(str(bootcount+1))
    f.close()
bootcount += 1
try:
    f = open('bcount.txt','w')
    f.write(str(bootcount))
    f.close()
except:
    f = open('bcount.txt','x')
    f.write(str(bootcount))
    f.close()
iopqwe = 0
def error(erc):
    erc = str(erc)
    erm = "An error has occured. Error code "
    erm = erm + erc
    Tk().withdraw()
    messagebox.showerror("Error",erm)
iopqwe = 0
iopqwe = 0
def newwindow():

    x = pyutils39.toplevelquestion('Do you want to open a new window of Basic Utilities before you run this long/infinite command?')
    if x == True:
        try:
            os.startfile('BasicUtilities.exe')
        except:
            pyutils39.error('Could not find BasicUtilities.exe. Did you rename it?')
iopqwe = 0
def conv(start,end,formula):
    global txt
    global lbl2
    def convert():
        
        res = txt.get()
        try:
            res = float(res)
        except:
            lbl2.configure(text='error')
        else:
            c = str(res)+formula
            c = float(eval(c))
            lbl2.configure(text=c)
    window = Tk()
    def die():
        window.destroy()
        window.quit()
    window.title('Converter')
    lbl = Label(window,text='please input the amount of '+start+' and press convert.')
    lbl.grid(column=0,row=0)
    lbl1 = Label(window,text='Converting to '+end)
    lbl1.grid(column=1,row=0)
    txt = Entry(window,width=20)
    txt.grid(column=0,row=1)
    btn = Button(window,text='Convert',command=convert,bg='lime green')
    btn.grid(column=1,row=1)
    lbl2 = Label(window,text='')
    lbl2.grid(column=0,row=2)
    btn1 = Button(window,text='close',command=die,bg='yellow')
    btn1.grid(column=1,row=2)
    window.mainloop()

iopqwe = 0

def reload():
    try:
        os.startfile("BasicUtilities.exe")
    except:
        print("Could not start Basic Utilities")
    else:
        sys.exit()
iopqwe = 0

def startsound():
    if os.path.isfile('startsound.dat') == True:
        try:
            f = open('startsound.dat')
            data = f.read()
        except:
            print('Startsound file could not be read. Will delete')
            try:
                f.close()
            except:
                pass
            os.remove('startsound.dat')
        else:
            f.close()
            if os.path.isfile(data):
                playsound(data)
    else:
        print('You currently do not have a startup sound set. Set one via the startsound command')
ss_po = threading.Thread(target=startsound)
ss_po.start()
iopqwe = 0       
def runfile(filename):
    try:
        os.startfile(filename)
    except:
        error(2)

iopqwe = 0

try:
    f = open('username.txt','r')
except:
    try:
        f = open('username.txt','x')
    except:
        try:
            f = open('username.txt','w')
        except:
            print('Access Denied')
        else:
            f.write('DefaultUser')
            f.close()
            sysuser = 'DefaultUser'
    else:
        f.write('DefaultUser')
        f.close()
        sysuser = 'DefaultUser'
else:
    sysuser = str(f.read())
    f.close()
iopqwe = 0
try:
    f = open('bday.txt','r')
    x = f.readlines()
    mt = x[0]
    dy = x[1]
except:
    print('')
else:
    t = datetime.datetime.now()
    p = t.month
    o = t.day
    try:
        mt = int(mt)
        dy = int(dy)
    except:
        print('Warning: Bday file cannot be converted to type <int>.',end='\r')
    else:
        try:
            l = datetime.datetime(2021,mt,dy,0,0,0)
        except:
            print('Warning: Bday out of range',end='\r')
        else:
            if mt == p and dy ==o:
                print("Happy birthday to you!")
                print("Happy birthday to you!")
                print("Happy birthday, dear User")
                print("Happy birthday to you!")
                print("")
                print('press enter to continue to the command menu')
                input()
iopqwe = 0
t = datetime.datetime.now()
y = t.year
p = t.month
o = t.day
if p == 1 and o ==1:
    print('Happy New Year, User (gregorian calendar)')
elif y == 2022 and p == 2 and o == 1:
    print('happy Chinese New Year')
elif y == 2023 and p == 1 and o == 22:
    print('happy Chinese New Year')
elif y == 2024 and p == 2 and o == 10:
    print('happy Chinese New Year')
elif y == 2025 and p == 1 and o == 29:
    print('happy Chinese New Year')
elif p == 12 and o == 25:
    print('Happy Holidays, User')
elif p == 12 and o == 24:
    print('Happy Holidays, User')
elif p == 12 and o == 26:
    print('Happy Holidays, User')
elif p == 2 and o == 15:
    print('Happy Parinirvana Day, User (If you are buddhist)')
elif p == 10 and o == 31:
    print('Happy Halloween, User!')
#Couldn't find any more fixed-date holidays that are recognized globally.


iopqwe = 0
print('You have booted up Basic Utilities',bootcount,'times.')
x = datetime.datetime.now()
if x.month == 4 and x.day == 1 and x.hour < 12:
    webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')
if x.month == 7 and x.day == 1:
    print('Happy Canada Day, User!')
if x.month == 7 and x.day == 4:
    print('Happy American Day, User( if you are american)')
try:
    f = open('btime.txt','r')
except:
    f = open('btime.txt','x')
    f.write(str(x.year)+'\n')
    f.write(str(x.month)+'\n')
    f.write(str(x.day)+'\n')
    f.write(str(x.hour)+'\n')
    f.write(str(x.minute)+'\n')
    f.write(str(x.second)+'\n')
    a = x.year
    b = x.month
    c = x.day
    d = x.hour
    e = x.minute
    g = x.second
else:
    try:
        content = f.readlines()
        a = content[0]
        b = content[1]
        c = content[2]
        d = content[3]
        e = content[4]
        g = content[5]
    except:
        f = open('btime.txt','w')
        f.write(str(x.year)+'\n')
        f.write(str(x.month)+'\n')
        f.write(str(x.day)+'\n')
        f.write(str(x.hour)+'\n')
        f.write(str(x.minute)+'\n')
        f.write(str(x.second)+'\n')
        a = x.year
        b = x.month
        c = x.day
        d = x.hour
        e = x.minute
        g = x.second
    else:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            g = int(g)
        except:
            f = open('btime.txt','w')
            f.write(str(x.year)+'\n')
            f.write(str(x.month)+'\n')
            f.write(str(x.day)+'\n')
            f.write(str(x.hour)+'\n')
            f.write(str(x.minute)+'\n')
            f.write(str(x.second)+'\n')
            a = x.year
            b = x.month
            c = x.day
            d = x.hour
            e = x.minute
            g = x.second
d0 = datetime.datetime(a,b,c,d,e,g)
d1 = datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)
diff = d1-d0
ts = diff.total_seconds()
print('You opened Basic Utilities for the first time in',ts,'seconds!')
f.close()
f = open('btime.txt','w')
f.write(str(x.year)+'\n')
f.write(str(x.month)+'\n')
f.write(str(x.day)+'\n')
f.write(str(x.hour)+'\n')
f.write(str(x.minute)+'\n')
f.write(str(x.second)+'\n')
f.close()
iopqwe = 0
iopqwe = 0
print('')
print("Welcome to Basic Utilities,",sysuser)
print(datetime.datetime.now())
x = datetime.datetime.now()
if x.hour > 0 and x.hour < 12:
    print('Good morning,',sysuser)
elif x.hour > 11 and x.hour < 18:
    print('Good afternoon,',sysuser)
elif x.hour > 17 and x.hour < 22:
    print('Good evening,',sysuser)
else:
    print('Good night,',sysuser)
nua = False
print(sysslash)
if reqins == True and haspkg:
    SYSVERNUM = version.parse(SYSVERDATA[0:6])
    SYSVERSION = version.parse("2.23.1")
    if SYSVERNUM > SYSVERSION:
        print('!New update found. Run the update command to download it!')

        log('Found new update')
        nua = True
while xae == True:
    crashed = False
    print("")
    print("-----Command Menu-----")
    print("Type your command under here and press enter")
    command = input()
    log('User executed command '+command)
    if command == "help" or command == "?":
        
        print("-----Commands List-----")
        print('-----Misc-----')
        print("help: Shows this list")
        
        print('seelog: View the log')
        
        print("draw: Draw with Turtle!")
        print("credits: View credits.")
        print("contact: Get my email and Discord")
        print("colour: Find a colour")
        print("bday: Input your birthday to get a surprise on startup when it matches")
        print("wb: Visit our website")
        print("lockdown: lockdown your screen until you enter a password")
        
        
        
        print('notifs: Change your commmand-running notification settings.')
        print('rev: Reverse the contents of a file')
        print("stat: Get some statistics of this program.")
        print('usr: change your username')
        print('startsound: Set your startup sound')
        print('')
        print("-----USELESS COMMANDS-----")
        print("insult: Get insulted")
        print("prank: try it out :P")
        print('crash: Crash this program')
       
        print('')
        print('-----System Interaction-----')
        print("stop: Stops this window")
        print("stopall: stops all BasicUtilities windows")
        print("reload: reloads this program.")
        if sysslash == '\\':
            print("logoff: Logs you out.")
            print("restart: Restarts your computer")
            print("shutdown: Shutdown your computer")
        print("browser: Open the Basic Utilities Browser.")
        print("dir: Get the directory that this program is installed to")
        print('')
        print('-----Games-----')
        print("game: Play Beat The Bank")
        print("snl: Play Snakes and Ladders [sc]")
        print("m8b: Magic 8 ball")
        print("cpg: Play the Cartesian Plane Game")
        print('game2: Play Discount Prodigy')
        
        print('')
        print('-----Preset Counters-----')
        print("meter: See how long it has been since COVID infected its first human.(VE COUNTER)")
        print("lnmeter: How long since life was normal?")
        print('progcount: How long since this program existed')
        print('')
        print('-----Clocks & Alarms-----')
        print("alarm: Open the alarm clock")
        print("clock: Tells you the exact time")
        print("counter: make a counter")
        print("sw: Stop watch!")
        print("clk: Get an ongoing clock")
        
        print("timer: Pauseable Timer")
        print('')
        print('-----Random Generators-----')
        print("rng: Random Number Generator")
        print("cf: Coin Flip")
        print('hex: Random Hexadecimal Generator (x16)')
        print('hexbi: Random hexadecabinary generator (x62)')
        print('picker: Make a custom random generator')
        print('cpicker: Random colour picker')
        print('npicker: Random Name Picker (NOT TO BE TAKEN SERIOUSLY)')#Todo 1.11 pre 1
        print('tpicker: Random Town Picker (NOT TO BE TAKEN SERIOUSLY)')#Todo 1.11 pre 1
        print('fpicker: Get a randomly generated food product name')
        print('rname: Random Ruby Name Generator')
        #Ruby is my dog and she has a lot of names
        print('art: Get some random art')
        print('')
        print('-----Utility-----')
        print("lag: Measures your computer's lag.")
        print("anim: Get a little animation of a wheel.")
        print("pyterm: Open a python terminal prompt [potentially dangerous]")
        print("randpass: Get a random password.")
        print("erc: List of error codes")
        print("encode: encode stuff so no one can read it")
        print("translate: Translate files back to readable") 
        print('ping: Ping an IP address')
        print('ip: Get your IPv4 address')
        print('permaping: Ping an IP address indefinitely')
        print('fstat: Read a file and get an statistics report on it in the form of *.*.fstat')
        print('cmd: Execute something on the Command Prompt')
        print('musplay: Play an audio file in the background')
        print('sysplat: Get your system platform, version, etc.')
        print('sysmem: Get some system memory statistics')
        print('folmem: Get memory statistics about a folder. [Warning for big folders]')
        print('filemem: Ge memory statistics about a file')
        print('bumem: Get a statistic about how much of YOUR memory WE are using!')
        print('tsklst: List all task running on the system')
        print('ip6: Get your Ipv6 address')
        print('update: check for updates')
        print('scanall: Get a list of all files in a directory')
        print('tar: Make tar.gz archive')
        print('untar: Uncompress a tar.gz archive')
        print('search: Search folders for files that contain things you input. Warning: Can take up lots of resources!')
        print('speed: How many equations can your computer do in 1 second?')
        if sysslash == '\\':
            print('diran: Get directory statistics and write to file')
            print('te: Open the Text Editor that comes with this program.')
        
        
        print('')
        print('-----Calculators & Converters-----')
        print("apv: area, perimeter, and volume calculator [sc]")
        print('tempt: Temperature converter')
        print('degp: degrees to percent')
        print('pdeg: percent to degrees')
        print('pi: Get up to 100 digits of pi')
     
        print("pa: Add percent")
        print("pr: Remove percent")
        print("pgpa: Percent to GPA")
        print("gpap: GPA to percent")
        print("avg: Get an average calculator")
        print("calc help: Help with the calculator")
        print("calc: Calculator")
        print("quiz: get a multiplication quiz up to 12x12")
        
        print("conv len: length converters [sc]")
        print('fibb: Generate the Fibbonacci sequence <-- Spelled wrong but who cares')
        print('prime: Generate all prime numbers up to a number')
        
        print('sqrpyr: Calculate volume of a rectangular pyramid.')
        print('tripyr: Calculate volume of a triangular pyramid')
        print('emc2: Calcuate th energy(joules) in a given object.')
        print('')
        print('-----Uninstalling and cleaning-----')
        print("uninstall: Uninstall this program completely")
        print("clr: Reset Basic Utilities' AppData.")
        print("rem: Remove custom appdata")
        print('cln: Clean up files from old versions that you dont need')

        
        print('')
        #^Under development, release in 2.6 or 2.7
        if sysslash == '\\':
            print('-----Sound-----')
            print('beep: Get a beep')
            print('curse: Have this program curse at you (no actual cursing)')

            print('toneup: Make a rising Tone')
            print('rmg: Random Music Generator')
            print('cmaj: Play the ascending C major scale')
            print('alm: Get a nice beepy alarm')
        print('')
        print('-----YouTube-----')
        print('ytdownload: Download a single video from YouTube')
        print("ytaudio: Download a video's audio only")
        print('')
        print("There are also some easter egg commands :)")
        print('-----Contact and Support-----')
        print('If you need help, contact me with the contact command')

    elif command == 'ytdownload':
        print('Please input the full URL to the video of your choice and press enter')
        ytdownld = input()
        try:
            yx = YouTube(ytdownld)
            yx.check_availability()
        except:
            Tk().withdraw()
            messagebox.showerror('Error','Please input a valid video URL')
        else:
            def dlr():
                global yx
                ytw.quit()
                ytw.destroy()
                print('Preparing')
                x = yx.streams.get_lowest_resolution()
                print('Please select save file')
                files = [('mp4 video', '*.mp4')]
                Tk().withdraw()
                file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                
                print('Downloading')
                x.download(filename=str(file.name))
                print('Complete')

            def dhr():
                global yx
                ytw.quit()
                ytw.destroy()
                print('Preparing')
                x = yx.streams.get_highest_resolution()
                print('Please select save file')
                files = [('mp4 video', '*.mp4')]
                Tk().withdraw()
                file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                
                print('Downloading')
                x.download(filename=str(file.name))
                print('Complete')
                
            ytw = Tk()
            ytw.title('Options')
            lbl = Label(ytw,text='Please select your option')
            lbl.grid(column=0,row=0)
            btn = Button(ytw,text='Cancel',bg='red',command=ytw.destroy)
            btn.grid(column=0,row=1)
            btn1 = Button(ytw,text='Download lowest resolution',bg='yellow',command=dlr)
            btn1.grid(column=1,row=0)
            btn2 = Button(ytw,text='Download highest resolution',bg='lime green',command=dhr)
            btn2.grid(column=1,row=1)
            ytw.mainloop()

    elif command == 'ytaudio':
        print('Please input the full URL to the video of your choice and press enter')
        ytdownld = input()
        try:
            yx = YouTube(ytdownld)
            yx.check_availability()
        except:
            Tk().withdraw()
            messagebox.showerror('Error','Please input a valid video URL')
        else:
            

            def dhr():
                global yx
                yta.quit()
                yta.destroy()
                print('Preparing')
                x = yx.streams.get_audio_only()
                print('Please select save file')
                files = [('mp3 Audio', '*.mp3')]
                Tk().withdraw()
                file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                
                print('Downloading')
                x.download(filename=str(file.name))
                print('Complete')
                
            yta = Tk()
            yta.title('Options')
            lbl = Label(yta,text='Please select your option')
            lbl.grid(column=0,row=0)
            btn = Button(yta,text='Cancel',bg='red',command=yta.destroy)
            btn.grid(column=0,row=1)
            
            btn2 = Button(yta,text='Download',bg='lime green',command=dhr)
            btn2.grid(column=1,row=0)
            yta.mainloop()

    elif command == 'conceal':
        Tk().withdraw()
        xlmy = messagebox.askyesno('Q','WARNING! If used improperly, this command can damage your system! Are you sure you want to do this?')
        if xlmy == True:
            print('What password do you want to set? (DO NOT FORGET IT)')
            pswd = input()
            def kill_con():
                global txt
                ent = txt.get()
                global pswd
                if ent == pswd or ent == 'YOU set' or ent == 'the password YOU set':
                    con.quit()
                    con.destroy()
            def bypass_ev():
                pass
            con = Tk()
            con.attributes('-fullscreen',True)
            con.wm_attributes('-topmost',True)
            con.config(bg='blue')
            lbl = Label(con,text='This device has been locked down. Input the password YOU set and press exit to exit.',fg='white',bg='blue',font=('Arial',24))
            lbl.pack()
            txt = Entry(con,width=50)
            txt.pack()
            btn = Button(con,text='Exit',bg='lime green',command=kill_con)
            btn.pack()
            con.protocol('WM_DELETE_WINDOW',bypass_ev)
            con.mainloop()

    elif command == 'search':
        print('What to search for?')
        searchfor = input()
        print('Please choose directory')
        Tk().withdraw()

        root = filedialog.askdirectory()
        
        if os.path.isdir(root):
            for path, subdirs, files in os.walk(root):
                for name in files:
                    fin = os.path.join(path, name)
                    if searchfor.lower() in name.lower():
                        print(fin.replace('/','\\'))

    elif command == 'speed':
        has_finished_counting = False
        def count_speed():
            global has_finished_counting
            sleep(1)
            has_finished_counting = True
        counting = 0
        th = threading.Thread(target=count_speed)
        th.start()
        while not has_finished_counting:
            counting += 1
        print('Equations/second:',counting)
                    
            
    elif command == 'tar':
        try:
            f = tarfile.open('archive.tar.gz',mode='x:gz')
        except:
            f = tarfile.open('archive.tar.gz',mode='w:gz')
        print('Please choose files')
        Tk().withdraw()
        files_to_add = filedialog.askopenfilenames()
        
        
        for files in files_to_add:
            f.add(files,arcname=os.path.basename(files))
        f.close()
        print('Please select file save directory')
        Tk().withdraw()
        file_to_save = filedialog.askdirectory()
        print('What should it be called (excluding file extension)')
        file_name = input()
        try:
            os.rename('archive.tar.gz',file_name+'.tar.gz')
            file_to_copy = file_name+'.tar.gz'
            shutil.copyfile(file_to_copy,file_to_save+sysslash+file_to_copy)
            os.remove(file_to_copy)
        except:
            pyutils39.toplevelerror('Error when copying file. You can find your archive as archive.tar.gz in this program"s folder.')

    elif command == 'untar':
        print('Please select file to uncompress')
        Tk().withdraw()
        ftu = filedialog.askopenfilename()
        print('Please select output directory')
        Tk().withdraw()
        ftx = filedialog.askdirectory()

        try:
            f = tarfile.open(ftu)
            f.extractall(ftx)
            f.close()
        except:
            pyutils39.toplevelerror('Could not uncompress')

    elif command == 'scanall':
        print('Please choose directory')
        Tk().withdraw()

        root = filedialog.askdirectory()
        how_many_files = 0
        if os.path.isdir(root):
            for path, subdirs, files in os.walk(root):
                for name in files:
                    print(os.path.join(path, name).replace('/','\\'))
                    how_many_files += 1
            print('Files:',how_many_files)
            
        else:
        
            print('Invalid directory')
        

    elif command == 'update':
        if nua == True:
            
            Tk().withdraw()
            m = messagebox.askyesno('BU','A new update ('+SYSVERDATA[0:6]+') is available. Do you want to download it?')
            if m == True:
                webbrowser.open(SYSVERDATA[6:len(SYSVERDATA)])
                log('Download new update')
        else:
            Tk().withdraw()
            messagebox.showinfo('BU','No new updates are available')

    elif command == 'seelog':
        os.startfile('log_000.log')

    elif command == 'startsound':
        try:
            f = open('startsound.dat')
            data = f.read()
            f.close()
        except:
            print('You do not have a start sound')
        else:
            if os.path.isfile(data) == True:
                print('This is your current startup sound')
                playsound(data)
                
            else:
                print('startsound.dat contains invalid data.')
        print('Please select a start sound')
        Tk().withdraw()
        dlf = filedialog.askopenfilename()
        print(dlf)
        
        try:
            playsound(str(dlf))
        except:
            Tk().withdraw()
            messagebox.showerror('BU','File is unreadable')
        else:
            f = open('startsound.dat','w+')
            f.write(dlf)
            f.close()
            print('Startup sound set to',dlf)
            log('Changed startsound')

    elif command == 'te':
        
        CREATE_NEW_PROCESS_GROUP = 0x00000200
        DETACHED_PROCESS = 0x00000008
        try:
            p = subprocess.Popen(["BasicUtilities.exe", "new"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
        except:
            Tk().withdraw()
            messagebox.showerror('BU','Unable to start.')

    elif command == 'art':
        try:
            s = turtle.getscreen()
            t = turtle.Turtle()
        except:
            s = turtle.getscreen()
            t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-300,-300)
        t.pendown()
        t.goto(-300,300)
        t.goto(300,300)
        t.goto(300,-300)
        t.goto(-300,-300)
        t.penup()
        t.goto(0,0)
        t.pendown()
        colours = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4','gray60']
        for i in range(random.randint(10,200)):
            try:
                t.pencolor(random.choice(colours))
                t.pensize(random.randint(1,10))
                t.goto(random.randint(-300,300),random.randint(-300,300))
                t.right(random.randint(0,360))
                exec(random.choice(['t.dot(random.randint(1,20))','t.circle(random.randint(1,20))','print("")','print("")']))
            except:
                crashed = True
                break
        if crashed == False:
            Tk().withdraw()
            mmop = messagebox.askyesno('Art','Do you want to export this to a .eps file?')
            if mmop == True:
                
                s.getcanvas().postscript(file='art'+str(random.randint(0,999999))+'.eps')
                mmoo = messagebox.askyesno('Art','Do you want to visit the website to convert to a png?\n\
                    WARNING: USE AT OWN RISK, NO AFFILIATED WITH BU IN ANY WAY')
                if mmoo == True:
                    webbrowser.open("https://epsviewer.org/onlineviewer.aspx")
            messagebox.showinfo('BU','Done. Dismiss this messagebox when you are ready to close turtle window')
            turtle.bye()
        


    elif command == 'usr':
        print(f"Your current username is {sysuser}")
        print('Please input your new name')
        sysuser = input()
        try:
            f = open('username.txt','w')
        except:
            try:
                f = open('username.txt','x')
            except:
                print('Access denied. Your new name will only work for this session')
            else:
                f.write(sysuser)
                f.close()
                print('Sucess')
                log('Changed username')
        else:
            f.write(sysuser)
            f.close()
            print('sucess')
            log('Changed username')
    

    elif command == 'rname':
        rname = ''
        for i in range(random.randint(1,20)):
            rname += str(random.choice(['Ruby','Roo','Roobster','Doo','By','By','By','Boo','Dy','Doodle','r','oo','oo','dle','oobster']))
        rname = rname.replace('BooB','RooB')
        print(rname)

    elif command == 'clk':
        newwindow()
        isfini = False
        def cloc():
            sleep(1)
            global lbl
            global isfini
            while isfini == False:
                sleep(0.1)
                try:
                    lbl.configure(text=str(datetime.datetime.now()))
                except:
                    break
                
        def ckill():
            global isfini
            isfini = True
            clk.quit()
            clk.destroy()
            
        th = threading.Thread(target=cloc)
        th.start()
        clk = Tk()
        clk.title('Clock')
        clk.geometry('150x50')
        lbl = Label(clk,text='')
        lbl.grid(column=0,row=0)
        btn = Button(clk,text='Exit',bg='red',command=ckill)
        btn.grid(column=0,row=1)
        clk.mainloop()
        

    elif command == 'fpicker':
        print('-----')
        print(random.choice(['Nutra','nutri','health','good','fod'])+random.choice(['-o-','er','','',''])+random.choice(['loaf','fod','snak','fodder','health','food']))
        print('-----')

    elif command == 'shutdown':
        os.system("shutdown /s /t 0")

    elif command == 'tkdebug':
        
        
        messagebox.showinfo('Basic Utilities','Test')
        Tk().withdraw()
        Tk().destroy()
        Tk().withdraw()
        filedialog.askopenfilename()
        filedialog.askdirectory()

    
    elif command == 'alm':
        for i in range(10):
            winsound.Beep(1500,500)
            winsound.Beep(1000,500)

    elif command == 'diran':
        print('Please select the folder to analyze')
        Tk().withdraw()
        dtoo = filedialog.askdirectory()
        
        cdt = datetime.datetime.now()
        try:
            os.system('cd '+dtoo+'&'+' dir'+'&'+' dir > directoryanalysis.txt')
        except:
            error(0)
        else:
            try:
                total_size = 0
                
                for path, dirs, files in os.walk(dtoo):
                    for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
                print("Directory size: " + str(total_size),'Bytes')
                print('folder is using',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of YOUR used memory ')
                print('folder is using',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of YOUR total memory ')
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Could not access directory to count size')
            try:
                f = open(dtoo+sysslash+'directoryanalysis.txt','a')
            except:
                error(0)
            else:
                f.write('\n')
                f.write('Directory analysis for '+dtoo+'\n')
                f.write('Made on '+str(datetime.datetime.now())+'\n')
                try:
                    f.write('Total Directory Size: '+str(total_size)+' Bytes'+'\n')
                except:
                    f.write('Could not get total directory size')
                else:
                    f.write('folder is using '+str((total_size / shutil.disk_usage(sysslash)[1]*100))+' % of YOUR used memory'+'\n')
                    f.write('folder is using '+str((total_size / shutil.disk_usage(sysslash)[0]*100))+' % of YOUR total memory ')
                f.close()
                print('Statistics written to '+dtoo+sysslash+'directoryanalysis.txt')
    elif command == 'tsklst':
        os.system('tasklist')

    elif command == 'rem':
        Tk().withdraw()
        da0 = messagebox.askyesno('Basic Utilities','Do you want to clear best time?')
        print('ClearBestTime =',da0)
        Tk().withdraw()
        da1 = messagebox.askyesno('Basic Utilities','Do you want to clear boot count?')
        print('ClearBootCount =',da1)
        Tk().withdraw()
        da2 = messagebox.askyesno('Basic Utilities','Do you want to clear birthday?')
        print('ClearBday=',da2)
        Tk().withdraw()
        da3 = messagebox.askyesno('Basic Utilities','Do you want to clear boot time?')
        print('ClearBootTime =',da3)
        Tk().withdraw()
        da4 = messagebox.askyesno('Basic Utilities','Do you want to clear game health?')
        print('ClearGameealth =',da4)
        Tk().withdraw()
        da5 = messagebox.askyesno('Basic Utilities','Do you want to clear browser history?')
        print('ClearBrowserHistory =',da5)
        Tk().withdraw()
        da6 = messagebox.askyesno('Basic Utilities','Do you want to clear Notifications settings?')
        print('ClearNotifs =',da6)
        Tk().withdraw()
        da7 = messagebox.askyesno('Basic Utilities','Do you want to clear game xp?')
        print('ClearXP =',da7)
        Tk().withdraw()
        da8 = messagebox.askyesno('Basic Utilities','Do you want to clear system Username?')
        print('ClearUsr =',da8)
        Tk().withdraw()
        da9 = messagebox.askyesno('Basic Utilities','Do you want to clear startup sound?')
        print('ClearStartSound =',da9)
        print('-----')
        print('Confirm? [y/n]')
        conf = input()
        if conf.lower().startswith('y'):
            f.close()
            if da0 == True:
                try:
                    os.remove('appdata.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da1 == True:
                try:
                    os.remove('bcount.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da2 == True:
                try:
                    os.remove('bday.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da3 == True:
                try:
                    os.remove('btime.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da4 == True:
                try:
                    os.remove('health.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da5 == True:
                try:
                    os.remove('history.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da6 == True:
                try:
                    os.remove('notifs.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da7 == True:
                try:
                    os.remove('xp.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da8 == True:
                try:
                    os.remove('username.txt')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            if da9 == True:
                try:
                    os.remove('startsound.dat')
                except:
                    print('File not found')
                else:
                    print('Deleted succesfully')
            log('User reset some appdata')
            Tk().withdraw()
            messagebox.showinfo('Basic Utilities','Press OK to reload BasicUtilities')
            reload()
    elif command == 'cln':
        fcln = 0
        try:
            os.remove('pre-uninstall.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('logoff.bat')
        except:
            fcln+=0
        else:
            fcln +=1
        try:
            os.remove('restart.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('clrapdat.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('ping.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('permaping.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('execute.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('stop.bat')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('notes.txt')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('notice.txt')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('changelog.txt')
            fcln +=1
        except:
            fcln +=0
        try:
            os.remove('license.txt')
            fcln +=1
        except:
            fcln +=0
        
        print(fcln,' useless files removed.')
        log('User cleaned out old files')


    elif command == 'emc2':
        print('Mass of Object? (kilograms please)')
        m = input()
        try:
            m = float(m)
        except:
            error(1)
        else:
            c = 299792458
            c2 = c**2
            e = m*c2
            print('Energy: '+str(e))

    elif command == 'sqrpyr':
        print('Length?')
        l = input()
        try:
            l = int(l)
        except:
            error(1)
        else:
            print('Width?')
            w = input()
            try:
                w = int(w)
            except:
                error(1)
            else:
                print('Height?')
                h = input()
                try:
                    h = int(h)
                except:
                    error(1)
                else:
                    print('The volume is '+str((l*w*h)/3)+' Cubic Units')

    elif command == 'tripyr':
        print('Length?')
        l = input()
        try:
            l = int(l)
        except:
            error(1)
        else:
            print('Width?')
            w = input()
            try:
                w = int(w)
            except:
                error(1)
            else:
                print('Height?')
                h = input()
                try:
                    h = int(h)
                except:
                    error(1)
                else:
                    print('The volume is '+str(((l*w)/2*h)/3)+' Cubic Units')

    elif command == 'bumem':
        dirpath = os.getcwd()
        try:
            total_size = 0
            
            for path, dirs, files in os.walk(dirpath):
                for f in files:
                    fp = os.path.join(path, f)
                    total_size += os.path.getsize(fp)
            print("Directory size: " + str(total_size),'Bytes')
            print('we are using',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of YOUR used memory :)')
            print('we are using',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of YOUR total memory :)')
        except:
            Tk().withdraw()
            messagebox.showerror('Error','Basic utilities is not able to access its own folder. What a shame.')

    elif command == 'filemem':
        Tk().withdraw()
        file_path = filedialog.askopenfilename()
        try:
            fsize = os.path.getsize(file_path)
            print('Size:',fsize,'Bytes')
            print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
            print('This file accounts for',(fsize / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
        except:
            error(1)

    elif command == 'sysmem':
        memory = shutil.disk_usage(sysslash)
        print('Total Memory '+str(memory[0])+' Bytes')
        print('Used Memory '+str(memory[1])+' Bytes')
        print('Free Memory '+str(memory[2])+' Bytes')
        print('You have used',((memory[1]/memory[0])*100),'%')

    elif command == 'folmem':
        total = 0
        Tk().withdraw()
        dirpath = filedialog.askdirectory()
        if str(dirpath) == '()':
            print('')
        else:
            try:
                total_size = 0
                
                for path, dirs, files in os.walk(dirpath):
                    for f in files:
                        fp = os.path.join(path, f)
                        total_size += os.path.getsize(fp)
                print("Directory size: " + str(total_size),'Bytes')
                print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[1]*100),'% of used memory')
                print('This folder accounts for',(total_size / shutil.disk_usage(sysslash)[0]*100),'% of total memory')
            except:
                Tk().withdraw()
                messagebox.showerror('Error','Basic utilities is not able to access this folder.')

    elif command == 'stat':
        print('lines: 5562')
        print('print statements: 854')
        print('Variables: 1433')
        print('comparisons 425')
        print('Exception handling loops 238')
        print('While loops 49')
        print('For loop 65')
        print('Commands: 139')
        print('Libraries Imported 22')
        print('files utilized 100')
        print('Tkinter windows used 103')

    elif command == 'sysplat':
        print('-----')
        print(platform.system())
        print(platform.release())
        print(platform.platform())
        print('-----')

    elif command == 'dir':
        print('-----')
        print(os.getcwd())
        print('-----')

    elif command == 'npicker':
        let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t''u','v','w','x','y','z']
        print('-----')
        for i in range(random.randint(2,12)):
            print(random.choice(let),end='',flush=True)
        print('')
        print('-----')

    elif command == 'tpicker':
        prefixes = ['she','kensing','park','new','Burn','Squa','Whis','Morton','Farris','Kalmy','Ruby','Fansing','','PArks','Sur','Castle']
        mid = ['field','aby','st','','','','Dooby']
        end = ['ton','ville','vill','don','hood','','Rey']
        print('-----')
        print(random.choice(prefixes)+random.choice(mid)+random.choice(end))
        print('-----')

    elif command == 'musplay':
        newwindow()
        file_path = filedialog.askopenfilename()
        try:
            playsound(file_path)
        except:
            error(1)

    elif command == 'rev':

        Tk().withdraw()
        file_path = filedialog.askopenfilename()
        f = open(file_path)
        data = f.read()
        strlen = len(data)
        newstr = data[strlen::-1]
        print(newstr)
        f.close()
        try:
            f = open(file_path+'rev','x')
        except:
            f = open(file_path+'rev','x')
        f.write(newstr)
        f.close()
    elif command == 'pi':
        print('How many units')
        units = input()
        try:
            units = int(units)
        except:
            error(1)
        else:
            piq = str('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
            print(piq[0:units])

    elif command == 'prime':
        num = 0
        prime = 0
        print('All prime numbers up to what?')
        units = input()
        try:
            units = int(units)
        except:
            error(1)
        else:
            for i in range(units):
                num += 1
                if num > 1:
                    for i in range(2,int(num/2)+1):
                        if (num % i) == 0:
                            nqtye = 0
                            break
                    else:
                        print(num)
                        prime += 1
                else:

                    nqtye = 0
            
            print('There were',prime,'prime numbers in that set')
            try:
                print('The prime number percent value is',str(prime/units*100)+' percent')
            except:
                print("We tried to print a percent, but you decided to devide by 0")
    elif command == 'fibb':
        print('How many units?')
        cmz = input()
        try:
            cmz = int(cmz)
        except:
            error(1)
        else:
            a = 0
            b = 1
            if cmz > 0:
                print(1)
            for i in range(cmz-1):
                c = a + b
                print(c)
                a = b
                b = c

    elif command == 'cmaj':
        if sysslash == '\\':
            x = 500
            winsound.Beep(261,x)
            winsound.Beep(293,x)
            winsound.Beep(329,x)
            winsound.Beep(349,x)
            winsound.Beep(392,x)
            winsound.Beep(440,x)
            winsound.Beep(493,x)
            winsound.Beep(523,x)
        else:
            Tk().withdraw()
            messagebox.showerror('BU','This command is not compatible with your device')

    elif command == 'fstat':
        print('What file to analyse? ')
        Tk().withdraw()
        fta = filedialog.askopenfilename()
        
        try:
            f = open(fta,'r')
        except:
            error(2)
        else:
            try:
                data = f.read()
            except:
                f.close()
                Tk().withdraw()
                messagebox.showinfo('File Error','Basic Utilities cannot read this file. It may be compressed or unreadable.')
            else:
                size = len(data)
                print('Will write file statistics to',fta+'.fstat')
                if size < 1000:
                    print('PREVIEW:')
                    print('-----')
                    print(data)
                    print('-----')
                else:
                    print('Oops! File was to large to preview')
                print('Characters:',size)
                if size < 1000:
                    fs = size
                    fs = str(str(fs)+' bytes')
                    print('File Size:',size,'bytes')
                elif size > 1000 and size < 1000000:
                    fs = size/1024
                    print('File Size:',fs,'kilobytes')
                    fs = str(str(fs)+' kilobytes')
                else:
                    fs = size /1000/1024
                    print('File Size:',fs,'megabytes')
                    fs = str(str(fs)+ ' megabytes')
                aol = 0
                f.close()
                f = open(fta)
                tiwieyc = f.readlines()
                while True:
                    try:    
                        x = tiwieyc[aol]
                        aol = aol + 1
                    except:
                        break
                print('Amount of lines:',aol)
                tw = fta+'.fstat'
                print('Writing to',tw)
                f.close()
                try:
                    f = open(tw,'x')
                    f.write('Characters = '+str(size)+'\n')
                    f.write('Size = '+str(fs)+'\n')
                    f.write('Lines = '+str(aol)+'\n')
                    
                except:
                    f = open(tw,'w')
                    f.write('Characters = '+str(size)+'\n')
                    f.write('Size = '+str(fs)+'\n')
                    f.write('Lines = '+str(aol)+'\n')
                    
                finally:
                    f.close()
                

    elif command == 'permaping':
        def pgo0():
            global txt
            res = txt.get()
            pping.destroy()
            pping.quit()
            
            try:
                os.system('ping '+res+' -t')
            except:
                error(1)
        pping = Tk()
        pping.title('permapinger')
        lbl = Label(pping,text='IP address to ping')
        lbl.grid(column=0,row=0)
        btn = Button(pping,text='Close',command=pping.destroy,bg='yellow')
        btn.grid(column=1,row=0)
        txt = Entry(pping,width=20)
        txt.grid(column=0,row=1)
        btn1 = Button(pping,text='Ping',command=pgo0,bg='green')
        btn1.grid(column=1,row=1)
        pping.mainloop()
        pping.quit()

    elif command =='ping':
        def pgo1():
            global txt
            global txt1
            global btn1
            btn1['state'] = 'disabled'
            res = txt.get()
            res1 = txt1.get()
            try:
                os.system('ping '+res+' -n '+res1)
            except:
                error(3)
            btn1['state'] = 'normal'
        ping = Tk()
        ping.title('pinger')
        lbl = Label(ping,text='IP address to ping')
        lbl1 = Label(ping,text='Number of times to ping')
        lbl.grid(column=0,row=0)
        lbl1.grid(column=1,row=0)
        btn = Button(ping,text='Close',command=ping.destroy,bg='Yellow')
        btn.grid(column=2,row=0)
        txt = Entry(ping,width=20)
        txt.grid(column=0,row=1)
        txt1 = Entry(ping,width=10)
        txt1.grid(column=1,row=1)
        btn1 = Button(ping,text='Ping',command=pgo1,bg='green')
        btn1.grid(column=2,row=1)
        ping.mainloop()
        ping.quit()

    
    elif command =='cmd':
        def go2():
            global txt
            cmdtr = txt.get()
            try:
                os.system(cmdtr)
            except:
                error(3)
        cmdc = Tk()
        cmdc.title('Command Executor')
        lbl = Label(cmdc,text='Command to execute')
        lbl.grid(column=0,row=0)
        btn = Button(cmdc,text='Close',command=cmdc.destroy,bg='yellow')
        btn.grid(column=1,row=0)
        txt = Entry(cmdc,width=50)
        txt.grid(column=0,row=1)
        btn1 = Button(cmdc,text='Go',command=go2,bg='green')
        btn1.grid(column=1,row=1)
        cmdc.mainloop()
        cmdc.quit()

        
        
    elif command == 'ip':
        try:
            ip = get('https://api.ipify.org').text
            print('Your public IPv4 address is: {}'.format(ip))
        except Exception as e:
            toplevelerror('ERROR\n'+str(e))

    elif command == 'ip6':
        try:
            ip = get('https://api64.ipify.org').text
            print('Your public IPv6 address is: {}'.format(ip))
        except Exception as e:
            toplevelerror('ERROR\n'+str(e))

    elif command == 'rmg':
        if sysslash == '\\':
            for i in range(random.randint(20,50)):
                winsound.Beep(random.randint(200,1000),random.randint(200,1000))
        else:
            Tk().withdraw()
            messagebox.showerror('BU','Please use a microsoft device to run this command.')
            

    elif command == 'toneup':
        if sysslash == '\\':
            print('Starting tone? (HZ)')
            st = input()
            try:
                st = int(st)
            except:
                error(1)
            else:
                print('Ending tone? (Hz)')
                et = input()
                try:
                    et = int(et)
                except:
                    error(1)
                else:
                    while st < et:
                        winsound.Beep(st,100)
                        st = st + 10
                        print('Played tone of',st,'Hertz')
        else:
            Tk().withdraw()
            messagebox.showerror('BU','Please use a microsoft device to run this command.')

    elif command == 'hex':
        print(random.choice([0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']))
    elif command == 'hexbi':
        print(random.choice([0,1,2,3,4,5,6,7,8,9,'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']))

    elif command == 'curse':
        if sysslash == '\\':
            for i in range(random.randint(1,10)):
                winsound.Beep(1000,random.randint(200,1500))
                print(random.randint(1,10)*'*')
                sleep(random.randint(1,10)/10)
        else:
            Tk().withdraw()
            messagebox.showerror('BU','Please use a microsoft device to execute this command.')
            

    elif command == 'beep':
        if sysslash == '\\':
            print('What frequency?')
            freq = input()
            try:
                freq = int(freq)
            except:
                error(1)
            else:
                print('How many milliseconds?')
                playse = input()
                try:
                    playse = int(playse)
                except:
                    error(1)
                else:
                    if playse > 0:
                        winsound.Beep(freq,playse)
                    else:
                        error(1)

        else:
            Tk().withdraw()
            messagebox.showerror('BU','Please use a Microsoft device to execute this comamnd.')

    elif command == 'game2':
        newwindow()
        

        print('Welcome',sysuser,'to Discount Prodigy')
        print('Discount prodigy is a game where you cast spells against monsters.')
        print('To cast spells, you must answer simple math problems')
        print('As you cast spells, you earn points.')
        print('Press enter to begin.')
        input()
        fightmonsters = True
        monster_names = ['Black Widow','Wulf','Slayer','Shredder','Magma','The Kraken']
        monsters_battled = 0
        monsters_won = 0
        monsters_lost = 0
        try:
            f = open('xp.txt','r')
            xp = f.read()
        except:
            f = open('xp.txt','x')
            f.write('0')
            f.close()
            xp = 0
        try:
            xp = float(xp)
        except:
            xp = 0
            f = open('xp.txt','w')
            f.write('0')
            f.close()
        try:
            f = open('health.txt','r')
            health = f.read()
        except:
            f = open('health.txt','x')
            f.write('100')
            f.close()
            health = 100
        try:
            health = float(health)
        except:
            health = 100
            f = open('health.txt','w')
            f.write('100')
            f.close()
        blhealth = health
        blxp = xp
        while fightmonsters == True:
            print('A monster wants to battle you! do you want to battle?(y/n)')
            battle = input()
            if battle.lower().startswith('y'):
                monsterbattle_name = random.choice(monster_names)
                monster_health = health//(random.randint(12,24)/10)
                blmh = monster_health
                print('Your enemy is',monsterbattle_name)
                print(monsterbattle_name,'has',monster_health,'health')
                print('press enter to continue')
                input()
                if monsterbattle_name == 'Black Widow':
                    monster_spells = ['Poke','Venom','Crush']
                elif monsterbattle_name == 'Wulf':
                    monster_spells = ['Claw','Bite','Slaughter']
                elif monsterbattle_name == 'Slayer':
                    monster_spells = ['Execute','Corrupt','Overwrite the boot sector']
                elif monsterbattle_name == 'Shredder':
                    monster_spells = ['Shred','Big shred','Ultra Shred']
                    # I am running out of ideas :(
                elif monsterbattle_name == 'Magma':
                    monster_spells = ['Burn','Roast''Erupt']
                elif monsterbattle_name == 'The Kraken':
                    monster_spells = ['Wave','Tsunami','Horror of the Deep']
                else:
                    Tk().withdraw()
                    messagebox.showwarning('Exception','Unrecognized monster name. Will revert to base spells')
                    monster_spells = ['spell.placeholder.small','spell.placeholder.med','spell.placeholder.large']
                spells = ['Wingardium Leviosa','Impedimenta','Avada Kedavra']
                while monster_health > 0 and health > 0:
                    failed = False
                    print('Your spells are',spells[0],',',spells[1],',',spells[2])
                    print('What spell do you want to use? You may also use numbers 1,2,3.')
                    spell_used = input()
                    if spell_used == spells[0] or spell_used == spells[1] or spell_used == spells[2] or spell_used == '1' or spell_used == '2' or spell_used == '3':
                        if spell_used == spells[0] or spell_used == '1':
                            print('Answer this question')
                            a = random.randint(1,100)
                            b = random.randint(1,100)
                            print('What is',a,'+',b,'?')
                            answ = input()
                            try:
                                answ = int(answ)
                            except:
                                error(1)
                                print('Because we cant kick you to the command menu, we will restart the program')
                                reload()
                            else:
                                if answ == a + b:
                                    print('You got it correct')
                                    spell_damage = blhealth /10 * (random.randint(10,20)/10)
                                    print('You did',spell_damage,'damage')
                                    monster_health -= spell_damage
                                else:
                                    print('You got it wrong')
                                    print('Correct answer was',a+b)
                        elif spell_used == spells[1] or spell_used == '2':
                            print('Answer this question')
                            a = random.randint(1,100)
                            b = random.randint(1,100)
                            while b > a:
                                b = random.randint(1,100)
                            print('What is',a,'-',b,'?')
                            answ = input()
                            try:
                                answ = int(answ)
                            except:
                                error(1)
                                print('Because we cant kick you to the command menu, we will restart the program')
                                reload()
                            else:
                                if answ == a - b:
                                    print('You got it correct')
                                    spell_damage = blhealth /10 * (random.randint(20,50)/10)
                                    print('You did',spell_damage,'damage')
                                    monster_health -= spell_damage
                                    
                                else:
                                    print('You got it wrong')
                                    print('Correct answer was',a-b)
                        elif spell_used == spells[2] or spell_used == '3':
                            print('Answer this question')
                            a = random.randint(1,12)
                            b = random.randint(1,12)
                            print('What is',a,'*',b,'?')
                            answ = input()
                            try:
                                answ = int(answ)
                            except:
                                error(1)
                                print('Because we cant kick you to the command menu, we will restart the program')
                                reload()
                            else:
                                if answ == a * b:
                                    print('You got it correct')
                                    spell_damage = blhealth /10 * (random.randint(50,100)/10)
                                    print('You did',spell_damage,'damage')
                                    monster_health -= spell_damage
                                else:
                                    print('You got it wrong')
                                    print('Correct answer was',a*b)
                        xp += spell_damage
                        print(monsterbattle_name,'has',monster_health,'health')
                        if monster_health < 1:
                            break
                        print('It is now',monsterbattle_name,'turn')
                        mspell_used = random.choice(monster_spells)
                        print(monsterbattle_name,'used',mspell_used)
                        if mspell_used == monster_spells[0]:
                            mspell_damage = blmh /10 * (random.randint(10,20)/10)
                        elif mspell_used == monster_spells[1]:
                            mspell_damage = blmh /10 * (random.randint(20,50)/10)
                        elif mspell_used == monster_spells[2]:
                            mspell_damage = blmh /10 * (random.randint(50,100)/10)
                        print(monsterbattle_name,'did',mspell_damage,'against you')
                        health -= mspell_damage
                        print('You now have',health,'health')
                print('Game Over')
                if health < 1:
                    print('You lost')
                    monsters_lost = monsters_lost + 1
                elif monster_health < 1:
                    print('You won!')
                    monsters_won += 1
                monsters_battled += 1
                print('You gained',xp-blxp,'XP This round for a total of',xp)
                print('You have won against',monsters_won,'This session')
                print('You lost against',monsters_lost,'This session')
                print('For a total of',monsters_battled)
                print('You have a winning ration of',(str(monsters_won/monsters_battled*100)+' %'))
                health = blhealth + (random.randint(blmh//8,blmh//5))
                print('You gained',health-blhealth,'health This round for a total of',health)
                print('')
                print('Writing Statistics...',end='\r')
                try:
                    f = open('xp.txt','w')
                    f.write(str(xp))
                except:
                    f = open('xp.txt','x')
                    f.write(str(xp))
                f.close()
                try:
                    f = open('health.txt','w')
                    f.write(str(health))
                except:
                    f = open('health.txt','x')
                    f.write(str(health))
                f.close()
                print('Writing Statistics...done')
                print('')
            elif battle == 'n':
                break
            
    
    elif command == 'ls':
        runfile('license.txt')
    
        
    elif command == 'degp':
        print('How many degrees?')
        der = input()
        try:
            deg = int(der)
        except:
            error(1)
        else:
            deg = deg / 360
            deg = deg * 100
            print(der,'degrees is',deg,'percent.')
    elif command == 'pdeg':
        print('How many percent?')
        der = input()
        try:
            deg = int(der)
        except:
            error(1)
        else:
            deg = deg * 360
            deg = deg / 100
            print(der,'percent is',deg,'degrees.')
    elif command == 'tempt':
        print('Celsius (c), Farenheight (f), or Kelvin (k)')
        tcmd = input()
        if tcmd == 'c' or tcmd == 'f' or tcmd == 'k':
            print('What to convert to? (c,f,k)')
            ccmd = input()
            if ccmd == 'c' or ccmd == 'f' or ccmd == 'k':
                cmd = tcmd + ccmd
                print('Value to convert?')
                vtc = input()
                try:
                    vtc = float(vtc)
                except:
                    error(1)
                else:
                    if cmd == 'cf':
                        res = (vtc*9/5)+32
                        print('Converted is',res)
                    elif cmd == 'fc':
                        res = (vtc-32)*5/9
                        print('Converted is',res)
                    elif cmd == 'ck':
                        res = vtc - 273
                        print('Converted is',res)
                    elif cmd == 'kc':
                        res = vtc + 273
                        print('Converted is',res)
                    else:
                        Tk().withdraw()
                        messagebox.showwarning('Warning','Invalid Command Combination')
            else:
                Tk().withdraw()
                messagebox.showwarning('Warning','Invalid Command Combination')           

    elif command == 'cpicker':
        colours = ['red','orange','yellow','lime','green','turquois','blue','navy','purple','magenta','pink','brown','black','white']
        print('The chosen colour is',random.choice(colours))
    elif command == 'picker':
        pickable = []
        xmxa = False
        while True:
            print('Do you want to add an item? (y/n)')
            makenew = input()
            if makenew.lower().startswith('y'):
                print('What to add?')
                poi = input()
                pickable.append(poi)
                xmxa = True
            elif makenew == 'n' and xmxa == True:
                selection = random.choice(pickable)
                print('Your selection is',selection)
                break
            else:
                print('Please make sure that there is more than 0 items on the list and that you typed in a valid command.')
        
    elif command == 'progcount':
        newwindow()
        print('')
        
        while True:
            x = datetime.datetime.now()
            a = x.year
            b = x.month
            c = x.day
            d = x.hour
            e = x.minute
            f = x.second
            d1 = datetime.datetime(a,b,c,d,e,f)
            d0 = datetime.datetime(2021,4,14,15,30,0)
            difference = d1 - d0
            total_seconds = difference.total_seconds()
            total_min = total_seconds / 60
            total_hr = total_min / 60
            total_dy = total_hr / 24
            total_wk = total_dy /7
            total_yr = total_dy / 365
            total_mt = total_yr * 12
            print("")
            print("There are",total_seconds,"seconds since")
            print("There are",total_min,"minutes since")
            print("There are",total_hr,"hours since")
            print("There are",total_dy,"days since")
            print("There are",total_wk,"weeks since")
            print("There are",total_mt,"month since")
            print("There are",total_yr,"years since This program exisited.")
            sleep(1)
        
    elif command == 'crash':
        raise RuntimeError('Manual Crash')
        
    elif command == 'notifs':
        def nn():
            global nf
            try:
                f = open('notifs.txt','w')
                f.write('0')
            except:
                f = open('notifs.txt','x')
                f.write('0')
            f.close()
            nf.destroy()
        def cn():
            global nf
            try:
                f = open('notifs.txt','w')
                f.write('1')
            except:
                f = open('notifs.txt','x')
                f.write('1')
            finally:
                f.close()
            nf.destroy()
        def mn():
            global nf
            try:
                f = open('notifs.txt','w')
                f.write('2')
            except:
                f = open('notifs.txt','x')
                f.write('2')
            f.close()
            nf.destroy()
        nf = Tk()
        nf.title('Notifications settings')
        lbl = Label(nf,text='Select your notification settings')
        lbl.grid(column=1,row=0)
        btn = Button(nf,text='no notifications',command=nn)
        btn.grid(column=0,row=1)
        btn = Button(nf,text='console notifications (default)',command=cn)
        btn.grid(column=1,row=1)
        btn = Button(nf,text='messagebox notifications',command=mn)
        btn.grid(column=2,row=1)
        nf.mainloop()
        
    elif command == 'encode':
        print("Please select the file to encode.")
        Tk().withdraw()
        um = filedialog.askopenfilename()
        try:
            f = open(um)
            um = f.read()
            f.close()
        except:
            Tk().withdraw()
            messagebox.showerror(':(','Access denied')
            um = 'Access Denied'
        print('Unencoded Message:',um) 
        print("Message has a size of",len(um),"bytes")
        string = um.lower()
        enc = string.replace('a','NJ').replace('b','MPE').replace('c','CEXC').replace('d','QUIE').replace('e','*U&P/HTPS')\
        .replace('f','XML').replace('g','MDD').replace('h','BU#').replace('i','NNQP').replace('j','DYE').replace('k','AVOO').replace('l','AXZ')\
        .replace('m','LOL').replace('n','/-/').replace('o','NYX').replace('p','VAN').replace('q','FKUWEUI').replace('r','QYIF')\
        .replace('s','GHQ[W]').replace('t','CUED').replace('u','MOM').replace('v','OTW').replace('w','BITLY').replace('x','ENDER')\
        .replace('y','EXE').replace('z','GLHAC.P').replace('0','NULL').replace('1','0').replace('2','1').replace('3','2')\
        .replace('4','3').replace('5','4').replace('6','5').replace('7','6').replace('8','7').replace('9','8').replace(' ','PWSAC')

        print(enc,"is your encoded script")
        print("Size:",len(enc),"bytes")
        print("Do you want to write this to a file?(y/n)")
        sda = input()
        if sda.lower().startswith('y'):
            print('What directory to write to?')
            Tk().withdraw()
            fexx = filedialog.askdirectory()
            if fexx == '()':
                print('')
            else:
                print("What file name do you want it to be written to? No extension needed.")
                fex = input()
                fex = fex + '.bue'
                fex = fexx + sysslash +fex
                try:
                    f = open(fex,'x')
                    f.write(enc)
                    f.close()
                    print("written to",fex)
                except:
                    try:
                        f = open(fex,'w')
                        f.write(enc)
                        f.close()
                        print("written to",fex)
                    except:
                        Tk().withdraw()
                        messagebox.showerror(':(','Access Denied')
            
    elif command == 'translate':
        print("Please select file to translate.")
        Tk().withdraw()
        file_path = filedialog.askopenfilename()
        
        try:
            f = open(file_path,'r')
            mes = f.read()
            print("encoded message is",len(mes),"bytes")
        except:
            error(1)
        else:
            tra = mes.replace('GLHAC.P','z').replace('EXE','y').replace('ENDER','x').replace('BITLY','w').replace('OTW','v')\
            .replace('MOM','u').replace('CUED','t').replace('GHQ[W]','s').replace('QYIF','r').replace('FKUWEUI','q').replace('VAN','p')\
            .replace('NYX','o').replace('/-/','n').replace('LOL','m').replace('AXZ','l').replace('AVOO','k').replace('DYE','j')\
            .replace('NNQP','i').replace('BU#','h').replace('MDD','g').replace('XML','f').replace('*U&P/HTPS','e').replace('QUIE','d')\
            .replace('CEXC','c').replace('MPE','b').replace('NJ','a').replace('8','9').replace('7','8').replace('6','7').replace('5','6')\
            .replace('4','5').replace('3','4').replace('2','3').replace('1','2').replace('0','1').replace('NULL','0').replace('PWSAC',' ')
            print(tra,'is the translation')
            print('size:',len(tra),'bytes')
            print("Do you want to write this to a txt file?(y/n)")
            wt = input()
            if wt.lower().startswith('y'):
                print('What directory to write to?')
            Tk().withdraw()
            fexx = filedialog.askdirectory()
            if fexx == '()':
                print('')
            else:
                print("What file name do you want it to be written to? No extension needed.")
                fex = input()
                fex = fex + '.txt'
                fex = fexx + sysslash +fex
                try:
                    f = open(fex,'x')
                    f.write(enc)
                    f.close()
                    print("written to",fex)
                except:
                    try:
                        f = open(fex,'w')
                        f.write(enc)
                        f.close()
                        print("written to",fex)
                    except:
                        Tk().withdraw()
                        messagebox.showerror(':(','Access Denied')
    elif command == 'bday':
        print('What month is your birthday on?')
        mt = input()
        try:
            mt = int(mt)
        except:
            error(1)
        else:
            print("What day?")
            dy = input()
            try:
                dy = int(dy)
            except:
                error(1)
            else:
                mt = str(mt)
                dy = str(dy)
                mt = mt + '\n'
                try:
                    f = open('bday.txt','x')
                    f.write(mt)
                    f.write(dy)
                except:
                    f = open('bday.txt','w')
                    f.write(mt)
                    f.write(dy)
                finally:
                    f.close()
        
    elif command == 'colour' or command == 'color':
        try:
            s = turtle.getscreen()
            t = turtle.Turtle()
        except:
            s = turtle.getscreen()
            t = turtle.Turtle()
        def colourchange():
            global txt
            global txt1
            global txt2
            res = txt.get()
            res1 = txt1.get()
            res2 = txt2.get()
            efyi = True
            while efyi == True:
                try:
                    a = int(res)
                except:
                    error(1)
                    break
                
                try:
                    b = int(res1)
                except:
                    error(1)
                    break
                try:
                    c = int(res2)
                except:
                    error(1)
                    break       
                wx = turtle.Screen()
                wx.colormode(255)
                try:
                    turtle.Screen().bgcolor(a,b,c)
                except:
                    error(0)
                    error(5)
                finally:
                    break
        def bby():
            ct.destroy()
            try:
                turtle.bye()
            except:
                error(0)
        ct = Tk()
        ct.title('Window')
        txt = Entry(ct,width=10,bg='red')
        txt.grid(column=0,row=0)
        txt1 = Entry(ct,width=10,bg='green')
        txt1.grid(column=1,row=0)
        txt2 = Entry(ct,width=10,bg='blue')
        txt2.grid(column=2,row=0,)
        btn = Button(ct,text='Generate colour',command=colourchange,bg='green')
        btn.grid(column=1,row=1)
        lbl = Label(ct,text='Please enter values between 0 and 255')
        lbl.grid(column=1,row=2)
        btn1 = Button(ct,text='Exit',command=bby,bg='red')
        btn1.grid(column=0,row=1)
        ct.mainloop()
        
    elif command == 'clean your room':
        Tk().withdraw()
        messagebox.showerror('Error','Computers cannot clean their rooms')
    elif command == 'ur mom':
        Tk().withdraw()
        messagebox.showerror('Error','Shut up, you inmature child')
    elif command == 'spam':
        for i in range(20):
            try:
                os.startfile('error.vbs')
            except:
                pyutils39.toplevelerror('Please use version 2.19.4 or earlier!')
                break
            else:
                c = random.randint(3,13)
                c = c/10
                sleep(c)

    elif command == 'cpg':
        print("To return to the command menu, make sure all other Tk windows are closed.")
        def rot():
            try:
                t.right(90)
            except:
                error(7)

        def bb():
            ct.destroy()
            try:
                turtle.bye()
            except:
                error(0)
        def go():
            global txt
            global abh
            res = txt.get()
            try:
                res = int(res)
            except:
                error(1)
            else:
                try:
                    t.forward(res)
                except:
                    error(7)
                else:
                    ps = t.pos()
                    print("You are at",ps)
                    print("You need to go to",abh)
                    ps = str(ps)
                    abh = str(abh)
                    if ps == abh:
                        bb()
                        print("Yay! You did it!")

        def undo():
            t.undo()


        try:
            s = turtle.getscreen()
            t = turtle.Turtle()
        except:
            s = turtle.getscreen()
            t = turtle.Turtle()
        a = random.randint(-200,200)
        b = random.randint(-200,200)
        t.penup()
        t.goto(a,b)

        t.stamp()
        abh = t.pos()
        print("Go to",abh)
        amx = random.randint(-200,200)
        amd = random.randint(-200,200)
        t.goto(amd,amx)
        t.pendown()
        t.pencolor('blue')
        ct = Tk()
        ct.title('Control Panel')
        btn = Button(ct,text='rotate 1/4 turn CW',command=rot)
        btn.grid(column=0,row=0)
        btn2 = Button(ct,text='Exit',command=bb,bg='red')
        btn2.grid(column=1,row=0)
        txt = Entry(ct,width=10)
        txt.grid(column=0,row=1)
        btn3 = Button(ct,text='Go',command=go,bg='green')
        btn3.grid(column=1,row=1)
        btn4 = Button(ct,text='Undo',command=undo,bg='yellow')
        btn4.grid(column=0,row=2)
        ct.mainloop()

    elif command == 'clr':
        f.close()
        try:
            os.remove('appdata.txt')
        except:
            print('File not found')
        try:
            os.remove('bcount.txt')
        except:
            print('File not found')
        try:
            os.remove('bday.txt')
        except:
            print('File not found')
        try:
            os.remove('btime.txt')
        except:
            print('File not found')
        try:
            os.remove('health.txt')
        except:
            print('File not found')
        try:
            os.remove('history.txt')
        except:
            print('File not found')
        try:
            os.remove('notifs.txt')
        except:
            print('File not found')
        try:
            os.remove('xp.txt')
        except:
            print('File not found')
        try:
            os.remove('username.txt')
        except:
            print('File not found')

        reload()

    elif command == 'uninstall':
        f.close()
        
        try:
            os.startfile('unins000.exe')
            
        except:
            error(2)
            print('Main uninstaller failed to start.')
        else:
            os.system('taskkill /F /IM BasicUtilities.exe')

    elif command == 'wb':
        webbrowser.open('https://bit.ly/enderexe')

    elif command == 'anim':
        for i in range(10):
            print('|',end='\r')
            sleep(0.1)
            print('/',end='\r')
            sleep(0.1)
            print('-',end='\r')
            sleep(0.1)
            print('\ ',end='\r')
            sleep(0.1)
            print('|',end='\r')
            sleep(0.1)
            print("/ ",end='\r')
            sleep(0.1)
            print('-',end='\r')
            sleep(0.1)
            print('\ ',end='\r')
            sleep(0.1)

    elif command == 'conv':
        print("-----Subcommands for Convert-----")
        print("conv len: convert length of things")
        print("conv cmd: Converter command menu")

    elif command == 'conv len':
        print("-----Subcommands for Convert Length-----")
        print("conv len m-f: Metres to Feet")
        print("conv len f-m: Feet to metres")
        print("conv len i-c: Inches to centimeters")
        print("conv len c-i: centimetres to inches")
        print("conv len i-y: inches to yards")
        print("conv len m-y: meters to yards")
        print("conv len c-y: centimeters to yards")
        print("conv len y-i: yards to inches")
        print("conv len y-m: yards to meters")
        print("conv len y-c: yards to centimeters")
        

    elif command == 'conv len i-y':
        conv('inches','yards',"/48")
    elif command == 'conv cmd':
        xay = True
        while xay == True:
            print('-----Converter Command Menu-----')
            print('Type your command under here and press enter')
            mxe = input()
            if mxe == 'help' or mxe =='?':
                print('-----Commands List for Conv-----')
                print('help: Shows this list')
                print('cmd: Go to the command menu')
                print('km-mi: kilometres to miles')
                print('mi-km: miles to kilometres')
                print('kg-lb: Kilograms to pounds')
                print('lb-kg: pounds to kilograms')

            elif mxe == 'lb-kg':
                conv('pounds','kilograms','/2.20463')
                
            
            elif mxe == 'kg-lb':
                conv('kilograms','pounds','*2.20463')

            elif mxe == 'cmd':
                break
            elif mxe == 'km-mi':
                conv('kilometres','miles','/1.609')
            elif mxe == 'mi-km':
                conv('miles','kilometres','*1.609')
            else:
                print('You typed in an unrecognized command. \n\
                    Type "help" or "?" for the commands list.')

    elif command == 'conv len c-y':
        conv('centimeters','yards','*0.010936')
    elif command == 'conv len y-c':
        conv('yards','centimeters','*91.44')

    elif command == 'conv len y-m':
        conv('yards','meters','*1.093613')

    elif command == 'conv len m-y:':
        conv('meters','yards','/1.093613')

    elif command == 'conv len y-i':
        conv('inches','yards',"*48")

    elif command == 'conv len c-i':
        #/2.54
        conv('centimeters','inches',"/2.54")

    elif command == 'conv len i-c':
        conv('inches','centimeter','*2.54')

    elif command == 'conv len m-f':
        #* 3.28084
        conv('metres','feet','*3.28084')

    elif command == 'conv len f-m':
        conv('feet','meters','/3.28084')

    elif command == "timer":
        newwindow()
        print("How many seconds?")
        sc_tm = input()

        paused = False
        def tmmain():
            global sc_tm
            global paused
            while sc_tm > 0 and paused == False:
                try:
                    lbl.configure(text=sc_tm)
                except:
                    break
                sc_tm = sc_tm - 1
                sleep(1)
            if sc_tm < 1:
                tmdone()

        def tmdone():
            global btn23
            global btn22
            global btn25
            btn23['state'] = 'disabled'
            btn22['state'] = 'disabled'
            btn25['state'] = 'normal'
            global btn24
            btn24['state'] = 'normal'
            try:
                lbl.configure(text='Timer is Done')
            except:
                error(0)
            print("Your timer is done")
            try:
                winsound.Beep(1000,1000)
            except:
                error(2)

        def tmstart():
            global paused
            th = threading.Thread(target=tmmain)
            paused = False
            global btn22
            global btn25
            btn22['state'] = 'disabled'
            btn25['state'] = 'disabled'
            global btn24
            btn24['state'] = 'disabled'
            th.start()

        def tmkill():
            global tm
            global paused
            paused = True
            tm.quit()
            tm.destroy()

        def tmstop():
            global paused
            paused = True
            btn22['state'] = 'normal'
            btn25['state'] = 'normal'
            global btn24
            btn24['state'] = 'normal'

        def tmreset():
            global paused
            global sc_tm
            sc_tm = tm_full
            btn22['state'] = 'normal'
            btn23['state'] = 'normal'

            lbl.configure(text='Waiting for Start')
            paused = False
        try:
            sc_tm = int(sc_tm)
        except:
            error(1)
        else:
            tm_full = sc_tm
            tm = Tk()
            tm.title('Timer')
            tm.geometry("400x100")
            lbl = Label(tm,text='Waiting for start')
            lbl.grid(column=0,row=0)
            btn22 = Button(tm,text='Start',command=tmstart,bg="green")
            btn22.grid(column=0,row=1)
            btn23 = Button(tm,text="Pause",command=tmstop,bg="yellow")
            btn23.grid(column=1,row=1)
            btn24 = Button(tm,text="Stop",command=tmkill,bg='red')
            btn24.grid(column=2,row=1)
            btn25 = Button(tm,text='Reset',command=tmreset,bg='blue')
            btn25.grid(column=3,row=1)
            tm.mainloop()


    elif command == 'draw':
        newwindow()
        print("Please turn your attention to the Tkinter windows. If there are errors, they will be in the console.")
        window = Tk()
        window.title('LetsDraw')
        window.geometry('700x400')
        try:
            s = turtle.getscreen()
            t = turtle.Turtle()
        except:
            s = turtle.getscreen()
            t = turtle.Turtle()
        turtle.title("Let's Draw Canvas")
        def go_forward():
            global txt
            res = txt.get()
            try:
                res = float(res)
            except ValueError:
                error(1)
            else:
                try:
                    t.forward(res)
                except:
                    error(0)

        def go_backward():
            global txt1
            res = txt1.get()
            try:
                res = float(res)
            except:
                error(1)
            else:
                try:
                    t.backward(res)
                except:
                    error(0)

        def turn_left():
            global txt2
            res = txt2.get()
            try:
                res = float(res)
            except:
                error(1)
            else:
                try:
                    t.left(res)
                except:
                    error(0)
        def turn_right():
            global txt3
            res = txt3.get()
            try:
                res = float(res)
            except:
                error(1)
            else:
                try:
                    t.right(res)
                except:
                    error(0)

        def changecolor():
            global txt4
            res = txt4.get()
            try:
                t.pencolor(res)
            except:
                error(1)

        def changefill():
            global txt5
            res = txt5.get()
            try:
                t.fillcolor(res)
            except:
                error(1)

        def go_to():
            global txt6
            global txt7
            res = txt6.get()
            res1 = txt7.get()
            try:
                res = int(res)
                res1 = int(res1)
            except:
                error(1)
            else:
                try:
                    t.goto(res,res1)
                except:
                    error(0)

        def pensize():
            global txt8
            res = txt8.get()
            try:
                res = int(res)
            except:
                error(1)
            else:
                try:
                    t.pensize(res)
                except:
                    error(0)

        def dot():
            global txt9
            res = txt9.get()
            try:
                res = int(res)
            except:
                error(1)
            else:
                try:
                    t.dot(res)
                except:
                    error(0)

        def save():
            global txt10
            res = txt10.get()
            res1 = ".eps"
            res = res + res1
            s.getcanvas().postscript(file=res)
        def conv():
            webbrowser.open("https://epsviewer.org/onlineviewer.aspx")
        def circ():
            global txt11
            res = txt11.get()
            try:
                res = int(res)
            except:
                error(1)
            else:
                try:
                    t.circle(res)
                except:
                    error(0)
        def square():
            global txt12
            res = txt12.get()
            try:
                res = float(res)
            except:
                error(1)
            else:
                for i in range(4):
                    try:
                        t.forward(res)
                        t.right(90)
                    except:
                        error(0)

        def byebye():
            global tcrash
            window.destroy()
            turtle.bye()
            tcrash = True


        lbl = Label(window,text='Lets Draw',font=("Arial Bold",12))
        lbl.grid(column=0,row=0)
        btn = Button(window,text='Exit',command=byebye,bg="red")
        btn.grid(column=1,row=0)

        txt = Entry(window,width=10)
        txt.grid(column=0,row=1)
        btn1 = Button(window,text='Go',command=go_forward,bg="green")
        btn1.grid(column=1,row=1)
        lbl1 = Label(window,text='Go forward this many units')
        lbl1.grid(column=2,row=1)

        txt1 = Entry(window,width=10)
        txt1.grid(column=0,row=2)
        btn2 = Button(window,text='Go',command=go_backward,bg="green")
        btn2.grid(column=1,row=2)
        lbl2 = Label(window,text='Go backward this many units')
        lbl2.grid(column=2,row=2)


        txt2 = Entry(window,width=10)
        txt2.grid(column=0,row=3)
        btn3 = Button(window,text='Go',command=turn_left,bg="green")
        btn3.grid(column=1,row=3)
        lbl3 = Label(window,text='Turn left this many degrees')
        lbl3.grid(column=2,row=3)

        txt3 = Entry(window,width=10)
        txt3.grid(column=0,row=4)
        btn4 = Button(window,text='Go',command=turn_right,bg="green")
        btn4.grid(column=1,row=4)
        lbl4 = Label(window,text='Turn right this many degrees')
        lbl4.grid(column=2,row=4)
        btn5 = Button(window,text='pen up',command=t.penup)
        btn5.grid(column=0,row=5)
        btn6 = Button(window,text='pen down',command=t.pendown)
        btn6.grid(column=1,row=5)
        btn7 = Button(window,text='undo',command=t.undo,bg="yellow")
        btn7.grid(column=2,row=5)
        btn8 = Button(window,text='clear canvas',command=t.clear,bg="orange")
        btn8.grid(column=3,row=5)
        btn9 = Button(window,text='Start fill',command=t.begin_fill)
        btn9.grid(column=0,row=6)
        btn10 = Button(window,text='End fill',command=t.end_fill)
        btn10.grid(column=1,row=6)
        lbl5 = Label(window,text='Press start fill, draw a closed shape, and press end fill to fill.')
        lbl5.grid(column=2,row=6)
        txt4 = Entry(window,width=20)
        txt4.grid(column=0,row=7)
        btn11 = Button(window,text='go',command=changecolor,bg="green")
        btn11.grid(column=1,row=7)
        lbl6 = Label(window,text='Change the pen colour')
        lbl6.grid(column=2,row=7)
        txt5 = Entry(window,width=20)
        txt5.grid(column=0,row=8)
        btn12 = Button(window,text='go',command=changefill,bg="green")
        btn12.grid(column=1,row=8)
        lbl7 = Label(window,text='Change the fill colour')
        lbl7.grid(column=2,row=8)

        txt6 = Entry(window,width=10)
        txt6.grid(column=0,row=9)
        txt7 = Entry(window,width=10)
        txt7.grid(column=1,row=9)

        btn13 = Button(window,text='go',command=go_to,bg="green")
        btn13.grid(column=2,row=9)
        lbl8 = Label(window,text='Change draw to this location (x y)')
        lbl8.grid(column=3,row=9)

        txt8 = Entry(window,width=10)
        txt8.grid(column=0,row=10)
        btn14 = Button(window,text='go',command=pensize,bg="green")
        btn14.grid(column=1,row=10)
        lbl9 = Label(window,text='Change the pen size')
        lbl9.grid(column=2,row=10)

        txt9 = Entry(window,width=10)
        txt9.grid(column=0,row=11)
        btn15 = Button(window,text='go',command=dot,bg="green")
        btn15.grid(column=1,row=11)
        lbl10= Label(window,text='Draw a dot of this size')
        lbl10.grid(column=2,row=11)

        txt10 = Entry(window,width=20)
        txt10.grid(column=0,row=12)
        btn16 = Button(window,text='Save to file',command=save,bg="blue")
        btn16.grid(column=1,row=12)
        lbl11 = Label(window,text='Save image to the file of your choice .eps')
        lbl11.grid(column=2,row=12)
        btn18 = Button(window,text='Convert eps',command=conv)
        btn18.grid(column=3,row=12)
        txt11 = Entry(window,width=10)
        txt11.grid(column=0,row=13)
        btn19 = Button(window,text='Go',command=circ,bg="green")
        btn19.grid(column=1,row=13)
        lbl12 = Label(window,text='Draw a circle of this radius')
        lbl12.grid(column=2,row=13)

        txt12 = Entry(window,width=10)
        txt12.grid(column=0,row=14)
        btn20 = Button(window,text='Go',command=square,bg="green")
        btn20.grid(column=1,row=14)
        lbl13 = Label(window,text='Draw a square with a side length of this.')
        lbl13.grid(column=2,row=14)
        window.mainloop()

    elif command == "erc":
        print("-----List of Error Codes-----")
        print("error 0: Internal Error. You should usually not see this. Any message that does not have an error code is 0.")
        print("error 1: Conversion Error. This is the most common error, and is usually triggered by you entering letters into a place where only numbers go.")
        print("error 2: File Not Found Error. This is usually found when you rename or delete one of this program's files.")
        print("error 3: Script Error. This happens during the pyterm and calc commands. It is when you have an error in your script.")
        print("error 4: File Corrupt Error. This has yet to happen. If you find something like this, please report the bug.")
        print("error 5: Out Of Range. This happens when you input '13' into a month counter.")
        print("error 6: Invalid URL. This is what happens if you put an invalid url.")
        print("error 7: Turtle error")

    elif command == "sw":

        newwindow()
        print("Please look at the Tkinter window")
        def swkill():
            global window
            window.quit()
            window.destroy()
            global paused
            paused = True
        def swmain():
            global tcount
            global window
            global lbl
            global paused
            global btn
            global btn3
            global btn2
            window = Tk()
            window.title("Stopwatch")
            window.geometry("400x100")
            lbl = Label(window,text="0")
            lbl.grid(column=0,row=0)
            btn = Button(window,text="Start",command=swstart,bg="green")
            btn.grid(column=0,row=1)
            btn1 = Button(window,text="Pause",command=swstop,bg="yellow")
            btn1.grid(column=1,row=1)
            btn2 = Button(window,text="Stop",command=swkill,bg="red")
            btn2.grid(column=2,row=1)
            btn3 = Button(window,text='Reset',command=swreset,bg='blue')
            btn3.grid(column=3,row=1)
            window.mainloop()
            
            paused = True

        def swstart():
            global btn3
            global btn
            global btn2
            btn['state'] = "disabled"
            btn3['state'] = "disabled"
            btn2['state'] = "disabled"
            th0 = threading.Thread(target=swcount)
            th0.start()


        def swcount():
            global lbl
            global paused
            global tcount
            paused = False
            while paused == False:
                tcount = tcount + 0.1
                sleep(0.08)
                try:
                    lbl.configure(text=tcount)
                except:
                    pass

        def swstop():
            global paused
            global btn
            global btn3
            btn['state'] = "normal"
            btn3['state'] = 'normal'
            btn2['state'] = "normal"
            paused = True

        def swreset():
            global paused
            global tcount
            pasued = False
            tcount = 0
            try:
                lbl.configure(text=tcount)
            except:
                error(0)



        tcount = 0
        paused = False
        swmain()

    elif command == "quiz":
        print("Welcome to Multiplication Quiz! Press enter to begin!")
        input()
        isdone = False
        correct = 0
        wrong = 0
        cr = False
        def timer():
            global isdone
            global ttime
            ttime = 0
            while isdone == False:
                try:
                    sleep(1)
                    ttime = ttime + 1
                except:
                    break
        th = threading.Thread(target=timer)
        th.start()

        while correct < 10:
            n1 = random.randint(1,12)
            n2 = random.randint(1,12)
            answ = n1 * n2
            print("What is",n1,"x",n2,"?")
            sansw = input()
            try:
                sansw = int(sansw)
            except:
                print("Please put only numbers here.")
                cr = True
                wrong = wrong + 1
            if cr == False:
                if sansw == answ:
                    print("correct!")
                    correct = correct + 1
                else:
                    print("wrong.")
                    wrong = wrong + 1
        if correct > 9:
            isdone = True
        print("You did it in",ttime,"seconds!")
        if besttime == 0 or ttime < besttime:
            print("You have a new best time!")
            ttime = str(ttime)
            try:
                f = open("appdata.txt","x")
                f.write(ttime)
                f.close()
            except:
                ttime = ttime + "\n"
                f = open("appdata.txt","r")
                xr = f.readlines()
                xr[0] = ttime
                f = open("appdata.txt","w")
                f.writelines(xr)
                f.close()
        ot = correct + wrong
        print("You did",correct,"correct answers out of",ot)
        ote = correct / ot * 100
        print("Your score is",ote,"%")
    elif command == "calc help":
        print("-----Help With Calculator-----")
        print("This will help you with getting the correct operators")
        print("+: Addition, command usage: 1+1")
        print("-: Subtraction, command usage: 10-8")
        print("*: Multiplication, command usage: 10 * 5")
        print("/: Division, command usage: 10/2")
        print("%: Modulus, command usage: 10 % 3")
        print("**: Exponents, command usage: 10 ** 3")
        print("// Floor Division, command usage: 93 // 12")
        print("() Parentheses, used to execute some math first. Example: (12+6)/3")


    elif command == "calc":
        print("Please look at the tkinter window.")
        def calcu():
            global lbl1
            global txt
            res = txt.get()
            try:
                data = eval(res)
                print(data)
                lbl1.configure(text=data)
            except:
                lbl1.configure(text='error')
        cal = Tk()
        cal.title('Calculator')
        lbl = Label(cal,text='Please input full equation and press calculate')
        lbl.grid(column=0,row=0)
        btn = Button(cal,text='Close',command=cal.destroy,bg='red')
        btn.grid(column=1,row=0)
        txt = Entry(cal,width=50)
        txt.grid(column=0,row=1)
        btn1 = Button(cal,text='Calculate',command=calcu,bg='lime green')
        btn1.grid(column=1,row=1)
        lbl1 = Label(cal,text='')
        lbl1.grid(column=0,row=2)
        cal.mainloop()
        

    elif command == "lnmeter":
        newwindow()
        print('')
        if crashed == False:
            while True:
                x = datetime.datetime.now()
                a = x.year
                b = x.month
                c = x.day
                d = x.hour
                e = x.minute
                f = x.second
                d1 = datetime.datetime(a,b,c,d,e,f)
                d0 = datetime.datetime(2020,3,13,15,30,0)
                difference = d1 - d0
                total_seconds = difference.total_seconds()
                total_min = total_seconds / 60
                total_hr = total_min / 60
                total_dy = total_hr / 24
                total_wk = total_dy /7
                total_yr = total_dy / 365
                total_mt = total_yr * 12
                print("")
                print("There are",total_seconds,"seconds since")
                print("There are",total_min,"minutes since")
                print("There are",total_hr,"hours since")
                print("There are",total_dy,"days since")
                print("There are",total_wk,"weeks since")
                print("There are",total_mt,"month since")
                print("There are",total_yr,"years since life was normal.")
                sleep(1)

    elif command == "pyterm":
        crashed = False
        newwindow()
        print("")
        if crashed == False:
            print("Warning: This will give you access to most python commands. This could be dangerous. Make sure you know what you are doing!")
            print("type something in python and press enter. To return to the command menu, type 'breakout' and press enter")
            while True:
                cmd = input()
                if cmd == "breakout":
                    break
                try:
                    exec(cmd)
                except:
                    error(3)

    elif command == "gpap":
        print("GPA?")
        gpa = input()
        try:
            gpa = float(gpa)
        except:
            error(1)
        else:
            gpa = gpa + 1
            gpa = gpa * 20
            print("Percent =",gpa)

    elif command == "pgpa":
        print("percent?")
        prce = input()
        try:
            prce = float(prce)
        except:
            error(1)
        else:
            gpa = prce / 20 - 1
            print("GPA =",gpa)

    elif command == "pa":
        pa = True
        while pa == True:
            print("Starting number?")
            sn = input()
            try:
                sn = float(sn)
            except:
                error(1)
                break
            print("What percent do you want to add?")
            ap = input()
            try:
                ap = float(ap)
            except:
                error(1)
                break
            ap = ap / 100
            ax = ap * sn
            print("You  are adding",ax)
            tyi = ax + sn
            print("For a total of",tyi)
            pa = False

    elif command == "pr":
        pr = True
        while pr == True:
            print("Starting number?")
            sn = input()
            try:
                sn = float(sn)
            except:
                error(1)
                break
            print("What percent do you want to remove?")
            ap = input()
            try:
                ap = float(ap)
            except:
                error(1)
                break
            ap = ap / 100
            ax = ap * sn
            print("You  are removing",ax)
            tyi = sn - ax
            print("For a total of",tyi)
            pr = False

    elif command == "randpass":
        randpass = True
        while randpass == True:
            print("How many characters?")
            hmchar = input()
            hmchart = hmchar.isnumeric()
            if hmchart == False:
                error(1)
                break
            hmchar = int(hmchar)
            if hmchar > 24:
                print("Please only make passwords 24 characters or less. Your password will only be 24 long")
                hmchar = 24
                input("press eneter to generate the password of 24 characters.")
            letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            numbers = ["1","2","3","4","5","6","7","8","9","0"]
            symbols = ["!","@","#","$","%","^","&","*","'"]
            password = ["","","","","","","","","","","","","","","","","","","","","","","","",""]
            chgx = [0,0,1,2]
            characters = 0
            for i in range(hmchar):
                chgxy = random.choice(chgx)
                if chgxy == 0:
                    password[characters] = random.choice(letter)
                elif chgxy == 1:
                    password[characters] = random.choice(numbers)
                elif chgxy == 2:
                    password[characters] = random.choice(symbols)
                characters = characters + 1
            print("-----")
            qpo = 0
            for len in password:
                print(password[qpo])
                qpo = qpo + 1
                if password[qpo] == "":
                    break
            print("-----")
            print("This is the randomly generated password.")
            print("Do you want to write your password to a txt file?(y/n)")
            writetofile = input()
            if writetofile.lower().startswith('y'):
                print("What should the file containing the password be called?")
                print("example: myfile.txt")
                print("Make sure to include the .txt at the end, otherwise your file may be unreadable.")
                filesext = input()
                Tk().withdraw()
                filesname = filedialog.askdirectory()
                if filesname == '()':
                    break
                filesname = filesname + sysslash + filesext
                
                try:
                    f = open(filesname,"x")
                except:
                    print("This file already exists. Do you want to overwrite it?(y/n)")
                    overwrite = input()
                    if overwrite.lower().startswith('y'):
                        try:
                            f = open(filesname,"w")
                            print("writing to file 0%")
                            f.write(password[0])
                            f.write(password[1])
                            f.write(password[2])
                            f.write(password[3])
                            f.write(password[4])
                            f.write(password[5])
                            f.write(password[6])
                            f.write(password[7])
                            f.write(password[8])
                            f.write(password[9])
                            f.write(password[10])
                            f.write(password[11])
                            f.write(password[12])
                            print("writing to file 50%")
                            f.write(password[13])
                            f.write(password[14])
                            f.write(password[15])
                            f.write(password[16])
                            f.write(password[17])
                            f.write(password[18])
                            f.write(password[19])
                            f.write(password[20])
                            f.write(password[21])
                            f.write(password[22])
                            f.write(password[23])
                            f.write(password[24])
                            print("writing to file 100%")
                            f.close()
                            print("File overwritten successfully.")
                        except:
                            Tk().withdraw()
                            messagebox.showerror('Error','Access Denied')
                else:
                    print("Writing to file 0%")
                    f.write(password[0])
                    f.write(password[1])
                    f.write(password[2])
                    f.write(password[3])
                    f.write(password[4])
                    f.write(password[5])
                    f.write(password[6])
                    f.write(password[7])
                    f.write(password[8])
                    f.write(password[9])
                    f.write(password[10])
                    f.write(password[11])
                    f.write(password[12])
                    print("Writing to file 50%")
                    f.write(password[13])
                    f.write(password[14])
                    f.write(password[15])
                    f.write(password[16])
                    f.write(password[17])
                    f.write(password[18])
                    f.write(password[19])
                    f.write(password[20])
                    f.write(password[21])
                    f.write(password[22])
                    f.write(password[23])
                    f.write(password[24])
                    print("writing to file 100%")
                    f.close()
                    print("File written to",filesname,"successfully.")
                    
            randpass = False

    elif command == "apv":
        print("-----Subcommands for Area, Perimeter, Volume-----")
        print("apv rec: area and perimeter of a rectangle or square.")
        print("apv cir: area and perimeter of circle")
        print("apv tri: area of triangle")
        print("apv recp: volume of rectangular prism")
        print("apv trip: volume of triangular prism")
        print("apv cyl: volume of cylinder")
        print("apv sph: volume of sphere")

    elif command == "apv rec":
        apvrec = True
        while apvrec == True:
            print("base of rectangle?")
            base = input()
            try:
                base = float(base)
            except:
                error(1)
                break
            print("height of rectangle?")
            height = input()
            try:
                height = float(height)
            except:
                error(1)
                break
            area = base * height
            perimeter = base * 2 + height * 2
            print("The area is",area)
            print("The perimeter is",perimeter)
            apvrec = False

    elif command == "apv cir":
        apvcir = True
        while apvcir == True:
            print("Radius of circle?")
            radius = input()
            try:
                radius = float(radius)
            except:
                error(1)
                break
            diameter = radius * 2
            area = radius * radius * pi
            perimeter = diameter * pi
            print("Area is",area)
            print("Circumfrence is",perimeter)
            apvcir = False

    elif command == "apv tri":
        apvtri = True
        while apvtri == True:
            print("base of triangle?")
            base = input()
            try:
                base = float(base)
            except:
                error(1)
                break
            print("height of triangle?")
            height = input()
            try:
                height = float(height)
            except:
                error(1)
                break
            area = base * height / 2
            print("Area is",area)
            apvtri = False

    elif command == "apv recp":
        apvrecp = True
        while apvrecp == True:
            print("height?")
            height = input()
            try:
                height = float(height)
            except:
                error(1)
                break
            print("width?")
            width = input()
            try:
                width = float(width)
            except:
                error(1)
                break
            print("depth?")
            depth = input()
            try:
                depth = float(depth)
            except:
                error(1)
                break
            volume = height * width

            volume = volume * depth
            print("Volume is",volume)
            apvrecp = False

    elif command == "apv trip":
        apvtrip = True
        while apvtrip == True:
            print("height?")
            height = input()
            try:
                height = float(height)
            except:
                error(1)
                break
            print("width?")
            width = input()
            try:
                width = float(width)
            except:
                error(1)
                break
            print("depth?")
            depth = input()
            try:
                depth = float(depth)
            except:
                error(1)
                break
            volume = height * width

            volume = volume * depth
            volume = volume / 2
            print("Volume is",volume)
            apvtrip = False

    elif command == "apv cyl":
        apvcyl = True
        while apvcyl == True:
            print("radius?")
            radius = input()
            try:
                radius = float(radius)
            except:
                error(1)
                break
            print("length?")
            length = input()
            try:
                length = float(length)
            except:
                error(1)
                break
            volume = radius * radius
            volume = volume * pi
            volume = volume * length
            print("Volume is",volume)
            apvcyl = False

    elif command == "apv sph":
        apvsph = True
        while apvsph == True:
            print("Radius?")
            radius = input()
            try:
                radius = float(radius)
            except:
                error(1)
                break
            thingy = 4 / 3
            volume = radius * radius * radius
            volume = thingy * volume
            volume = volume * pi
            print("Volume is",volume)
            spvsph = False


    elif command == "contact":
        print("Email: enderbyte09@gmail.com")
        print("Discord: Enderbyte09#0542")

    elif command == "credits":
        print("Basic Utilities (c) 2021 Enderbyte Programs")
        print("Installer by Inno Setup")
        print("Coded in Python 3.7.3, 3.9.2, 3.9.6 and 3.9.5; compiled in Pyinstaller 4.2, 4.3, 4.4, 4.5.1")
        print("Written by Enderbyte09")
        print("With IDLE for 64-bit Windows")
        print("And notepad++")
        print("And Thonny IDE for Raspberry Pi 4")
        print('AND IDLE 3.7.3 for Raspberry Pi 4')
        print('And Visual Studio Code for Python 3.7.3 and 3.9.6')
        print("Game board pictures by Kdog.")
        print("Insults by Arceus007")
        
        print('Sound "Windows Xp Boot" from Instant Sounds')
        
        print('Sound "Windows 7 Boot" from [unknown]')
        print("Started on April 14, 2021")


    elif command == "prank":
        def prank():
            x = random.randint(1,4)
            if x == 1:
                webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
            elif x == 2:
                webbrowser.open("https://www.sketchywebsite.net")
            elif x == 3:
                webbrowser.open("https://geekprank.com/fake-virus/")
            elif x == 4:
                try:
                    winsound.Beep(1000,1000)
                except:
                    error(2)
        pr = Tk()
        pr.title("The Big Red Button")
        lbl9 = Label(pr,text='Go on. Click the Big Red Button.')
        lbl9.grid(column=0,row=0)
        brb = Button(pr,text='Click me',command=prank,bg="red")
        brb.grid(column=0,row=1)
        pr.mainloop()
    elif command == "stop":
        xae = False
        forcekill()
        break
    elif command == "stopall":
        try:
            os.system('taskkill /F /IM BasicUtilities.exe')
        except:
            error(2)
    elif command == "game":
        total_money = 500
        times_played = 0
        
        
        print("Welcome",sysuser,"to Enderbyte09's Beat th' Bank!")
        print("enter/return to continue.")
        input()
        print("You will have to open vault doors. You will gain money. However, there is a chance that you will open the ALARM, in which case you will get no money at all.")
        print("press enter/return to begin")
        print("It cost 100 to play.")
        input()
        if sysuser == 'Ruby' or sysuser == 'ruby':
            money = 10000000000000
            print('YOU WON A QUADRILLION DOLLARS')
            print('OHHHHHHHHHH')
        else:
            playagain = "y"
            possible = [10,25,50,75,100,150,200,300,"alarm","alarm"]
            while playagain == "y":
                total_money = total_money - 100
                money = 0
                vaults = 0
                alarm = False
                hasstopped = False
                while alarm == False and hasstopped == False:
                    print("do you want to open vault",vaults,"? (y/n)")
                    openvault = input()
                    if openvault.lower().startswith('y'):

                        moneyadd = random.choice(possible)
                        print("Vault",vaults,"has",moneyadd,"in it.")
                        print("")
                        vaults = vaults + 1
                        if moneyadd == "alarm":
                            alarm = True
                            try:
                                winsound.Beep(1000,1000)
                            except:
                                error(2)
                        elif alarm == False:
                            money = money + moneyadd
                    print("You have",money,"dollars")
                    if openvault == "n":
                        hasstopped = True
                if alarm ==  True:
                    money = 0
                print("You finished with",money,"money!")
                sleep(1)
                total_money = total_money + money
                times_played = times_played + 1
                print("Thank you for participating in Beat The Bank!")
                sleep(1)
                answered = False
                while answered == False:
                    print("Would you like to see your total statistics?[y/n]")
                    statsee = input()
                    if statsee.lower().startswith('y'):
                        answered = True
                        print("You have played",times_played,"games")
                        print("You have a total of",total_money,"money.")
                    elif statsee == "n":
                        answered = True
                        print("If you say so")
                print("do you want to play again? (y/n)")
                print("Typing n returns you to the commands menu.")
                playagain = input()
                if playagain.lower().startswith('y'):
                    playagain = 'y'
                    for i in range(1,20):
                        print("")
                    print("Do you want to change name? (y/n)")
                    changename = input()
                    if changename.lower().startswith('y'):
                        print("Please type your new name")
                        name = input()
                        print("Welcome,",name,"to Enderbyte09's Beat The Bank!")
                        for i in range(1,20):
                            print("")
                else:
                    playagain = 'n'
    elif command == "insult":
        adjec = ["Loggerheaded","Beefwitted","Cream-faced","","Stupid","Imbecilic","Rank","Gassy","Pork-witted","Zombified","Gelatin-bottomed","Picklebrained","@$%&TYFt767tT*^TT*%%RFft*^((%^$4&^^4"]
        noun = ["Applejohn","Loon","Creamface","Beefwit","Porkwit","Dummy","Lunatic","Idiot","Yellwe","Monkeybottom","Clackdish","Jellyfish","^%*yuygg&yguguyTUGUT87t83t868%&&^^&*^&*"]
        adjec1 = random.choice(adjec)
        adjec2 = random.choice(adjec)
        noun1 = random.choice(noun)
        filler = "Thou art a"
        same = True
        while same == True:
            if adjec1 == adjec2:
                adjec2= random.choice(adjec)
            else:
                break
        exc = "!"
        nothing = False
        if adjec1 == "" or adjec2 == "":
            nothing = True
        print('')
        if nothing == False:
            adjec1 = adjec1 + ","
        noun1 = noun1 + exc
        print("-----")
        print(filler,adjec1,adjec2,noun1)
        print("-----")

    elif command == "reload":
        reload()

    elif command == "meter":
        newwindow()
        while True:
            x = datetime.datetime.now()
            a = x.year
            b = x.month
            c = x.day
            d = x.hour
            e = x.minute
            f = x.second
            d1 = datetime.date(a,b,c)
            d0 = datetime.date(2019,12,30)
            delta = d1 - d0
            daysy = delta.days
            second = daysy * 24
            second = second + d
            second = second * 60
            second = second + e
            second = second * 60
            second = second + f
            minutes = second / 60
            hour = minutes / 60
            days = hour / 24
            weeks = days / 7
            years = days /365
            months = years * 12
            print("It has been",years,"years")
            print("It has been",months,"months")
            print("It has been",weeks,"weeks")
            print("It has been",days,"days")
            print("It has been",hour,"hours")
            print("It has been",minutes,"minutes")
            print("It has been",second,"seconds since COVID-19 infected its first human")
            print("")
            sleep(1)

    elif command == "browser":
        try:
            f = open('history.txt')
            data = f.read()
        except:
            f = open('history.txt','x')
            data = 'No History Yet'
            f.write(data)
        finally:
            f.close()
        def gourl():
            global txt
            global res
            res = txt.get()
            webbrowser.open(res)
            writehistory()
        def sech():
            global txt
            global res
            res = txt.get()
            res = 'https://www.google.com/search?q='+res
            webbrowser.open(res)
            writehistory()
        def sechb():
            global txt
            global res
            res = txt.get()
            res = 'https://www.bing.com/search?q='+res
            webbrowser.open(res)
            writehistory()
        def sechy():
            global txt
            global res
            res = txt.get()
            res = 'https://www.yahoo.com/search?p='+res
            webbrowser.open(res)
            writehistory()
        def sechw():
            global txt
            global res
            res = txt.get()
            res = 'https://en.wikipedia.org/w/index.php?search='+res
            webbrowser.open(res)
            writehistory()
        def sechyo():
            global txt
            global res
            res = txt.get()
            res = 'https://www.youtube.com/results?search_query='+res
            webbrowser.open(res)
            writehistory()
        def vh():
            global data
            if data == 'No History Yet':
                Tk().withdraw()
                messagebox.showinfo('','No History Yet')
            else:
                webbrowser.open(data)
        def writehistory():
            global res
            global lbl1
            try:
                f = open('history.txt','w')
                f.write(res)
                f.close()
            except:
                f = open('history.txt','w')
                f.write(res)
                f.close()
            lbl1.configure(text=res)
        def ddie():
             wbx.destroy()
             wbx.quit()
        wbx = Tk()
        wbx.title('BU Browser')
        
        lbl = Label(wbx,text='Put your URL or search here')
        lbl.grid(column=0,row=0)
        btn = Button(wbx,text='Close',bg='yellow',command=ddie)
        btn.grid(column=1,row=0)
        txt = Entry(wbx,width=50)
        txt.grid(column=0,row=1)
        btn1 = Button(wbx,text='Go to URL',command=gourl,bg='lime green')
        btn1.grid(column=0,row=2)
        btn2 = Button(wbx,text='Search with Google',command=sech,bg='lime green')
        btn2.grid(column=1,row=2)
        btn5 = Button(wbx,text='Bing',command=sechb,bg='lime green')
        btn5.grid(column=2,row=2)
        btn4 = Button(wbx,text='Yahoo',command=sechy,bg='lime green')
        btn4.grid(column=3,row=2)
        btn5 = Button(wbx,text='Wikipedia',command=sechw,bg='lime green')
        btn5.grid(column=4,row=2)
        btn6 = Button(wbx,text='Youtube',command=sechyo,bg='lime green')
        btn6.grid(column=5,row=2)
        lbl1 = Label(wbx,text=data)
        lbl1.grid(column=0,row=3)
        btn3 = Button(wbx,text='Go to recent search',bg='SkyBlue1',command=vh)
        btn3.grid(column=1,row=3)
        wbx.mainloop()

    elif command == "logoff":
        os.system('shutdown /l')
    elif command == "restart":
        os.system('shutdown /r /t 0')

    elif command == "rng":
        afghs = True
        while afghs == True:
            print("Lowest number?")
            botrand = input()
            u = botrand.isnumeric()
            if u == False:
                error(1)
                break

            botrand = int(botrand)
            print("Highest number?")
            toprand = input()
            w = toprand.isnumeric()
            if w == False:
                error(1)
                break
            toprand = int(toprand)
            randhj = random.randint(botrand,toprand)
            print("-----")
            print(randhj)
            print("-----")
            afghs = False
    elif command == "cf":
        cf = ("heads","tails")
        cfe = random.choice(cf)
        print("-----")
        print(cfe)
        print("-----")
    elif command == "alarm":
        ajh = True
        while ajh == True:
            newwindow()
            print("What year for alarm?")
            g = input()
            m = g.isnumeric()
            if m == False:
                error(1)
                break
            g = int(g)
            print("Month?")
            h = input()
            n = h.isnumeric()
            if n == False:
                error(1)
                break
            h = int(h)
            if h < 1 or h > 12:
                error(5)
                break
            print("Day?")
            i = input()
            nom3 = i.isnumeric()
            if nom3 == False:
                error(1)
                break
            i = int(i)
            if h > 31:
                error(5)
                break
            print("Hour?")
            j = input()
            nom4 = j.isnumeric()
            if nom4 == False:
                error(1)
                break
            j = int(j)
            if j > 23:
                error(5)
                break
            print("Minute?")
            k = input()
            nom5 = k.isnumeric()
            if nom5 == False:
                error(1)
                break
            k = int(k)
            if k > 59:
                error(5)
                break
            print("Second?")
            l = input()
            nom6 = l.isnumeric()
            if nom6 == False:
                error(1)
                break
            l = int(l)
            if l > 59:
                error(5)
                break
            print("Alarm will ring at",g,"-",h,"-",i,"at",j,":",k,":",l)
            isdone = False
            while isdone == False:
                x = datetime.datetime.now()
                a = x.year
                b = x.month
                c = x.day
                d = x.hour
                e = x.minute
                f = x.second
                d0 = datetime.datetime(a,b,c,d,e,f)
                try:
                    d1 = datetime.datetime(g,h,i,j,k,l)
                except:
                    error(5)
                    crashed = True
                    break
                difference = d1 - d0
                total_seconds = difference.total_seconds()
                total_min = total_seconds / 60
                total_hr = total_min / 60
                total_dy = total_hr / 24
                total_wk = total_dy /7
                total_yr = total_dy / 365
                total_mt = total_yr * 12
                print("")
                print("There are",total_seconds,"seconds left")
                print("There are",total_min,"minutes left")
                print("There are",total_hr,"hours left")
                print("There are",total_dy,"days left")
                print("There are",total_wk,"weeks left")
                print("There are",total_mt,"month left")
                print("There are",total_yr,"years left")
                if d0 == d1 or d0 > d1:
                    isdone = True
                sleep(1)
            if crashed == True:
                break
            print("Your timer is done")
            asdfgh = True
            while asdfgh == True:
                try:
                    winsound.Beep(1000,1000)
                    asdfgh = False
                except:
                    error(2)
                    crashed = True
                    asdfgh = False
                    break

            for i in range(1,5):
                if crashed == False:
                    winsound.Beep(1000,1000)
            ajh = False
    elif command == "clock":
        x = datetime.datetime.now()
        print(x)
    elif command == "counter":
        tgy = True
        while tgy == True:
            newwindow()
            print("counting year?")
            g = input()
            m = g.isnumeric()
            if m == False:
                error(1)
                break
            g = int(g)
            print("Month?")
            h = input()
            yu = h.isnumeric()
            if yu == False:
                error(1)
                break
            h = int(h)
            if h > 12:
                error(5)
                break
            print("Day")
            i = input()
            fh = i.isnumeric()
            if fh == False:
                error(1)
                break
            i = int(i)
            if i > 31:
                error(5)
                break
            print("Hour?")
            j = input()
            yt = j.isnumeric()
            if yt == False:
                error(1)
                break
            j = int(j)
            if j > 23:
                error(5)
                break
            print("Minute?")
            k = input()
            er = k.isnumeric()
            if er == False:
                error(1)
                break
            k = int(k)
            if k > 59:
                error(5)
                break
            print("Second?")
            l = input()
            xie = l.isnumeric()
            if xie == False:
                error(1)
                break
            l = int(l)
            if l > 59:
                error(5)
                break
            zxcv = True
            while zxcv == True:
                x = datetime.datetime.now()
                a = x.year
                b = x.month
                c = x.day
                d = x.hour
                e = x.minute
                f = x.second
                d0 = datetime.datetime(a,b,c,d,e,f)
                try:
                    d1 = datetime.datetime(g,h,i,j,k,l)
                except:
                    error(5)
                    crashed = True
                    tgy = False
                    break

                difference = d0 - d1
                total_seconds = difference.total_seconds()
                total_min = total_seconds / 60
                total_hr = total_min / 60
                total_dy = total_hr / 24
                total_wk = total_dy /7
                total_yr = total_dy / 365
                total_mt = total_yr * 12
                print("")
                print("There are",total_seconds,"seconds since")
                print("There are",total_min,"minutes since")
                print("There are",total_hr,"hours since")
                print("There are",total_dy,"days since")
                print("There are",total_wk,"weeks since")
                print("There are",total_mt,"month since")
                print("There are",total_yr,"years since")
                sleep(1)
            if crashed == True:
                break

    elif command == "lag":
        qwe = datetime.datetime.now()
        qwer = qwe.second
        nogo = False
        if qwer > 55:
            print(":(")
            print("Please try this after the minute rolls over in less than 5 seconds.")
            nogo = True
        if nogo == False:
            newwindow()
            averagelag = 0
            tavglag = 0
            tlagcount = 0
            lagcount = 0
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            turtle.title("Lag Graph")
            t.speed(0)
            t.penup()
            t.goto(-300,-100)
            t.pendown()
            t.goto(300,-100)
            t.penup()
            t.goto(-300,-100)
            t.pendown()
            t.pencolor("red")
            lnp = t.pos()
            lanp = t.pos()
            tlan = t.pos()
            noscreen = False
            ttotal = 0
            qwe = datetime.datetime.now()
            while True:

                
                qwer = qwe.second
                if qwer > 57:
                    sleep(3)
                    qwe = datetime.datetime.now()
                    qwer = qwe.second
                fa = qwe.strftime('%S.%f')[:-3]
                fa = float(fa)
                lagcount = lagcount + 1
                tlagcount += 1
                tims = 0
                sleep(1)
                tims = 1
                qwert = datetime.datetime.now()
                ft = qwert.strftime('%S.%f')[:-3]
                ft = float(ft)
                lag = ft - fa
                lag = lag - tims
                lag = lag * 1000
                averagelag = averagelag + lag
                avglag = averagelag / lagcount
                tavglag += lag
                xavglag = tavglag / tlagcount
                
                try:
                    if noscreen == False:
                        tlag = lag - 100
                        talag = avglag - 100
                        tlg = xavglag - 100
                        ttotal = ttotal + 10
                        tgotototal = ttotal - 300
                        t.goto(tgotototal,tlag)
                        lnp = t.pos()
                        t.penup()
                        t.pencolor("green")
                        t.goto(lanp[0],lanp[1])
                        t.pendown()
                        t.goto(tgotototal,talag)
                        lanp = t.pos()
                        t.penup()
                        t.pencolor('blue')
                        t.goto(tlan[0],tlan[1])
                        t.pendown()
                        t.goto(tgotototal,tlg)
                        tlan = t.pos()
                        t.penup()
                        t.pencolor('red')
                        t.goto(lnp[0],lnp[1])
                        t.pendown()
                        if tgotototal > 300:
                            t.pencolor("red")
                            t.clear()
                            ttotal = 0
                            t.penup()
                            t.goto(-300,-100)
                            t.pendown()
                            t.pencolor("black")
                            t.goto(300,-100)
                            t.penup()
                            t.goto(-300,-100)
                            t.pendown()
                            t.pencolor("red")
                            lnp = (-300,-100)
                            lanp = (-300,-100)
                            tlan = lnp
                            averagelag = 0
                            lagcount = 0
                            
                except:
                    xsgued = 0
                qwe = datetime.datetime.now()
                
                print("your computer is lagging by",lag,"milliseconds")
                print("Your moving average.60 computer lag is",avglag,"milliseconds")
                print("Your all-time average computer lag is",xavglag,"milliseconds")
                print("")
                

    elif command == "avg":
        nums = 0
        total = 0
        avg = 0
        crashed = False
        isdone = False
        while isdone == False:
            print("Do you want to add a data value (y/n)")
            adddata = input()
            if adddata.lower().startswith('y'):
                print("Please put the value.")
                addnum = input()
                try:
                    addnum = float(addnum)
                except:
                    print("No, NO NO NO!")
                    print("How many times do we have to tell you that you")
                    print("DON'T PUT LETTERS HERE!?!?!?!?!?")
                    print("Please wait while we sort out your TERRIBLE ERROR")
                    print("You will be punished for your INSOLENCE")
                    print("Your average will not work right this time, because YOU decided to input a STRING in a place where only INTEGERS or FLOATS are allowed.")
                    print("If I was you, I'd go back to the command menu and start again")
                    sleep(3)
                    crashed = True
                if crashed == False:
                    nums = nums + addnum

                    total = total + 1
            elif adddata == "n":
                isdone = True
        if crashed == False:

            try:
                avg = nums / total
                print("Your average is",avg)
                print("")
            except:
                print("DON'T DIVIDE BY 0, YOU JERK.")

        else:
            print("Because YOU messed up, YOU have to start OVER AGAIN.")

    elif command == "m8b":
        paty = ("Yes","It is certain","Outlook Good","No","Not a chance","My sources say no","Concentrate and ask again","BasicUtilities.exe has stopped working. Please try again later.")
        print("What do you want to ask The Magic 8 ball?")
        qutchten = input()
        answty = random.choice(paty)
        print("-----")
        print(answty)
        print("-----")

    elif command == "snl":
        print("Subcommands for snl:")
        print("snl manual: Play snakes and ladders")
        print("snl bot: Have a bot play Snakes and Ladders for you. Does not count for points.")
        print("snl stats: View your snakes and ladders statistics.")
        print("-Exiting to the command menu does not lose your statistics, however, closing this program will.-")

    elif command == "snl manual":
        names = ("Jim","Bob","Joe","Jeff","George","Sally","Emily","Doge","Tim","Bottomhead","Ruby")
        opponent = random.choice(names)
        print("Your opponent is",opponent,"!")
        square = 0
        opponent_square = 0
        print("Do you want to see the game board? (y/n)")
        seeboard = input()
        if seeboard.lower().startswith('y'):
            awrt = True
            while awrt == True:
                try:
                    webbrowser.open('https://imgur.com/a/CwzPDsB')
                except:
                    print("Oh no! Something went wrong!")
                    
                    print("")
                    sleep(1)
                    break
                finally:
                    break
        while square < 100 and opponent_square < 100:
            print("")
            print("It is your turn! Press enter to roll the dice!")
            input()
            diceroll = random.randint(1,6)
            print("you rolled a",diceroll,"!")
            square = square + diceroll
            sleep(1)
            print("You landed on square",square)
            print("")
            if square == 3:
                print("You landed on a ladder square!")
                square = 35
                sleep(1)
                print("You climbed to square",square)
            elif square == 15:
                print("You landed on a secret ladder square!")
                square = 65
                sleep(1)
                print("You climbed to square",square)
            elif square == 23:
                print("You landed on a secret snake square!")
                square = 2
                sleep(1)
                print("You slid to square",square)
            elif square == 29:
                print("You landed on a ladder square!")
                square = 71
                sleep(1)
                print("You climbed to square",square)
            elif square == 54:
                print("You landed on a ladder square!")
                square = 84
                sleep(1)
                print("You climbed to square",square)
            elif square == 63:
                print("You landed on a snake square!")
                square = 22
                sleep(1)
                print("You slid to square",square)
            elif square == 78:
                print("You landed on a snake square!")
                square = 36
                sleep(1)
                print("You slid to square",square)
            elif square == 80:
                print("You landed on a ladder square!")
                square = 100
                sleep(1)
                print("You climbed to square",square)
            elif square == 89:
                print("You landed on a snake square!")
                square = 72
                sleep(1)
                print("You slid to square",square)
            elif square == 94:
                print("You landed on a snake square!")
                square = 27
                sleep(1)
                print("You slid to square",square)
            elif square == 99:
                print("You landed on a snake square!")
                square = 21
                sleep(1)
                print("You slid to square",square)
            if square > 99:
                break
            print("It is now",opponent,"'s turn!")
            opponent_diceroll = random.randint(1,6)
            sleep(1)
            print(opponent,"rolled a",opponent_diceroll)
            opponent_square = opponent_square + opponent_diceroll
            sleep(1)
            #todo 1.8 pre-3 fix this
            print(opponent,"landed on square",opponent_square)
            if opponent_square == 3:
                print(opponent,"landed on a ladder square!")
                opponent_square = 35
                sleep(1)
                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 15:
                print(opponent,"landed on a secret ladder square!")
                opponent_square = 65
                sleep(1)
                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 23:
                print(opponent," landed on a secret snake square!")
                opponent_square = 2
                sleep(1)
                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 29:
                print(opponent,"landed on a ladder square!")
                opponent_square = 71
                sleep(1)
                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 54:
                print(opponent,"landed on a ladder square!")
                opponent_square = 84
                sleep(1)
                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 63:
                print(opponent,"landed on a snake square!")
                opponent_square = 22
                sleep(1)
                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 78:
                print(opponent,"landed on a snake square!")
                opponent_square = 36
                sleep(1)
                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 80:
                print(opponent,"landed on a ladder square!")
                opponent_square = 100
                sleep(1)
                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 89:
                print(opponent,"landed on a snake square!")
                opponent_square = 72
                sleep(1)
                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 94:
                print(opponent,"landed on a snake square!")
                opponent_square = 27
                sleep(1)
                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 99:
                print(opponent,"landed on a snake square!")
                opponent_square = 21
                sleep(1)
                print(opponent,"slid to square",opponent_square)
        if square > 99:
            print("You Won!")
            gamees_won = gamees_won + 1
        if opponent_square > 99:
            print(opponent,"won!")
        gamees_played = gamees_played + 1
    elif command == "snl stats":
        print("-----Snakes And Ladders Statistics-----")
        print("You have played",gamees_played,"games!")
        print("You have won",gamees_won,"games!")

    elif command == "snl bot":
        names = ("Jim","Bob","Joe","Jeff","George","Sally","Emily","Doge","Tim","Bottomhead","Ruby")
        opponent = random.choice(names)
        print("Your opponent is",opponent,"!")
        square = 0
        opponent_square = 0
        print("Do you want to see the game board? (y/n)")
        seeboard = input()
        if seeboard.lower().startswith('y'):
            awrt = True
            while awrt == True:
                try:
                    webbrowser.open('https://imgur.com/a/CwzPDsB')
                except:
                    error(2)
                    break
                finally:
                    break
        while square < 100 and opponent_square < 100:
            print("It is your turn!")

            diceroll = random.randint(1,6)
            print("you rolled a",diceroll,"!")
            square = square + diceroll

            print("You landed on square",square)
            print("")
            if square == 3:
                print("You landed on a ladder square!")
                square = 35

                print("You climbed to square",square)
            elif square == 15:
                print("You landed on a secret ladder square!")
                square = 65

                print("You climbed to square",square)
            elif square == 23:
                print("You landed on a secret snake square!")
                square = 2

                print("You slid to square",square)
            elif square == 29:
                print("You landed on a ladder square!")
                square = 71

                print("You climbed to square",square)
            elif square == 54:
                print("You landed on a ladder square!")
                square = 84

                print("You climbed to square",square)
            elif square == 63:
                print("You landed on a snake square!")
                square = 22

                print("You slid to square",square)
            elif square == 78:
                print("You landed on a snake square!")
                square = 36

                print("You slid to square",square)
            elif square == 80:
                print("You landed on a ladder square!")
                square = 100

                print("You climbed to square",square)
            elif square == 89:
                print("You landed on a snake square!")
                square = 72

                print("You slid to square",square)
            elif square == 94:
                print("You landed on a snake square!")
                square = 27

                print("You slid to square",square)
            elif square == 99:
                print("You landed on a snake square!")
                square = 21

                print("You slid to square",square)
            if square > 99:
                break
            print("It is now",opponent,"'s turn!")
            opponent_diceroll = random.randint(1,6)

            print(opponent,"rolled a",opponent_diceroll)
            opponent_square = opponent_square + opponent_diceroll

            #todo 1.8 fix this
            print(opponent,"landed on square",opponent_square)
            if opponent_square == 3:
                print(opponent,"landed on a ladder square!")
                opponent_square = 35

                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 15:
                print(opponent,"landed on a secret ladder square!")
                opponent_square = 65

                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 23:
                print(opponent," landed on a secret snake square!")
                opponent_square = 2

                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 29:
                print(opponent,"landed on a ladder square!")
                opponent_square = 71

                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 54:
                print(opponent,"landed on a ladder square!")
                opponent_square = 84

                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 63:
                print(opponent,"landed on a snake square!")
                opponent_square = 22

                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 78:
                print(opponent,"landed on a snake square!")
                opponent_square = 36

                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 80:
                print(opponent,"landed on a ladder square!")
                opponent_square = 100

                print(opponent,"climbed to square",opponent_square)
            elif opponent_square == 89:
                print(opponent,"landed on a snake square!")
                opponent_square = 72

                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 94:
                print(opponent,"landed on a snake square!")
                opponent_square = 27

                print(opponent,"slid to square",opponent_square)
            elif opponent_square == 99:
                print(opponent,"landed on a snake square!")
                opponent_square = 21

                print(opponent,"slid to square",opponent_square)
        if square > 99:
            print("You Won!")

        if opponent_square > 99:
            print(opponent,"won!")

    else:

        print('Warning: You typed an unrecognized command. If you want to see the commands list, dismiss this message and run the command "help" or "?".')

        #Whew! That's a lot of code!
#Wait! There is more!
    cmd_run = cmd_run + 1
    try:
        f = open('notifs.txt','r')
        xlm = f.read()
    except:
        f = open('notifs.txt','x')
        f.write('1')
        xlm = '1'
    xmls = str(cmd_run)
    if xlm == '0':
        pqie = 2009
    elif xlm == '1':
        print('')
        print('You have run',cmd_run,'commands this session')
    elif xlm == '2':


        xls = 'You have run this many commands this session: ' + xmls + ". If you don't want messagebox notifs, change this with the notifs command."
        Tk().withdraw()
        messagebox.showinfo('Analytics Reporter',xls)
    else:
        f = open('notifs.txt','w')
        f.write('1')
        
        xls = 'You have run this many commands this session: ' + xmls + ". If you don't want messagebox notifs, change this with the notifs command."
        print('')
        print(xls)
    f.close()
#NOW were done        
