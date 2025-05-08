# YOU CAN USE THIS SITE FOR TESTING https://testsafebrowsing.appspot.com/
# CREATES AN .env FILE WITH THE GOOGLE API KEY = SAFE_KEY

from pysafebrowsing import SafeBrowsing
import os
from dotenv import load_dotenv
from colorama import init, Fore

init(autoreset=True)

print(Fore.LIGHTMAGENTA_EX + r"""
  __  __       _ _      _  ___         __          ______  _     
 |  \/  |     | (_)    (_)/ _ \        \ \        / /___ \| |    
 | \  / | __ _| |_  ___ _| | | |_   _ __\ \  /\  / /  __) | |__  
 | |\/| |/ _` | | |/ __| | | | | | | / __\ \/  \/ /  |__ <| '_ \ 
 | |  | | (_| | | | (__| | |_| | |_| \__ \\  /\  /   ___) | |_) |
 |_|  |_|\__,_|_|_|\___|_|\___/ \__,_|___/ \/  \/   |____/|_.__/  
""")

print(Fore.LIGHTRED_EX + "By SuLzr1b")
print(Fore.LIGHTRED_EX + "Malicious URL checker")
print(Fore.RESET)  


load_dotenv()
API_KEY = os.getenv("SAFE_KEY")

LOG_FILE = "log_urls.txt"

if not API_KEY:
    print(Fore.RED + "Error: API key not found. Configure the .env file with SAFE_KEY.")
    exit(1)


url = input("Enter the URL of the website you want to check: ").strip()


if not url.startswith(("http://", "https://")):
    url = "http://" + url

try:
    
    s = SafeBrowsing(API_KEY)
    
    response = s.lookup_urls([url])
    
    result = response.get(url, {})
    status = "Malicious" if result.get("malicious", False) else "Safe"

    
    if result.get("malicious", False):
        print(Fore.RED + f"Attention! The {url} URL can be malicious: {result.get('threats', [])}")
    else:
        print(Fore.GREEN + f"The URL {url} looks safe!")
        
    existing_urls = set()
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                url_in_file = line.rsplit(":", 1)[0].strip()
                existing_urls.add(url_in_file)
    except FileNotFoundError:
        pass  
    
    if url not in existing_urls:
        with open(LOG_FILE, "a") as file:
            file.write(f"{url}: {result.get('threats', [])} = {status}\n")
    else:
        print(Fore.CYAN + "URL is already in the file.")

except Exception as e:
    print(Fore.RED + f"Error verifying URL: {str(e)}")
