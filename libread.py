"""
Libread is a lightweight module implementation of Teleread and allows you to read books. I find it useful to write documentations. To run, use libread.read(filename).
DEPENDS ON OTHER ENDERBYTE PROGRAMS LIBRARIES libcurses

(c) 2022 Enderbyte Programs
"""

import curses
from curses.textpad import rectangle
import os
from textwrap import wrap
from libcurses import *#Migrating special functions to new library

def read_book(stdscr,filename: str):
    global LIBRARY
    try:
        with open(filename) as f:
            data = f.read()
    except (PermissionError, OSError, FileNotFoundError) as e:
        displayerror(stdscr,e,"Book Read Error")
        return 1
    try:
        data = "\n".join([ln for ln in data.split("\n") if ln.replace(" ","") != ""])#Removing empty lines
        config = data.split("\n%startdata\n")[0]
        book = data.split("\n%startdata\n")[1]
        config = {st.split("=")[0].strip():st.split("=")[1].strip() for st in config.split("\n")}
    except Exception as e:
        displayerror(stdscr,e,"Book Init Error")
        return 1
    stdscr.erase()
    stdscr.addstr(0,0,f"Loading {config['title']}")
    stdscr.refresh()
    x,y = os.get_terminal_size()
    book = [d for d in book.splitlines() if d[0] != "#" and d.replace(" ","") != ""]#Removing comments and empty lines
    linc = 0
    chapregister = {}
    validchars = ["#","$","%","+","-","@"]
    recoverdoc = None
    #Validating syntax
    for bline in book:
        linc += 1
        if bline[0] not in validchars:
            if recoverdoc is None:
                displaymsg(stdscr,["Syntax error in",filename,f"Invalid character on line {linc}","\""+bline+"\"","Press any key to see options"])
                _rec = displayops(stdscr,["Yes (once)","No","Yes to all","No to all"],"Would you like to recover this document?")
                if _rec == 0:
                    str(list(bline).insert(0,"+"))
                elif _rec == 2:
                    recoverdoc = True
                elif _rec == 3:
                    recoverdoc = False
            elif recoverdoc:
                str(list(bline).insert(0,"+"))
        if len(bline) > 9 and bline[0:8] == "$register":
            chapregister[" ".join(bline.split(" ")[1:])] = linc
    linc = 0
    
    chapregister = []
    textlist = []
    activefg = 0
    for bline in book:
        if bline[0] == "+":
            if bline[1:] == "":

                textlist.append({"data":bline[1:],"cen":False,"cl":activefg,"appendr":False})
            else:
                _brline = wrap(bline[1:],x-3)
                for _br in _brline:
                    textlist.append({"data":_br,"cen":False,"cl":activefg,"appendr":False})
        elif bline[0:2] == "--":
            textlist.append({"data":bline[2:],"cen":True,"cl":activefg,"appendr":False})
        elif bline.strip() == "%pagebreak":
            textlist.append({"data":"","special":"break"})
        elif bline[0] == "$":
            if bline[1:3].upper() == "FG":
                newfg = bline[4:]
                if newfg.lower() == "reset":
                    activefg = 0
                    continue
                try:
                    activefg = int(newfg)
                except:
                    displaymsg(stdscr,["Syntax Error: Invalid colour"])
            elif bline[1:9] == "register":
                textlist.append({"data":bline[10:],"special":"putchapter"})#Telling interpreter to register a new chapter
            linc -= 1
        elif bline[0] == "@":
            textlist.append({"data":bline[1:],"cen":False,"cl":activefg,"appendr":True})#New entry for text but telling interpreter to remove formatting
        linc += 1
    linc = 0
    stdscr.erase()
    brokenpage = False
    #Calculating pagelist
    pagelist = []
    #print(textlist)
    page = 0
    lpage = 0
    x,y = os.get_terminal_size()
    validrlines = y - 4
    activeopage = []
    for instruction in textlist:
        
        if "special" in instruction.keys():
            if instruction["special"] == "break":
                pagelist.append(activeopage)#Early break of page
                page += 1
                lpage = 0
                activeopage = []
            elif instruction["special"] == "putchapter":
                chapregister.append((page,instruction["data"]))#Tuple in structure of (page,name)
                continue#DO NOT increment local page
        else:
            activeopage.append(instruction)
        lpage += 1
        if lpage == validrlines:
            lpage = 0
            page += 1
            pagelist.append(activeopage)
            activeopage = []
    del lpage
    #del textlist#Freeing up memory
    page = 0
   
    #print(pagelist)
    #print(chapregister)
    #input()
    while True:
        x,y = os.get_terminal_size()
        validrlines = y - 4
        llinc = 0
        
        #Iterate through textlist
        for t in pagelist[page]:
            if t == "":
                continue
            else:
                if not t["cen"]:
                    if t["appendr"]:
                        stdscr.addstr(llinc+2-1,len(pagelist[page][llinc-1+linc]["data"]),t["data"],curses.color_pair(t["cl"]))
                        llinc += 1
                    else:
                        _brdata = wrap(t["data"],x-3)
                        if len(_brdata) == 0:
                            llinc += 1
                        for br in _brdata:
                            stdscr.addstr(llinc+2,1,br,curses.color_pair(t["cl"]))
                            llinc += 1
                elif t["cen"]:
                    _brdata = wrap(t["data"],x-3)
                    if len(_brdata) == 0:
                            llinc += 1
                    for br in _brdata:
                        stdscr.addstr(llinc+2,x//2-(len(br)//2),br,curses.color_pair(t["cl"]))
                        llinc += 1
            if llinc > validrlines:
                break
            #llinc += 1
        stdscr.addstr(0,0,f"Reading {config['title']} by {config['publisher']}")
        rectangle(stdscr,1,0,y-2,x-1)
        stdscr.addstr(y-1,0,f"Page: {page+1}/{len(pagelist)} ({round((page+1)/len(pagelist)*100,2)}%)")#+1 for user friendliness
        stdscr.refresh()
        ch = stdscr.getch()
        if ch == curses.KEY_LEFT and page> 0:
            page -= 1
        elif ch == curses.KEY_RIGHT and page < len(pagelist)-1:
            page += 1
        elif ch == curses.KEY_RIGHT and page+1 == len(pagelist):
            bookl = ["Quit","Return to book"]
            urll = ["_"]
            stdscr.erase()
            dbook = displayops(stdscr,bookl,"You finished the book. Here are some more!")
            if dbook == 0:
                return
            elif dbook == 1:
                stdscr.erase()
                continue#Returning back to book
                
        elif ch == curses.KEY_BACKSPACE or ch == 98:
            stdscr.erase()
            return
        elif ch == 103:#g
            if len(chapregister) > 0:
                stdscr.erase()
                gtc = displayops(stdscr,[f"{c[1]} (Page {c[0]+1})" for c in chapregister],"Please choose a chapter")
                if gtc > -1:
                    page = chapregister[gtc][0]
            else:
                displaymsg(stdscr,["this book has no chapters."])
        stdscr.erase()

def load_colours():
    curses.init_pair(7,curses.COLOR_BLACK,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    curses.init_pair(8,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_WHITE,curses.COLOR_BLACK) 

def init(stdscr,filename: str):
    curses.start_color()
    curses.use_default_colors()
    load_colours()
    read_book(stdscr,filename)

def read(filename: str):
    curses.wrapper(init,(filename))