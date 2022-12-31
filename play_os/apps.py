import os
import sys
import tkinter.messagebox
import platform
from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror, showinfo
from hashlib import md5

class Paint_app(object):

	def __init__(self, b1="up", xold=None, yold=None):
		self.root = Tk()
		self.x = self.y = 0
		
		self.paint = Label(self.root,text="Nano Paint",font="Elephent 25",bg="Sky blue",bd=3,relief="solid",width=50,height=2)
		self.paint.grid(row=0,column=0,columnspan=7)

		self.selectTool_label = Label(self.root,text="Select your Tool",font="Times 20",fg="dark blue",bd=1,relief="solid",width=50,height=1)
		self.selectTool_label.grid(row=1,column=0,columnspan=7)
		
		self.pen_btn = Button(self.root, text='Pen',width=10,bg="light green",font="Times 13 bold", command=self.pen)
		self.pen_btn.grid(row=4, column=0)
		
		self.line_btn = Button(self.root, text='Line',width=10,bg="light green",font="Times 13 bold", command=self.draw_line)
		self.line_btn.grid(row=4, column=1)

		self.rectangle_btn = Button(self.root, text='Rectangle',width=10,bg="light green",font="Times 13 bold", command=self.draw_rectangle)
		self.rectangle_btn.grid(row=4, column=2)
		
		self.circle_btn = Button(self.root,text="Circle",width=10,bg="light green",font="Times 13 bold", command=self.draw_circle)
		self.circle_btn.grid(row=4,column=3)
		
		self.eraser_btn = Button(self.root, text='Eraser',width=10,bg="light green",font="Times 13 bold", command=self.eraser)
		self.eraser_btn.grid(row=4, column=4)
		
		self.clearScreen_btn = Button(self.root, text='Clear Screen',width=10,bg="light green",font="Times 13 bold", command=self.clearScreen)
		self.clearScreen_btn.grid(row=6, column=1)
		
		self.quit_btn = Button(self.root, text='Quit',width=10,bg="light green",font="Times 13 bold", command=self.quit)
		self.quit_btn.grid(row=6, column=3)
		
		self.canvas = Canvas(self.root, bg='white', width=1000, height=500,cursor="cross")
		self.canvas.grid(row=5, columnspan=5)
		
		self.old_x = None
		self.old_y = None
	
		self.root.mainloop()
		
	def pen(self):
		self.canvas.bind('<B1-Motion>', self.motionPen)
		self.canvas.bind('<ButtonPress-1>',self.on_button_pressPen)
		self.canvas.bind('<ButtonRelease-1>',self.on_button_releasePen)
		
		
	def draw_line(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressLine)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseLine)
		
		
	def draw_rectangle(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressRectangle)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseRectangle)
		
		
	def draw_circle(self):
		self.canvas.bind("<ButtonPress-1>", self.on_button_pressCircle)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_releaseCircle)
		
		
	def eraser(self):
		self.canvas.bind('<B1-Motion>', self.motionEraser)
		self.canvas.bind('<ButtonPress-1>',self.on_button_pressEraser)
		self.canvas.bind('<ButtonRelease-1>',self.on_button_releaseEraser)
		
		
	def clearScreen(self):
		answer=tkinter.messagebox.askquestion("Reset","You want to Clear your Progress")	
		if answer=="yes":
			self.canvas.delete("all")
			
		if answer=="no":
			pass
		
	def quit(self):
		answer=tkinter.messagebox.askquestion("Quit","Want to Quit")
		if answer=="yes":
			self.root.destroy()
		if answer=="no":
			pass
	

	def on_button_pressLine(self, event):
		self.x = event.x
		self.y = event.y


	def on_button_releaseLine(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_line(x0,y0,x1,y1)
		

	def on_button_pressRectangle(self, event):
		self.x = event.x
		self.y = event.y

	def on_button_releaseRectangle(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_rectangle(x0,y0,x1,y1)
		
				
	def on_button_pressCircle(self, event):
		self.x = event.x
		self.y = event.y


	def on_button_releaseCircle(self, event):
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.create_oval(x0,y0,x1,y1)
		
		
	def on_button_pressPen(self,event):
		global b1
		b1 = "down"          


	def on_button_releasePen(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None


	def motionPen(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)                      
			xold = event.x
			yold = event.y
			
	
	def on_button_pressEraser(self,event):
		global b1
		b1 = "down"          


	def on_button_releaseEraser(self,event):
		global b1, xold, yold
		b1 = "up"
		xold = None         
		yold = None


	def motionEraser(self,event):
		if b1 == "down":
			global xold, yold
			if xold is not None and yold is not None:
				event.widget.create_line(xold,yold,event.x,event.y,fill="white",width=10,smooth=TRUE)
			xold = event.x
			yold = event.y

class Document:
    def __init__(self, Frame, TextWidget, FileDir=''):
        self.file_dir = FileDir
        self.file_name = 'Untitled' if not FileDir else os.path.basename(FileDir)
        self.textbox = TextWidget
        self.status = md5(self.textbox.get(1.0, 'end').encode('utf-8'))
        
class Editor:
    def __init__(self, master):
        self.master = master
        self.master.title("Nano Editor")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        self.filetypes = (("Normal text file", "*.txt"), ("all files", "*.*"))
        self.init_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        self.tabs = {} # { index, text widget }
        
        # Create Notebook ( for tabs ).
        self.nb = ttk.Notebook(master)
        self.nb.bind("<Button-2>", self.close_tab)
        self.nb.bind("<B1-Motion>", self.move_tab)
        self.nb.pack(expand=1, fill="both")
        self.nb.enable_traversal()
        #self.nb.bind('<<NotebookTabChanged>>', self.tab_change)

        # Override the X button.
        self.master.protocol('WM_DELETE_WINDOW', self.exit)
        
        # Create Menu Bar
        menubar = tk.Menu(self.master)
        
        # Create File Menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as)
        filemenu.add_command(label="Close", command=self.close_tab)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        
        # Create Edit Menu
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Paste", command=self.paste)
        editmenu.add_command(label="Delete", command=self.delete)
        editmenu.add_command(label="Select All", command=self.select_all)
        
        # Create Format Menu, with a check button for word wrap.
        formatmenu = tk.Menu(menubar, tearoff=0)
        self.word_wrap = tk.BooleanVar()
        formatmenu.add_checkbutton(label="Word Wrap", onvalue=True, offvalue=False, variable=self.word_wrap, command=self.wrap)
        
        # Attach to Menu Bar
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Format", menu=formatmenu)
        self.master.config(menu=menubar)
        
        # Create right-click menu.
        self.right_click_menu = tk.Menu(self.master, tearoff=0)
        self.right_click_menu.add_command(label="Undo", command=self.undo)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label="Cut", command=self.cut)
        self.right_click_menu.add_command(label="Copy", command=self.copy)
        self.right_click_menu.add_command(label="Paste", command=self.paste)
        self.right_click_menu.add_command(label="Delete", command=self.delete)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label="Select All", command=self.select_all)
        
        # Create tab right-click menu
        self.tab_right_click_menu = tk.Menu(self.master, tearoff=0)
        self.tab_right_click_menu.add_command(label="New Tab", command=self.new_file)
        self.nb.bind('<Button-3>', self.right_click_tab)

        # Create Initial Tab
        first_tab = ttk.Frame(self.nb)
        self.tabs[ first_tab ] = Document( first_tab, self.create_text_widget(first_tab) )
        self.nb.add(first_tab, text='Untitled')

    def create_text_widget(self, frame):
        # Horizontal Scroll Bar 
        xscrollbar = tk.Scrollbar(frame, orient='horizontal')
        xscrollbar.pack(side='bottom', fill='x')
        
        # Vertical Scroll Bar
        yscrollbar = tk.Scrollbar(frame)
        yscrollbar.pack(side='right', fill='y')

        # Create Text Editor Box
        textbox = tk.Text(frame, relief='sunken', borderwidth=0, wrap='none')
        textbox.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, undo=True, autoseparators=True)

        # Keyboard / Click Bindings
        textbox.bind('<Control-s>', self.save_file)
        textbox.bind('<Control-o>', self.open_file)
        textbox.bind('<Control-n>', self.new_file)
        textbox.bind('<Control-a>', self.select_all)
        textbox.bind('<Control-w>', self.close_tab)
        textbox.bind('<Button-3>', self.right_click)

        # Pack the textbox
        textbox.pack(fill='both', expand=True)        
        
        # Configure Scrollbars
        xscrollbar.config(command=textbox.xview)
        yscrollbar.config(command=textbox.yview)
        
        return textbox

    def open_file(self, *args):        
        # Open a window to browse to the file you would like to open, returns the directory.
        file_dir = (tkinter
         .filedialog
         .askopenfilename(initialdir=self.init_dir, title="Select file", filetypes=self.filetypes))
        
        # If directory is not the empty string, try to open the file. 
        if file_dir:
            try:
                # Open the file.
                file = open(file_dir)
                
                # Create a new tab.
                new_tab = ttk.Frame(self.nb)
                self.tabs[ new_tab ] = Document(new_tab, self.create_text_widget(new_tab), file_dir)
                self.nb.add(new_tab, text=os.path.basename(file_dir))
                self.nb.select( new_tab )
                            
                # Puts the contents of the file into the text widget.
                self.tabs[ new_tab ].textbox.insert('end', file.read())
                
                # Update hash
                self.tabs[ new_tab ].status = md5(self.tabs[ new_tab ].textbox.get(1.0, 'end').encode('utf-8'))
            except:
                return

    def save_as(self):
        curr_tab = self.get_tab()
    
        # Gets file directory and name of file to save.
        file_dir = (tkinter
         .filedialog
         .asksaveasfilename(initialdir=self.init_dir, title="Select file", filetypes=self.filetypes, defaultextension='.txt'))
        
        # Return if directory is still empty (user closes window without specifying file name).
        if not file_dir:
            return
         
        # Adds .txt suffix if not already included.
        if file_dir[-4:] != '.txt':
            file_dir += '.txt'
            
        self.tabs[ curr_tab ].file_dir = file_dir
        self.tabs[ curr_tab ].file_name = os.path.basename(file_dir)
        self.nb.tab( curr_tab, text=self.tabs[ curr_tab ].file_name) 
            
        # Writes text widget's contents to file.
        file = open(file_dir, 'w')
        file.write(self.tabs[ curr_tab ].textbox.get(1.0, 'end'))
        file.close()
        
        # Update hash
        self.tabs[ curr_tab ].status = md5(self.tabs[ curr_tab ].textbox.get(1.0, 'end').encode('utf-8'))
        
    def save_file(self, *args):
        curr_tab = self.get_tab()
        
        # If file directory is empty or Untitled, use save_as to get save information from user. 
        if not self.tabs[ curr_tab ].file_dir:
            self.save_as()

        # Otherwise save file to directory, overwriting existing file or creating a new one.
        else:
            with open(self.tabs[ curr_tab ].file_dir, 'w') as file:
                file.write(self.tabs[ curr_tab ].textbox.get(1.0, 'end'))
                
            # Update hash
            self.tabs[ curr_tab ].status = md5(self.tabs[ curr_tab ].textbox.get(1.0, 'end').encode('utf-8'))
                
    def new_file(self, *args):                
        # Create new tab
        new_tab = ttk.Frame(self.nb)
        self.tabs[ new_tab ] = Document(new_tab, self.create_text_widget(new_tab))
        self.tabs[ new_tab ].textbox.config(wrap= 'word' if self.word_wrap.get() else 'none')
        self.nb.add(new_tab, text='Untitled')
        self.nb.select( new_tab )
        
    def copy(self):
        # Clears the clipboard, copies selected contents.
        try: 
            sel = self.tabs[ self.get_tab() ].textbox.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.master.clipboard_clear()
            self.master.clipboard_append(sel)
        # If no text is selected.
        except tk.TclError:
            pass
            
    def delete(self):
        # Delete the selected text.
        try:
            self.tabs[ self.get_tab() ].textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)
        # If no text is selected.
        except tk.TclError:
            pass
            
    def cut(self):
        # Copies selection to the clipboard, then deletes selection.
        try: 
            sel = self.tabs[ self.get_tab() ].textbox.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.master.clipboard_clear()
            self.master.clipboard_append(sel)
            self.tabs[ self.get_tab() ].textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)
        # If no text is selected.
        except tk.TclError:
            pass
            
    def wrap(self):
        if self.word_wrap.get() == True:
            for index in self.tabs:
                self.tabs[ index ].textbox.config(wrap="word")
        else:
            for index in self.tabs:
                self.tabs[ index ].textbox.config(wrap="none")
            
    def paste(self):
        try: 
            self.tabs[ self.get_tab() ].textbox.insert(tk.INSERT, self.master.clipboard_get())
        except tk.TclError:
            pass
            
    def select_all(self, *args):
        curr_tab = self.get_tab()
        
        # Selects / highlights all the text.
        self.tabs[ curr_tab ].textbox.tag_add(tk.SEL, "1.0", tk.END)
        
        # Set mark position to the end and scroll to the end of selection.
        self.tabs[ curr_tab ].textbox.mark_set(tk.INSERT, tk.END)
        self.tabs[ curr_tab ].textbox.see(tk.INSERT)

    def undo(self):
        self.tabs[ self.get_tab() ].textbox.edit_undo()

    def right_click(self, event):
        self.right_click_menu.post(event.x_root, event.y_root)
        
    def right_click_tab(self, event):
        self.tab_right_click_menu.post(event.x_root, event.y_root)
        
    def close_tab(self, event=None):
        # Close the current tab if close is selected from file menu, or keyboard shortcut.
        if event is None or event.type == str( 2 ):
            selected_tab = self.get_tab()
        # Otherwise close the tab based on coordinates of center-click.
        else:
            try:
                index = event.widget.index('@%d,%d' % (event.x, event.y))
                selected_tab = self.nb._nametowidget( self.nb.tabs()[index] )
            except tk.TclError:
                return

        # Prompt to save changes before closing tab
        if self.save_changes():
            self.nb.forget( selected_tab )
            self.tabs.pop( selected_tab )

        # Exit if last tab is closed
        if self.nb.index("end") == 0:
            self.master.destroy()
        
    def exit(self):        
        # Check if any changes have been made.
        if self.save_changes():
            self.master.destroy()
        else:
            return
               
    def save_changes(self):
        curr_tab = self.get_tab()
        file_dir = self.tabs[ curr_tab ].file_dir
        
        # Check if any changes have been made, returns False if user chooses to cancel rather than select to save or not.
        if md5(self.tabs[ curr_tab ].textbox.get(1.0, 'end').encode('utf-8')).digest() != self.tabs[ curr_tab ].status.digest():
            # If changes were made since last save, ask if user wants to save.
            m = messagebox.askyesnocancel('Editor', 'Do you want to save changes to ' + ('Untitled' if not file_dir else file_dir) + '?' )
            
            # If None, cancel.
            if m is None:
                return False
            # else if True, save.
            elif m is True:
                self.save_file()
            # else don't save.
            else:
                pass
                
        return True
    
    # Get the object of the current tab.
    def get_tab(self):
        return self.nb._nametowidget( self.nb.select() )
        
    def move_tab(self, event):
        '''
        Check if there is more than one tab.
        
        Use the y-coordinate of the current tab so that if the user moves the mouse up / down 
        out of the range of the tabs, the left / right movement still moves the tab.
        '''
        if self.nb.index("end") > 1:
            y = self.get_tab().winfo_y() - 5
            
            try:
                self.nb.insert( event.widget.index('@%d,%d' % (event.x, y)), self.nb.select() )
            except tk.TclError:
                return

