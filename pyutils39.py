#WHY WON"T IT UPLOAD RIGHT!?!
#Toplevel commands may require Microsoft Only
from tkinter import Tk, messagebox
def reverse(data):
    x = str(data)
    datalen = len(data)
    x = x[datalen::-1]
    return x
def consoleask(question):
    while True:
        print(str(question)+' (Y/N)')
        x = input()
        if x.lower().startswith('y'):
            return True
            break
        elif x.lower().startswith('n'):
            return False
            break
def error(message,title='Error'):
    title = str(title)
    message = str(message)
    Tk().withdraw()
    messagebox.showerror(title,message)
def toplevelerror(message,title='Error'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showerror(title,message)
        

def question(message,title='Question'):
    title = str(title)
    message = str(message)
    Tk().withdraw()
    x = messagebox.askyesno(title,message)
    return x
def toplevelquestion(message,title='Question'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    x = messagebox.askyesno(title,message)
    return x

def infobox(message,title='Info'):
    title = str(title)
    message = str(message)
    Tk().withdraw()
    messagebox.showinfo(title,message)
    
def toplevelinfobox(message,title='Info'):
    title = str(title)
    message = str(message)
    root = Tk()
    root.wm_attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(title,message)
    
        