from hashlib import md5
from getpass import getpass
import os
import time


os.system("clear")
index = """\033[1;36m
    __     __          _                  _____                   
    \ \   / /         | |                / ____|                  
     \ \_/ /   _ _ __ | | _____ _ __ ___| |     _ __ _____      __
      \   / | | | '_ \| |/ / _ \ '__/ __| |    | '__/ _ \ \ /\ / /
       | || |_| | | | |   <  __/ |  \__ \ |____| | |  __/\ V  V / 
       |_| \__,_|_| |_|_|\_\___|_|  |___/\_____|_|  \___| \_/\_/  
    https://github.com/YukersCreew                        Mr.Ardi
*******************************************************************
[#] Login (#)
"""

print(index)

attempts = 0
check_username = '9e7bd94c29ffc67ad0840151aa7a99b5'
check_password = '9e7bd94c29ffc67ad0840151aa7a99b5'

while True: 
    print("\n")
    username = input("Username: ")
    password = getpass("Password: ")
    print("\n")

    if attempts == 3:
        print("Too many attempts.")
        exit()

    if md5(username.encode("utf-8")).hexdigest() == check_username:
        if md5(password.encode("utf-8")).hexdigest() == check_password:
            print("Username Betul ->", (username), "Password Betul ->", (password))
            time.sleep(2)
            os.system("clear")
            exit()
        else:
        	print("Password Salah Bosku->", (password))
        time.sleep(3)
        os.system("killall -9 com.termux")
    else:
        print("Username Salah Bosku->", (username))
        
os.system("clear")