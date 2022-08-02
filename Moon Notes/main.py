import os
from colorama import Fore, init

init(autoreset=True)

####Variables####
color1 = Fore.MAGENTA
color2 = Fore.MAGENTA
fg = Fore.MAGENTA
bg = Fore.MAGENTA
name_template = "Moon Notes"

def cls():
    os.system("cls")
cls()

def login():
    print("login")

def create_notes():
    print("create_notes")

def menu():
    print(f"                    {color1}[{fg}1{color1}]  {fg}Create Note                                         Notes List {color2}[{fg}2{color2}]")
    option_choice = input(f"\n{bg}[{fg}{name_template}{bg}]{fg} | {bg}Choice{fg}: ")
    cls()
    menu()
    if option_choice == "1":
        create_notes()

login()
menu()