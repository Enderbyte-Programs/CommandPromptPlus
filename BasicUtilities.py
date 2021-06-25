print('Basic Utilities 2.6.1 (c) 2021 Enderbyte Programs. All rights reserved.')
print('')
print('preparing libraries ...',end='\r')
from tkinter import messagebox
try:
    import winsound
except:
   messagebox.showwarning('Error','Your device does not support Winsound. Some features may be broken.') 
import os
import webbrowser
import random
from time import sleep
import datetime
try:
    from playsound import playsound
except:
    messagebox.showwarning('Warning','Your device does not support playsound. Some features may be broken')
import turtle
import threading
from tkinter import *
import sys

print("preparing libraries ... done")
print('Assigning variables ...',end='\r')
sw = False
gamees_played = 0
gamees_won = 0
pi = 3.14
hasarg = True
try:
    arguments = sys.argv
    openfile_dir = arguments[1]
except:
    hasarg= False
xae = True
tcrash = False
cmd_run = 0
print('Assigning variables ...done',end='\n')
print('Writing appdata files ...',end='\r')
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
    f = open("appdata.txt","x")
    f.write("0")
    besttime = 0
    f.close()
finally:
    try:
        f.close()
    except:
        ggggggggg = False
print('Writing Appdata files ... done',end='\n')
print('preparing functions ...',end='\r')
def error(erc):
    erc = str(erc)
    erm = "An error has occured. Error code "
    erm = erm + erc
    messagebox.showerror("Error",erm)

def nwstart():
    global nw
    try:
        os.startfile('BasicUtilities.exe')
    except:
        error(2)
    finally:
        nw.destroy()

def newwindow():
    global nw
    print("Please look at the tkinter window.")
    nw = Tk()
    nw.title("New Window Starter")
    nw.geometry("800x50")
    lbl = Label(nw,text='Do you want to start a new window of BasicUtilities before you run this long/infinite command?')
    lbl.grid(column=0,row=0)
    btn322 = Button(nw,text='Yes',command=nwstart,bg="green")
    btn322.grid(column=0,row=1)
    btn323 = Button(nw,text='No',command=nw.destroy,bg="red")
    btn323.grid(column=1,row=1)
    nw.mainloop()
    nw.quit()

def conv(start,end,formula):
    print("how many",start,"?")
    a = input()
    try:
        a = float(a)
    except:
        error(1)
    else:
        b = a
        a = str(a)
        formula = str(formula)
        equation = a + " " + formula
        c = eval(equation)
        print(b,start,"is",c,end)
def reload():
    try:
        os.startfile("BasicUtilities.exe")
    except:
        error(2)
    else:
        sys.exit()
def startsound():
    try:
        playsound('startup.mp3')
    except:
        print('',end='\r')
        
def runfile(filename):
    try:
        os.startfile(filename)
    except:
        error(2)

print('preparing functions ... done',end='\n')
print('Reading appdata files...',end='\r')
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
print('reading appdata files ... done',end='\n')
print('Scanning dates ...',end='\r')
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
#Couldn't find any more fixed-date holidays that are recognized globally.
print('Scanning dates ... done',end='\n')
ss_po = threading.Thread(target=startsound)
ss_po.start()
if hasarg == True:
    try:
        f = open(openfile_dir,'r')
        mes = f.read()
        print('')
        print("encoded message is",len(mes),"bytes")
    except:
        error(0)
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
        print("What should the fle name be? (no extension needed)")
        fex = input()
        fex = fex + '.txt'
        try:
            f = open(fex,'x')
            f.write(tra)
            f.close()
            print("written to",fex)
        except:
            f = open(fex,'w')
            f.write(tra)
            f.close()
            print("written to",fex)
    print('Press enter to quit program.')
    input()
    sys.exit()
print('')
print("Welcome to BasicUtilities")

