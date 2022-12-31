from os import *
from cmd import *

running = True

while running:
  print("PD", getlogin() + ">")
  cmd_prompt = input()
  print(cmd.CommandRunner(cmd_prompt))