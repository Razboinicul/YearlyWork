import play
from datetime import datetime
import psutil
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo, showwarning
from apps import apps
    
def example_app():
    window = Tk()

    window.title("Example app")

    window.mainloop()

def main():
    open = False
    play.set_backdrop(color_or_image_name='blue')
    # Main program
    taskbar = play.new_box(color='gray',y=-300, width=950, height=45)
    start_button = play.new_text(words="Start", size=35, x=-370, y=-290, font_size=95)
    print_button = play.new_text(words="Print", size=35, x=-370, y=-240, font_size=105)
    shutdown_button = play.new_text(words="Shutdown", size=35, x=-335, y=-260, font_size=105)
    apps_button = play.new_text(words="Apps", size=35, x=-365, y=-220, font_size=120)
    close_button = play.new_text(words="X", size=35, x=-314, y=-200, font_size=120)
    time = play.new_text(words='-', y=-283, x=265, size=50)
    date = play.new_text(words='-', y=-295, x=265, size=50)
    battery_text = play.new_text(words='-', y=-290, x=360, size=75)
    print_button.hide()
    shutdown_button.hide()
    apps_button.hide()
    close_button.hide()

    @play.repeat_forever
    def do():
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M")
        time.words = current_time
        today = datetime.now().date()
        d1 = today.strftime("%d/%m/%Y")
        date.words = d1
        battery_info = battery = psutil.sensors_battery()
        percent = battery_info.percent
        battery_text.words = str(percent) + '%'


    @start_button.when_clicked
    def function():
            print("Start open")
            print_button.show()
            apps_button.show()
            shutdown_button.show()
            close_button.show()

    @close_button.when_clicked
    def function():
        print("Start close")
        print_button.hide()
        apps_button.hide()
        shutdown_button.hide()
        close_button.hide()


    @print_button.when_clicked
    def function():
        print(print_button)
        
    @apps_button.when_clicked
    def function():
        apps()

    @time.when_clicked
    def function():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        example_app()
        
    @shutdown_button.when_clicked
    def function():
        print("Shutdown")
        quit()

    play.start_program()
    
def login_screen(dev=False):
    password = open("D:\stuff\Play\play_os\.pass", "r")
    up_password = str(password).upper()
    if dev == True:
        main()
    else:
        prompt = askstring("Login", "Password:") 
        if prompt == password or up_password:
            showinfo(title='Correct', message="Logged in")
            main()
        else:
            showwarning(title='Incorect', message="You are not logged in")
            quit()
    
if __name__ == '__main__':
    login_screen()