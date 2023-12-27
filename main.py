#!/usr/bin/env python3
import os,requests,json,random
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
ver = open("./src/version")
version =  ver.read()

def banner():
    print(f"""{BOLD}{rand}__  __  _____                                            _    
\ \/ / |  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
 \  /  | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 /  \  |  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
/_/\_\ |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ 
          
          {GREEN}Author : {CYAN}X-Coder
          {GREEN}Version :{CYAN}{version}
          """)
    print(f"{BOLD}{YELLOW}This is for educational purposes only and I will not be held responsible if anything happens")

banner()