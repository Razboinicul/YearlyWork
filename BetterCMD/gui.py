import tkinter
import cmd
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror

root = tkinter.Tk()
root.title('CMD')
root.geometry('200x200')
root.resizable(False, False)
output_text = tkinter.StringVar()
output = tkinter.Label(root, textvariable=output_text)
output.pack()
while True:
    prompt = askstring("Prompt", "prompt:") 
    if cmd.CommandRunner(prompt) == "Wrong Command":
        showerror(title='Error', messoage="Command does not exist")
    else:
        cmd.CommandRunner(prompt)
        output_text.set(cmd.CommandRunner(prompt))     
          
    root.mainloop()

