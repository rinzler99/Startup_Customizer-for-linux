# GUI generated using Page
# Written by Rinzler June-7-2018

import sys
import startupcustomizer


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def set_Tk_var():
    global command
    command = StringVar()
    global name_of_app
    name_of_app = StringVar()



                        #:::::::::::Main logic starts from here:::::::::::#




def addapp():
    command_app=command.get()
    name=name_of_app.get()
    d = {}
    d[name]=command_app


#get the path of home directory

    if name!='' and command_app!='':
        import subprocess
        subprocess.call("chmod +x extract_homedir.sh",shell=True)
        subprocess.call("./extract_homedir.sh", shell=True)
        f=open("read_homedir.txt","r")
        home_dir=f.read()
        f.close()

#Insert the command into .profile/.bash_profile to start it after logging in

        import os
        home=home_dir[:len(home_dir)-1]
        for i in os.listdir(home):
            if i=='.bash_profile':
                y='/.bash_profile'
                break
            elif i=='.bash_login':
                y='/.bash_login'
                break
            else:
                y='/.profile'

        z= home+y
        f=open(z,"a+")
        f.write(command_app+" &\n")
        f.close()
        f = open("view.txt", "a+")
        for key, value in d.items():
            f.write(key + " " * (20 - len(key)) + value + "\n")
        f.close()
        destroy_window()
        import easygui
        easygui.msgbox("Your app is added to startup...\n Reboot to test ...")
        startupcustomizer.vp_start_gui()
    else:
        import easygui
        easygui.msgbox("Text-Entry Should not be empty")


#delete apps from startup
def deleteapps():
    import easygui
    result=easygui.multenterbox("","Delete Startup Application",["Name","Command"])
    #print(result)
    strtodelete=result[0]+" "*(20-len(result[0]))+result[1]+'\n'
    f = open("view.txt", "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != strtodelete:
            f.write(i)
    f.truncate()
    f.close()
    f = open("read_homedir.txt", "r")
    home_dir = f.read()
    f.close()
    import os
    home = home_dir[:len(home_dir) - 1]
    for i in os.listdir(home):
        if i == '.bash_profile':
            y = '/.bash_profile'
            break
        elif i == '.bash_login':
            y = '/.bash_login'
            break
        else:
            y = '/.profile'

    z = home + y
    f = open(z, "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != result[1]+" &\n":
            f.write(i)
    f.truncate()
    f.close()

#view apps added on startup

def viewaddedapps():
    #f = open("view.txt", "a+")
    #for key, value in d.items():
    #    f.write(key+" "*(20-len(key))+value+"\n")
    #f.close()
    import subprocess
    subprocess.call("gedit view.txt",shell=True)
#Help
def help():
    import easygui
    easygui.msgbox("For example ::\n\n\n1.to open firefox you have to type 'firefox' in terminal\n\n2.To open sublime text editor you have to type 'sblm' in terminal\n\n\tSuch Commands You have to type in here\n\n\n\n\n\n\n\t\t\t\tProgrammed By:Rinzler","Help")

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import startupcustomizer
    startupcustomizer.vp_start_gui()


