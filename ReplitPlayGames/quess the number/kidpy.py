from win32com.client import Dispatch
from os import system
import keyboard
from math import sqrt

speak = Dispatch("SAPI.SpVoice").Speak

def get_key(key):
    pressed = False
    if keyboard.read_key() == key:
        pressed = True
        return pressed

def clearscreen():
    system('cls')

def write(text):
    print(str(text))

def say(text):
    speak(text)
    return text

def add(var, var1):
    add_var = int.var + int.var1
    return add_var
def take(var, var1):
    take_var = int.var - int.var1
    return take_var

def multiply(var1, var2):
    multiply_var = int.var1 * int.var2
    return multiply_var

def divide(var, var1):
    if var1 <= 0:
        print('Impossible divide')
    else:
        div_var = int.var / int.var1
        return div_var

def power(var1, var2):
    power_var = int.var1 ** int.var2
    return power_var

def sqareroot(number):
    sqrt_var = sqrt(int.number)
    return number