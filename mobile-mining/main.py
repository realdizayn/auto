import os
import json
import time
import pip
from config import banner


# check import module
try:
    with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']

    os.system(f"cd set-miner && wget -N --timeout 10 --connect-timeout=15 -t 1 http://{ip}/online.json")
    time.sleep(2)
    from progress.bar import ShadyBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ShadyBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests
    
    
zergpool = ["stratum+tcp://eu.luckpool.net:3960","stratum+tcp://eu.luckpool.net:3960","stratum+tcp://eu.luckpool.net:3960","stratum+tcp://eu.luckpool.net:3960"]
    
    
def runOffline():
    banner()
    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")

        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "noname"
        if cpu == "":
           cpu = "1"
        with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']

        print("\033[93m CONNECT NETWORK\033[00m\n  http://",ip)
        print("\033[1;34;40m")   
        print("\033[96m WALLET =\033[0m",wallet)
        print("\033[96m NAME   =\033[0m",name)
        print("\033[96m POOL   =\033[0m",pool)
        print("\033[96m CPU    =\033[0m",cpu)
        if pool in zergpool:

           print("\033[96m PASS   =\033[0m",password +",id="+name)
           print("\033[00m\n")

         #  time.sleep(2)
           os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu}")
       
        else:
        	
         print("\033[96m PASS   =\033[0m",password)
         print("\033[00m\n")

        # time.sleep(2)
         os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
    except:
        push = {'pool': '','wallet': '','pass': ''}
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        
        
        
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ShadyBar("\033[32m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
            
        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