while xae == True:
    crashed = False
    print("")
    print("-----Command Menu-----")
    print("Type your command under here and press enter")
    command = input()
    if command == "help" or command == "?":
        print("-----Commands List-----")
        print("help: Shows this list")
        print("stop: Stops this window")
        print("stopall: stops all BasicUtilities windows")
        print("game: Play Beat The Bank")
        print("reload: reloads this program.")
        print("insult: Get insulted")
        print("meter: See how long it has been since COVID infected its first human.(VE COUNTER)")
        print("lnmeter: How long since life was normal?")
        print("logoff: Logs you out.")
        print("restart: Restarts your computer")
        print("web: Open a website.")
        print("alarm: Open the alarm clock")
        print("clock: Tells you the exact time")
        print("counter: make a counter")
        print("rng: Random Number Generator")
        print("cf: Coin Flip")
        print("lag: Measures your computer's lag.")
        print("anim: Get a little animation of a wheel.")
        print("avg: Get an average calculator")
        print("prank: try it out :P")
        print("erc: List of error codes")
        print("m8b: Magic 8 ball")
        print("snl: Play Snakes and Ladders [sc]")
        print("credits: View credits and statistics")
        print("contact: Get my email and Discord")
        print("randpass: Get a random password.")
        print("apv: area, perimeter, and volume calculator [sc]")
        print("pa: Add percent")
        print("pr: Remove percent")
        print("pgpa: Percent to GPA")
        print("gpap: GPA to percent")
        print("pyterm: Open a python terminal prompt [potentially dangerous]")
        print("calc help: Help with the calculator")
        print("calc: Calculator")
        print("quiz: get a multiplication quiz up to 12x12")
        print("sw: Stop watch!")
        print("draw: Draw with Turtle!")
        print("timer: Pauseable Timer")
        print("conv: converters [sc]")
        print("wb: Visit our website")
        print("uninstall: Uninstall this program completely")
        print("pre-uninstall: Get rid of the files that the uninstall can't uninstall. This will destroy appdata.txt and saved drawings still in this directory.")
        print("cpg: Play the Cartesian Plane Game")
        print("colour: Find a colour")
        print("bday: Input your birthday to get a surprise on startup when it matches")
        print("encode: encode stuff so no one can read it")
        print("translate: Translate files back to readable")
        print('notifs: Change your commmand-running notification settings.')
        print('crash: Crash this program')
        print('progcount: How long since this program existed')
        print('picker: Make a custom random generator')
        print('cpicker: Random colour picker')
        print('tempt: Temperature converter')
        print('degp: degrees to percent')
        print('pdeg: percent to degrees')
        print('cl: view the changelog')
        print('ls: View the license')
        print('ae: Addiional information and uninstalling help')
        print('game2: Play Discount Prodigy (NOT YET FINISHED)')
        #^Under development, release in 2.6 or 2.7
        print('beep: Get a beep')
        print('curse: Have this program curse at you (no actual cursing)')
        print('hex: Random Hexadecimal Generator (x16)')
        print('hexbi: Random hexadecabinary generator (x62 system)')
        print("There are also some easter egg commands :)")

    elif command == 'hex':
        print(random.choice([0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']))
    elif command == 'hexbi':
        print(random.choice([0,1,2,3,4,5,6,7,8,9,'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']))

    elif command == 'curse':
        for i in range(random.randint(1,10)):
            winsound.Beep(1000,random.randint(200,1500))
            print(random.randint(1,10)*'*')
            sleep(random.randint(1,10)/10)
            

    elif command == 'beep':
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
    elif command == 'game2':
        messagebox.showinfo('','This game is currently under development. It may cause unwanted effects if you continue.')
        print('What is your Username?')
        username = input()
        print('Welcome',username,'to Discount Prodigy')
        print('Discount prodigy is a game where you cast spells against monsters.')
        print('To cast spells, you must answer simple math problems')
        print('As you cast spells, you earn points.')
        print('Press enter to begin.')
        input()
        fightmonsters = True
        monster_names = ['Black Widow','Wulf','Slayer','Shredder','Magma','Tsunahmee']
        monsters_battled = 0
        monsters_won = 0
        monsters_lost = 0
        xp = 0
        health = 100
        while fightmonsters == True:
            print('A monster wants to battle you! do you want to battle?(y/n)')
            battle = input()
            if battle == 'y':
                monsterbattle_name = random.choice(monster_names)
                monster_health = health/(random.randint(12,24)/10)
                print('Your enemy is',monsterbattle_name)
                print(monsterbattle_name,'has',monster_health,'health')
                print('press enter to continue')
                input()
                if monsterbattle_name == 'Black Widow':
                    monster_spells = ['Poke','Venom']
    elif command == 'cl':
        runfile('changelog.txt')
    elif command == 'ls':
        runfile('license.txt')
    elif command == 'ae':
        runfile('notes.txt')
        
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
                        messagebox.showwarning('Warning','Invalid Command Combination')
            else:
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
            if makenew == 'y':
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
        for i in range(30):
            print('')
        print('.  //')
        print('  ||')
        print('.  \\')
        print('')
        print('A critical system failure has occured.')
        print('If this is the first time that you have seen this screen, restart.')
        print('If this problem persists, reinstall.')
        print('')
        print('Techincal Information:')
        print('')
        print('Error code 0x00000129c (0x00000000a,0x00000011p,0x0_)')
        print('Stop: Manually_Initiated_Crash')
        print('')
        print('press enter to continue to restart')
        input()
        try:
            os.startfile('BasicUtilities.exe')

        except:
            print('Exception: Most recent Callback')
            print('Error in line 414 of BasicUtilities.py')
            print('try:')
            print("     os.startfile('BasicUtilites.exe')")
            print('[ERRNO] 17')
            print('')
            print('During the handling of the above exception, another exception occured')
            print('')
            print('Error in line @#*(@^* of &(@#&(@.$*)@')
            print('4vby3489vtb3v7tr80T*)@B^C806b3r807wb')
            print('*(349bfUFGbbofeb78838b0t78t038tbb')
            print('C@&s3: y07r syst3m hav3 h0l*d^^n02')
            print('pr3@@ 3n53r t0 g0 t0 s7st3, sh*5d02n')
            input()
            sys.exit()
        else:
            sys.exit()
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
        print("Input unencrypted message.")
        um = input()
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
        if sda == 'y':
            print("What file do you want it to be written to? No extension needed.")
            fex = input()
            fex = fex + '.bue'
            try:
                f = open(fex,'x')
                f.write(enc)
                f.close()
                print("written to",fex)
            except:
                f = open(fex,'w')
                f.write(enc)
                f.close()
                print("written to",fex)
            
    elif command == 'translate':
        print("Translate from what file? Encoded message files usually have a bue file extension. You don't need to put the file extension here.")
        fex = input()
        fex = fex + '.bue'
        try:
            f = open(fex,'r')
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
            if wt == 'y':
                print("What should the fle name be? (no extension needed)")
                fex = input()
                fex = fex + '.txt'
                try:
                    f = open(fex,'x')
                    f.write(tra)
                    f.close()
                    print("written to",fex)
                except:
                    f = open(fex,'w')
                    f.write(tra)
                    f.close()
                    print("written to",fex)
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
        txt = Entry(ct,width=10)
        txt.grid(column=0,row=0)
        txt1 = Entry(ct,width=10)
        txt1.grid(column=1,row=0)
        txt2 = Entry(ct,width=10)
        txt2.grid(column=2,row=0)
        btn = Button(ct,text='Generate colour',command=colourchange,bg='green')
        btn.grid(column=1,row=1)
        lbl = Label(ct,text='Please enter values between 0 and 255')
        lbl.grid(column=1,row=2)
        btn1 = Button(ct,text='Exit',command=bby,bg='red')
        btn1.grid(column=2,row=1)
        ct.mainloop()
        
    elif command == 'clean your room':
        messagebox.showerror('Error','Computers cannot clean their rooms')
    elif command == 'ur mom':
       messagebox.showerror('Error','Shut up, you inmature child')
    elif command == 'spam':
        for i in range(20):
            try:
                os.startfile('error.vbs')
            except:
                error(2)
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

    elif command == 'pre-uninstall':
        try:
            os.startfile('pre-uninstall.bat')
        except:
            error(2)
        else:
            print("doing stuff .",end='\r')
            sleep(0.3)
            print("doing stuff ..",end='\r')
            sleep(0.3)
            print("doing stuff ...",end='\n')
            sleep(0.3)

    elif command == 'uninstall':
        try:
            os.startfile('pre-uninstall.bat')
        except:
            error(2)
        else:
            for i in range(5):
                print("uninstalling .",end='\r')
                sleep(0.3)
                print("uninstalling ..",end='\r')
                sleep(0.3)
                print("uninstalling ...",end='\r')
                sleep(0.3)
                print("                            ",end='\r')
            try:
                os.startfile('unins000.exe')
            except:
                error(2)
            else:
                sys.exit()

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
        print('conv len cmd: Access the new length converter command menu')

    elif command == 'conv len i-y':
        conv('inches','yards',"/48")
    elif command == 'conv len cmd':
        xay = True
        while xay == True:
            print('-----Length Converter Command Menu-----')
            print('Type your command under here and press enter')
            mxe = input()
            if mxe == 'help' or mxe =='?':
                print('-----Commands List for Conv Len-----')
                print('help: Shows this list')
                print('cmd: Go to the command menu')
                print('km-mi: kilometres to miles')
                print('mi-km: miles to kilometres')
            elif mxe == 'cmd':
                break
            elif mxe == 'km-mi':
                conv('kilometres','miles','/1.609')
            elif mxe == 'mi-km':
                conv('miles','kilometres','*1.609')
            else:
                messagebox.showwarning('Warning','Unrecognised command. Type help for the list.')

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
                    error(0)
                sc_tm = sc_tm - 1
                sleep(1)
            if sc_tm < 1:
                tmdone()

        def tmdone():
            global btn23
            btn23['state'] = 'disabled'
            btn22['state'] = 'disabled'
            btn25['state'] = 'normal'
            try:
                lbl.configure(text='Timer is Done')
            except:
                error(0)
            print("Your timer is done")
            try:
                playsound("warning.mp3")
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
            th.start()

        def tmstop():
            global paused
            paused = True
            btn22['state'] = 'normal'
            btn25['state'] = 'normal'

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
            btn24 = Button(tm,text="Stop",command=tm.destroy,bg='red')
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
        def swmain():
            global tcount
            global window
            global lbl
            global paused
            global btn
            global btn3
            window = Tk()
            window.title("Stopwatch")
            window.geometry("400x100")
            lbl = Label(window,text="0")
            lbl.grid(column=0,row=0)
            btn = Button(window,text="Start",command=swstart,bg="green")
            btn.grid(column=0,row=1)
            btn1 = Button(window,text="Pause",command=swstop,bg="yellow")
            btn1.grid(column=1,row=1)
            btn2 = Button(window,text="Stop",command=window.destroy,bg="red")
            btn2.grid(column=2,row=1)
            btn3 = Button(window,text='Reset',command=swreset,bg='blue')
            btn3.grid(column=3,row=1)
            window.mainloop()
            window.quit()
            paused = True

        def swstart():
            global btn3
            global btn
            btn['state'] = "disabled"
            btn3['state'] = "disabled"
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
                    error(0)
                    print("You can still run commands.")

        def swstop():
            global paused
            global btn
            global btn3
            btn['state'] = "normal"
            btn3['state'] = 'normal'
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
        print("Please type the full equation here.")
        equation = input()
        qku = "print("
        equation = qku + equation
        equation = equation + ")"
        try:
            exec(equation)
        except:
            error(3)

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
            chgx = [0,0,0,1,2]
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
            if writetofile == "y":
                print("What should the file containing the password be called?")
                print("example: myfile.txt")
                print("Make sure to include the .txt at the end, otherwise your file may be unreadable.")
                filesname = input()
                if filesname == "BasicUtilities.exe":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "logoff.bat":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "restart.bat":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "stop.bat":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "gameboard.jpg":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "help.txt":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "BasicUtilities.py":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                elif filesname == "warning.mp3":
                    print("This is the name of a vital program file. You are not allowed to overwrite that.")
                    break
                try:
                    f = open(filesname,"x")
                except FileExistsError:
                    print("This file already exists. Do you want to overwrite it?(y/n)")
                    overwrite = input()
                    if overwrite == "y":
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
                        print("After you copy and paste this file to a secure directory, remember to destroy the file in this directory!")
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
                    print("After you copy and paste this file to a secure directory, remember to destroy the file in this directory!")
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
        print("Coded in Python 3.7.3, 3.9.2 and 3.9.5; compiled in Pyinstaller 4.3")
        print("Written by Enderbyte09")
        print("With IDLE for 64-bit Windows")
        print("And notepad++")
        print("And Thonny IDE for Raspberry Pi 4")
        print('AND IDLE 3.7.3 for Raspberry Pi 4')
        print("Game board pictures by Kdog.")
        print("Insults by Arceus007")
        print('Sound Air Horn from SoundBible')
        print('Sound "Windows Xp Boot" from Instant Sounds')
        print('Sound "Windwos 7 Boot" from [unknown]')
        print("Started on April 14, 2021")
        print("2838 lines of code")
        print("Alot of chracters")

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
                    playsound("warning.mp3")
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
        sys.exit()
        break
    elif command == "stopall":
        try:
            os.startfile("stop.bat")
        except:
            error(2)
    elif command == "game":
        total_money = 500
        times_played = 0
        print("What is your name?")
        name = input()
        print("Welcome",name,"to Enderbyte09's Beat th' Bank!")
        print("enter/return to continue.")
        input()
        print("You will have to open vault doors. You will gain money. However, there is a chance that you will open the ALARM, in which case you will get no money at all.")
        print("press enter/return to begin")
        print("It cost 100 to play.")
        input()
        if name == 'Ruby' or name == 'ruby':
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
                    if openvault == "y":

                        moneyadd = random.choice(possible)
                        print("Vault",vaults,"has",moneyadd,"in it.")
                        print("")
                        vaults = vaults + 1
                        if moneyadd == "alarm":
                            alarm = True
                            try:
                                playsound("warning.mp3")
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
                    if statsee == "y":
                        answered = True
                        print("You have played",times_played,"games")
                        print("You have a total of",total_money,"money.")
                    elif statsee == "n":
                        answered = True
                        print("If you say so")
                print("do you want to play again? (y/n)")
                print("Typing n returns you to the commands menu.")
                playagain = input()
                if playagain == "y":
                    for i in range(1,20):
                        print("")
                    print("Do you want to change name? (y/n)")
                    changename = input()
                    if changename == "y":
                        print("Please type your new name")
                        name = input()
                        print("Welcome,",name,"to Enderbyte09's Beat The Bank!")
                        for i in range(1,20):
                            print("")
    elif command == "insult":
        adjec = ["Loggerheaded","Beefwitted","Cream-faced","","Stupid","Imbecilic","Rank","Gassy","Pork-witted","Zombified","Gelatin-bottomed","picklebrained"]
        noun = ["Applejohn","Loon","Creamface","Beefwit","Porkwit","Dummy","Lunatic","Idiot","Yellwe","Straightjacket","Clackdish","Jellyfish"]
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
            print("It has been",second,"seconds sinceCOVID-19 infected its first human")
            print("")
            sleep(1)

    elif command == "web":
        print("Please type the exact url of what you want to search.")
        search = input()
        if search[0] == "h" and search[1] == "t" and search[2] == "t" and search[3] == "p":
            try:
                webbrowser.open(search)
            except:
                error(6)
        else:
            error(6)

    elif command == "logoff":
        logoff = True
        while logoff == True:
            try:
                os.startfile("logoff.bat")
            except:
                error(2)
                break
            finally:
                logoff = False
    elif command == "restart":
        restart = True
        while restart == True:
            try:
                os.startfile("restart.bat")
            except:
                error(2)
                break
            finally:
                restart = False

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
                    playsound("warning.mp3")
                    asdfgh = False
                except:
                    error(2)
                    crashed = True
                    asdfgh = False
                    break

            for i in range(1,5):
                if crashed == False:
                    playsound("warning.mp3")
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
            lagcount = 0
            try:
                s = turtle.getscreen()
                t = turtle.Turtle()
            except:
                s = turtle.getscreen()
                t = turtle.Turtle()
            t.speed(10)
            t.penup()
            t.goto(-300,-300)
            t.pendown()
            t.goto(300,-300)
            t.penup()
            t.goto(-300,-300)
            t.pendown()
            t.pencolor("red")
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
                tims = 0
                sleep(1)
                tims = 1
                qwert = datetime.datetime.now()
                ft = qwert.strftime('%S.%f')[:-3]
                ft = float(ft)
                lag = ft - fa
                lag = lag - tims
                lag = lag * 1000
                try:
                    if noscreen == False:
                        tlag = lag - 300
                        ttotal = ttotal + 10
                        tgotototal = ttotal - 300
                        t.goto(tgotototal,tlag)
                        if tgotototal > 300:
                            t.clear()
                            ttotal = 0
                            t.penup()
                            t.goto(-300,-300)
                            t.pendown()
                            t.pencolor("black")
                            t.goto(300,-300)
                            t.penup()
                            t.goto(-300,-300)
                            t.pendown()
                            t.pencolor("red")
                            
                except:
                    xsgued = 0
                qwe = datetime.datetime.now()
                averagelag = averagelag + lag
                avglag = averagelag / lagcount
                print("your computer is lagging by",lag,"milliseconds")
                print("Your average computer lag is",avglag,"milliseconds")
                print("Your computer is",averagelag,"milliseconds behind.")
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
            if adddata == "y":
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
        if seeboard == "y":
            awrt = True
            while awrt == True:
                try:
                    os.startfile("gameboard.jpg")
                except:
                    print("Oh no! Something went wrong!")
                    print("Please make sure that there is a file called 'gameboard.jpg'.")
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
        if seeboard == "y":
            awrt = True
            while awrt == True:
                try:
                    os.startfile("gameboard.jpg")
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
        messagebox.showwarning('Warning',"You typed in an unrecognised command.\n If you want the commands list, dismiss this message and run the command '?' or 'help'")
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
        messagebox.showinfo('Analytics Reporter',xls)
    else:
        f = open('notifs.txt','w')
        f.write('1')
        
        xls = 'You have run this many commands this session: ' + xmls + ". If you don't want messagebox notifs, change this with the notifs command."
        print('')
        print(xls)
    f.close()
#NOW were done        