class CMD_utils:
    def CommandRunner(self, prompt):
        self.prompt = prompt
        returned_cmd = ""
        if prompt == "mkdir":
            try:
                mkdir_name = askstring("Name", "Name for the folder:")
                os.mkdir(mkdir_name)
            except:
                sys.exit()
        elif prompt == "folderprop":
            print(os.getcwd())
            print(os.listdir())
            os.system("cd")
            returned_cmd = os.getcwd() + " " + os.listdir() + " " + os.system("cd")
            return returned_cmd
        elif prompt == "exit":
            running = False
        elif prompt == "cdfol":
            try:
                cd_input = askstring("CD", "Where to cd:")
                os.chdir(cd_input)
            except:
                sys.exit()
        elif prompt == "rmdir":
            try:
                rmdir_input = askstring("Delete", "What folder to delete(only folder(only one)):")
                os.rmdir(rmdir_input)
                returned_cmd = "Action Done"
                return returned_cmd
            except:
                sys.exit()
        elif prompt == "rename":
            try:
                ren_dir = askstring("DIR", "Name for the folder to rename:")
                try:
                    nn_dir = askstring("DIR", "New name for the folder:")
                    os.rename(ren_dir, nn_dir)
                    returned_cmd = "Action Done"
                    return returned_cmd
                except:
                    sys.exit()
            except:
                sys.exit()
        elif prompt == "walkfol":
            try:
                walkfol_input = askstring("WALK", "What folder to walk:")
                for dirpath, dirnames, filenames in os.walk(walkfol_input):
                    print("Directory path: ", dirpath)
                    print("Directory names: ", dirnames)
                    print("Files: ", filenames)
                    returned_cmd = "Directory path: ", dirpath, "Directory names: ", dirnames, "Files: ", filenames
                    return returned_cmd
            except:
                sys.exit()
        elif prompt == "randombyte":
            try:
                randombyte_input = askstring("RB", "Random bytes:")
                returned_cmd = os.urandom(vars(randombyte_input))
                return returned_cmd
            except:
                sys.exit()
        elif prompt == "cpucount":
            returned_cmd = os.cpu_count()
            return returned_cmd
        elif prompt == "mdate":
            try:
                mod_input = askstring("LMOD", "What folder or file do you want to see:")
                mod_time = os.stat(mod_input).st_mtime
                returned_cmd = datetime.fromtimestamp(mod_time)
                return returned_cmd
            except:
                sys.exit()
        elif prompt == "platform":
            if platform.system() == 'Darwin':
                returned_cmd = "OSX"
                return returned_cmd
            else:
                returned_cmd = platform.system()
                return returned_cmd
        else:
            if CMD_utils.CommandVerifier(prompt) == True:
                os.system(prompt)
            else:
                returned_cmd = "Wrong Command"
                return returned_cmd
            
    def CommandVerifier(self, command):
        self.command = command
        runable = False
        if os.system(command) == 0:
            runable = True
        else:
            runable = False
        return runable
    
    def cmd_extention(self):
        utils = CMD_utils()
        cmd_prompt = askstring("Command", "Command:") 
        if cmd_prompt == "exit":
            return False
        else:
            if utils.CommandRunner(prompt=cmd_prompt) == "Wrong Command":
                showerror(title='Error', message="Command does not exist")
            else:
                utils.CommandRunner(prompt=cmd_prompt)
                showinfo("Output", utils.CommandRunner(prompt=cmd_prompt))
            return True

def cmd_app():
    utils = CMD_utils()
    running = True
    while running:
        utils.cmd_extention()
        running = utils.cmd_extention()
            
def nano_editor():
    root = tk.Tk()
    app = Editor(root)
    root.mainloop()
    
def apps():
    root = tk.Tk()
    cmd_button = tk.Button(root, text="CMD", command=cmd_app)
    nano_editor_button = tk.Button(root, text="Nano Editor", command=nano_editor)
    paint_button = tk.Button(root, text="Nano Paint", command=Paint_app)
    cmd_button.pack()
    nano_editor_button.pack()
    paint_button.pack()
    root.mainloop()
    
apps()

        
        
