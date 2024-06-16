import requests
import json
from colorama import Fore

# URL of the API endpoint
url = 'https://kretaglobalmobileapi2.ekreta.hu/api/v3/Institute'

# Header with the API key
headers = {
    'apiKey': '7856d350-1fda-45f5-822d-e1a2f3f1acf0'
}

# Make the HTTP GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Save the JSON data to a file
    with open('iskolak.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(Fore.GREEN + f"[+] Data has been saved to {Fore.CYAN}[iskolak.json]" + Fore.RESET)
else:
    print(Fore.RED + f"[-] Failed to retrive data, HTTP code: {response.status_code}"+ Fore.RESET)