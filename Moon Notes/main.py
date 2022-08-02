import os
import ctypes
from colorama import Fore

####Variables####

version = str("0.0.1 Beta")

color1 = Fore.MAGENTA
color2 = Fore.MAGENTA
fg = Fore.MAGENTA
bg = Fore.MAGENTA
project_name = "Moon Notes"

ctypes.windll.kernel32.SetConsoleTitleW(f"{project_name} | {version}")

def console_text(var_name, datatype, value):
    var_name = datatype(input(f"\n{bg}[{fg}{project_name}{bg}]{fg} | {bg}value{fg}: "))

def cls():
    os.system("cls")
cls()


def setup():
    print("login")


def create_notes():
    print(console_text("note", str, "enter your note"))
    # print(f"{note}")


def note_list():
    print("note list")


def ascii_art():
    moon_ascii = f"""
                                        {fg}█{fg}█{fg}█{bg}╗   {fg}█{fg}█{fg}█{bg}╗ {fg}█{fg}█{fg}█{fg}█{fg}█{fg}█{bg}╗  {fg}█{fg}█{fg}█{fg}█{fg}█{fg}█{bg}╗ {fg}█{fg}█{fg}█{bg}╗   {fg}█{fg}█{bg}╗
                                        {fg}█{fg}█{fg}█{fg}█{bg}╗ {fg}█{fg}█{fg}█{fg}█{bg}║{fg}█{fg}█{bg}╔═══{fg}█{fg}█{bg}╗{fg}█{fg}█{bg}╔═══{fg}█{fg}█{bg}╗{fg}█{fg}█{fg}█{fg}█{bg}╗  {fg}█{fg}█{bg}║
                                        {fg}█{fg}█{bg}╔{fg}█{fg}█{fg}█{fg}█{bg}╔{fg}█{fg}█{bg}║{fg}█{fg}█{bg}║   {fg}█{fg}█{bg}║{fg}█{fg}█{bg}║   {fg}█{fg}█{bg}║{fg}█{fg}█{bg}╔{fg}█{fg}█{bg}╗ {fg}█{fg}█{bg}║
                                        {fg}█{fg}█{bg}║{bg}╚{fg}█{fg}█{bg}╔{bg}╝{fg}█{fg}█{bg}║{fg}█{fg}█{bg}║   {fg}█{fg}█{bg}║{fg}█{fg}█{bg}║   {fg}█{fg}█{bg}║{fg}█{fg}█{bg}║{bg}╚{fg}█{fg}█{bg}╗{fg}█{fg}█{bg}║
                                        {fg}█{fg}█{bg}║ {bg}╚═{bg}╝ {fg}█{fg}█{bg}║{bg}╚{fg}█{fg}█{fg}█{fg}█{fg}█{fg}█{bg}╔{bg}╝{bg}╚{fg}█{fg}█{fg}█{fg}█{fg}█{fg}█{bg}╔{bg}╝{fg}█{fg}█{bg}║ {bg}╚{fg}█{fg}█{fg}█{fg}█{bg}║
                                        {bg}╚═{bg}╝     {bg}╚═{bg}╝ {bg}╚═════{bg}╝  {bg}╚═════{bg}╝ {bg}╚═{bg}╝  {bg}╚═══{bg}╝
"""
    print(moon_ascii)


def menu():
    print(f"                    {color1}[{fg}1{color1}] {fg}Create Note                                         Notes List {color2}[{fg}2{color2}]")
    option_choice = input(f"\n{bg}[{fg}{project_name}{bg}]{fg} | {bg}Choice{fg}: ")
    cls()
    if option_choice == "1":
        create_notes()
    elif option_choice == "2":
        note_list()


# login()
ascii_art()
menu()

# # vars and console title (!IMPORTANT)