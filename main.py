#!/usr/bin/env python3
import os,requests,json,random
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
color = [RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN]
rand = random.choice(color)
version = open("./src/version", "r")


def banner():
    print(f"""{rand}__  __  _____                                            _    
\ \/ / |  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
 \  /  | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 /  \  |  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
/_/\_\ |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ 
          
          {GREEN}Author : {CYAN}X-Coder
          {GREEN}Version :{CYAN}{version.read()}
          """

    )

banner()