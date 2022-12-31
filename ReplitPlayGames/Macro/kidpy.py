
from os import system
import keyboard
from math import sqrt


def get_key(key):
    pressed = False
    if keyboard.read_key() == key:
        pressed = True
        return pressed

def clearscreen():
    system('cls')

def write(text):
    print(str(text))


def add(var, var1):
    add_var = var + var1
    return add_var
def take(var, var1):
    take_var = var - var1
    return take_var

def multiply(var1, var2):
    multiply_var = var1 * var2
    return multiply_var

def divide(var, var1):
    if var1 <= 0:
        print('Impossible divide')
    else:
        div_var = var / var1
        return div_var

def power(var1, var2):
    power_var = var1 ** var2
    return power_var

def sqareroot(number):
    sqrt_var = sqrt(number)
    return number