#!/usr/bin/ python3

import os
import requests
import random
import getpass
import subprocess

os.system("clear")
username = getpass.getuser()

os.system("git pull")
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
RESET = "\033[0m"
BOLD = "\033[1m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
color = [RED, GREEN, BLUE, MAGENTA, CYAN, ORANGE]
rand = random.choice(color)


def update_scr():
    os.system("cd $HOME && rm -rf x_famework && git clone https://github.com/zaypaihtet/x_famework/ && cd x_famework $$ python3 main.py ")


ver = open("./src/version")
version = ver.read()

update = requests.get("https://raw.githubusercontent.com/zaypaihtet/x_famework/main/src/version").text
if update == version:
    pass
else:
    update_scr()


def banner():
    os.system("figlet X Framework | lolcat")
    print(f"""{BOLD}{rand}
          {GREEN}Author : {CYAN}X-Coder
          {GREEN}Version :{CYAN}{version}
          {BLUE}Contact : {CYAN}https://t.me/x_c0d3r
          """)
    print(f"{BOLD}{YELLOW}This is for educational purposes only and I will not be held responsible if anything happens{RESET}")


def track_ip():
    subprocess.run(['python3', "./src/trackip.py"], check=True)


def sms_spam():
    os.system("cd src && python3 sms.py")


def phishing():
    os.system("cd src && python3 phishing.py")


def gmail_clone():
    os.system("cd src && python3 gmail.py")


def number_clone():
    os.system("cd src && python3 number.py")
  


def update_tool():
    update_scr()


def menu():
    banner()
    print("type help to usage")

    options = {
        "help": lambda: print(f"""{BOLD}
            [1] -- Track Ip 
            [Type] -> Track
            [2] -- SMS Spam
            [Type] -> SMS
            [3] -- Phishing 
            [Type] -> Phishing
            [4] -- Gmail Clone
            [Type] -> Gmail
            [5] -- Number Clone
            [Type] -> Number
            [6] -- Update
            [Type] -> update
            """),
        "1": track_ip,
        "Track": track_ip,
        "2": sms_spam,
        "SMS": sms_spam,
        "3": phishing,
        "Phishing": phishing,
        "4": gmail_clone,
        "Gmail": gmail_clone,
        "5": number_clone,
        "Number": number_clone,
        "6": update_tool,
        "update": update_tool,
        "ls": lambda: (banner(), os.system("ls")),
        "clear": lambda: (banner(), os.system("clear")),
        'banner': banner,
        'exit': lambda: print(f"{BOLD}Thanks For Using My Tool") or exit(),
        'break': lambda: print(f"{BOLD}Thanks For Using My Tool") or exit(),
        'end': lambda: print(f"{BOLD}Thanks For Using My Tool") or exit(),
    }

    while True:
        option = input(f"{BOLD}{GREEN}{username}@X_framwwork >> {RESET}")
        func = options.get(option.lower())
        if func:
            func()
        else:
            print(f"{RED}Wrong input...")


menu()
