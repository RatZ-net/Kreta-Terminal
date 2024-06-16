import json
from colorama import Fore
import time
import os
import datetime
import subprocess
import requests
import hmac
import base64
import hashlib



c = Fore

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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exec(fileformat, name):
    subprocess.run([fileformat, name])

class KretaURL:
    nonce = "https://idp.e-kreta.hu/nonce"

def getNonce(nonce):
    url = "https://idp.e-kreta.hu/nonce"  # Replace with KretaURL.nonce if it's defined somewhere else
    
    try:
        gnonce = requests.get(url)
        gnonce.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        nonce = gnonce.text
        # If request is successful, return the nonce
        return nonce

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Failed to get NONCE: {e}" + Fore.RESET)
        return None

class Info:
    user = None
    passw = None
    ins = None
    TOKEN = None
    RTOKEN = None


with open('userdata.json', 'r') as json_file:
        try:
            user_data = json.load(json_file)
            Info.user = user_data.get('usr')
            Info.passw = user_data.get('pass')
            Info.ins = user_data.get('ins')
        except json.JSONDecodeError:
            print(Fore.RED + f"[-] ERROR while decoding {c.CYAN}[userdata.json]" + Fore.RESET)

def getAuthP(AuthP):
    user = Info.user
    Ins = Info.ins
    nonce = getNonce(None)
    key = "baSsxOwlU1jM"
    username = user.upper()
    instituteCode = Ins.upper()
    
    try:
        message = f"{instituteCode}{nonce}{username}".encode('utf-8')
        key_bytes = key.encode('utf-8')
        hmac_sha512 = hmac.new(key_bytes, message, hashlib.sha512)
        digest = hmac_sha512.digest()
        AuthP = base64.b64encode(digest).decode('utf-8')

        return AuthP

    except:
        print(Fore.RED + f"[-] Failed to get AuthP " + Fore.RESET)
        return None
    

def getAuth():
    url = "https://idp.e-kreta.hu/connect/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Authorizationpolicy-Key": getAuthP(None),  # Optional header
        "X-Authorizationpolicy-Version": "v2",               # Optional header
        "X-Authorizationpolicy-Nonce": getNonce(None)  # Optional header
    }
    payload = {
        "userName": Info.user,
        "password": Info.passw,
        "institute_code": Info.ins,
        "grant_type": "password",
        "client_id": "kreta-ellenorzo-mobile-android"
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        print(c.GREEN + f"[+] Server has sent the TOKEN" + c.RESET)

        with open('auth.json', 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
            print(c.GREEN + f"[+] Token saved in {c.CYAN}[auth.json]" + c.RESET)

        with open('auth.json', 'r') as json_file:
            try:
             user_data = json.load(json_file)
             Info.TOKEN = user_data.get('access_token')
             Info.RTOKEN = user_data.get('refresh_token')
             print(Fore.GREEN + f"[+] Loaded {c.CYAN}[auth.json]" + Fore.RESET)
            except json.JSONDecodeError:
                print(Fore.RED + f"[-] ERROR while decoding {c.CYAN}[auth.json]" + Fore.RESET)

    except requests.exceptions.RequestException as e:
        print(c.RED + f"[-] ERROR while getting TOKEN: {e}")

        


def getData():
    url = f"https://klik200951002.e-kreta.hu/ellenorzo/v3/sajat/GondviseloAdatlap"
    headers = {
        #"apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463",
        "Authorization": Info.TOKEN
    }


    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        print(c.GREEN + f"[+] Data recived from server" + c.RESET)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(c.RED + f"[-] ERROR getting DATA: {e}")


if __name__ == "__main__":
    clear()
    logo()
    print(c.GREEN + f"[+] {c.CYAN}[getAuth.py]{c.GREEN} has started" + c.RESET)
    time.sleep(1)
    getAuth()
    getData()

