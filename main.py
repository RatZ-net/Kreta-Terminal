import json
from colorama import Fore
import time
import os
import datetime
import subprocess


# Displaying logo
def logo():
    banner = """
══════════════════════════════════════════════════════════════════║ 
██████╗  █████╗ ████████╗███████╗     ███╗   ██╗███████╗████████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══███╔╝     ████╗  ██║██╔════╝╚══██╔══╝
██████╔╝███████║   ██║     ███╔╝█████╗██╔██╗ ██║█████╗     ██║   
██╔══██╗██╔══██║   ██║    ███╔╝ ╚════╝██║╚██╗██║██╔══╝     ██║   
██║  ██║██║  ██║   ██║   ███████╗     ██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝ 
Made By Lecs0                                        v0.1 [BETA]  
══════════════════════════════════════════════════════════════════║
    """
    print(Fore.BLUE + banner + Fore.RESET)
    time.sleep(3)

class Files:
    file_path = 'userdata.json'
    auth = 'auth.json'
    getAuth = 'getauth.py'
    isAuthGood = False

class Info:
    user = None
    passw = None
    ins = None
    authP = None

# Function to check if the required data exists in userdata.json
def check_user_data():
    if not os.path.exists(Files.file_path):
        return False, {}
    
    with open(Files.file_path, 'r') as json_file:
        try:
            user_data = json.load(json_file)
            Info.user = user_data.get('usr')
            Info.passw = user_data.get('pass')
            Info.ins = user_data.get('ins')
        except json.JSONDecodeError:
            return False, {}
    
    if Info.user and Info.passw and Info.ins:
        return True, user_data
    else:
        return False, {}

# Function to get user input and save it to the JSON file
def get_and_save_user_data():
    username = input(Fore.CYAN + "Enter username: ")
    time.sleep(0.4)
    password = input("Enter password: ")
    time.sleep(0.4)
    inst_c = input("Enter institute code: ")
    time.sleep(0.4)
    print(Fore.BLUE + "══════════════════════════════════════════════════════════════════║" + Fore.RESET)
    time.sleep(0.4)

    userdata = {
        "usr": username,
        "pass": password,
        "ins": inst_c
    }
    with open(Files.file_path, 'w') as json_file:
        json.dump(userdata, json_file, indent=4)
        print(Fore.GREEN + f"[+] Userdata has been saved to {Fore.CYAN}[userdata.json]" + Fore.RESET)

def UserINFO():  
    data_exists, user_data = check_user_data()  
    if data_exists:
        print(Fore.GREEN + f"[+] Saved information loaded from {Fore.CYAN}[userdata.json]" + Fore.RESET)
        time.sleep(2)
        clear()
        logo()
        print(Fore.BLUE + f"Logged in as: {Fore.CYAN}{Info.user}" + Fore.RESET)
        print(Fore.BLUE + f"Password: {Fore.CYAN}{Info.passw}" + Fore.RESET)
        print(Fore.BLUE + f"Institute Code: {Fore.CYAN}{Info.ins}" + Fore.RESET)
    else:
        print(Fore.RED + "[-] No valid user data found. Please enter new data." + Fore.RESET)
        get_and_save_user_data()


# Clear command
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exec(fileformat, name):
    subprocess.run([fileformat, name])

if __name__ == "__main__":
    clear()
    logo()
    UserINFO()
    print(Fore.BLUE + "══════════════════════════════════════════════════════════════════║" + Fore.RESET)
    time.sleep(4)
    clear()
    logo()
    print(Fore.GREEN + f"[?] Verifying {Fore.CYAN}[auth.json]" + Fore.RESET)
    time.sleep(1)
    if Files.isAuthGood == True:
        print("okay")
    elif Files.isAuthGood == False:
        print(Fore.GREEN + f"[+] Starting {Fore.CYAN}[getAuth.py]" + Fore.RESET)
        time.sleep(0.7)
        exec('python', Files.getAuth)
    else:
        print(Fore.RED + "[-] No valid data found." + Fore.RESET)

    print("Program has run! Exiting in 3 seconds...")
    time.sleep(3)
