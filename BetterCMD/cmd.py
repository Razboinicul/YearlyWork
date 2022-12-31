import os
import subprocess
import platform
from datetime import datetime
import tkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror


def CommandRunner(prompt):
    returned_cmd = ""
    if prompt == "mkdir":
        mkdir_name = input("New folder name: ")
        os.mkdir(mkdir_name)
    elif prompt == "folderprop":
        print(os.getcwd())
        print(os.listdir())
        os.system("cd")
        returned_cmd = os.getcwd() + " " + os.listdir() + " " + os.system("cd")
        return returned_cmd
    elif prompt == "exit":
        exit()
    elif prompt == "cdfol":
        cd_input = input("Where to cd: ")
        os.chdir(cd_input)
    elif prompt == "rmdir":
        rmdir_input = input("What Folder to del: ")
        os.rmdir(rmdir_input)
    elif prompt == "rename":
        ren_dir = input("What you want to rename: ")
        nn_dir = input("What you want to be the new name: ")
        os.rename(ren_dir, nn_dir)
    elif prompt == "walkfol":
        walkfol_input = input("what folder to walk: ")
        for dirpath, dirnames, filenames in os.walk(walkfol_input):
            print("Directory path: ", dirpath)
            print("Directory names: ", dirnames)
            print("Files: ", filenames)
            returned_cmd = "Directory path: ", dirpath, "Directory names: ", dirnames, "Files: ", filenames
            return returned_cmd
    elif prompt == "randombyte":
        randombyte_input = input("Random Bytes: ")
        returned_cmd = os.urandom(vars(randombyte_input))
        return returned_cmd
    elif prompt == "cpucount":
        returned_cmd = os.cpu_count()
        return returned_cmd
    elif prompt == "mdate":
        mod_input = input("What file to see the last mod time: ")
        mod_time = os.stat(mod_input).st_mtime
        returned_cmd = datetime.fromtimestamp(mod_time)
        return returned_cmd
    elif prompt == "platform":
        if platform.system() == 'Darwin':
            returned_cmd = "OSX"
            return returned_cmd
        else:
            returned_cmd = platform.system()
            return returned_cmd
    else:
        if CommandVerifier(prompt) == True:
            os.system(prompt)
        else:
            returned_cmd = "Wrong Command"
            return returned_cmd
        
def CommandVerifier(command):
    runned = False
    if os.system(command) == 0:
        runned = True
    else:
        runned = False
    return runned

def cmd_app():
    root = tkinter.Tk()
    root.title('CMD')
    root.geometry('200x200')
    root.resizable(False, False)
    output_text = tkinter.StringVar()
    output = tkinter.Label(root, textvariable=output_text)
    output.pack()
    while True:
        prompt = askstring("Prompt", "prompt:") 
        if CommandRunner(prompt) == "Wrong Command":
            showerror(title='Error', messoage="Command does not exist")
        else:
            CommandRunner(prompt)
            output_text.set(CommandRunner(prompt))     
            
        root.mainloop()
