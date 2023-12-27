#!/usr/bin/ python3

import os,requests,json,random
import getpass
import subprocess
os.system("clear")
username = getpass.getuser()

os.system("git pull")
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
RESET = "\033[0m"
BOLD	 = "\033[1m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
color = [RED,GREEN,BLUE,MAGENTA,CYAN,ORANGE]
rand = random.choice(color)
def update_scr():
    os.system("cd $HOME && rm -rf x_famework && git clone https://github.com/zaypaihtet/x_famework/ && cd x_famework $$ python3 main.py ")

ver = open("./src/version")
version =  ver.read()

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
    print(f"{BOLD}{YELLOW}This is for educational purposes only and I will not be held responsible if anything happens")



def menu():
    banner()
    print("type help to usage")
    while True:
        option = input(f"{BOLD}{GREEN}{username}@X_framwwork >> {RESET}")
        if option in ["help","HELP","Help","option"]:
            list = f"""{BOLD}
            [1] -- Track Ip 
            [Type] -> Track
            [2] -- SMS Spam
            [Type] -> SMS
            [3] -- Phishing 
            [Type] -> Phishing
            [4] -- Gmail Clone
            [Type] -> Gmail
            [5] -- Update
            [Type] -> update
            """
            print(list)
        elif option in ["1","Track"]:
            subprocess.run(['python3',"./src/trackip.py" ], check=True)
        elif option in ["2","SMS"]:
            os.system("cd src && python3 sms.py")
        elif option in ["exit","break","end"]:
            print(f"{BOLD}Thanks For Using My Tool")
            exit()
        elif option in ["3","Phishing"]:
            os.system("cd src && python3 phishing.py")
        elif option in ["4","Gmail"]:
            os.system("cd src && python3 gmail.py")
        elif option in ["ls","clear"]:
            os.system(f"{option}")
            banner()
        elif option in ['banner']:
            banner()
        elif option in ['update','5']:
            update_scr()
        else:
            print(f"{RED}Wrong input...")



menu()