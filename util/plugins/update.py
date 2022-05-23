import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.commun import *

def search_for_updates():
    clear()
    setTitle("@TIO Checking For Updates...")
    r = requests.get("https://github.com/AstraaDev/Discord-All-Tools-In-One/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("@TIO New Update Found!")
        print(f'''\n\n                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝\n'''.replace('█', f'{b}█{y}'))
        discserver()
        print(f'''{y}[{Fore.RED}!{y}]{w}Looks like this @TIO {THIS_VERSION} is outdated...''')
        soup = BeautifulSoup(requests.get("https://github.com/AstraaDev/Discord-All-Tools-In-One/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(f'{y}[{b}#{y}]{w} Update to the latest version (Y/N) ? ')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n{y}[{b}#{y}]{w} Updating...")
            setTitle(f'@TIO Updating...')

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("@TIO.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("@TIO.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("@TIO.zip")
                cwd = os.getcwd()+'\\@TIO\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), '@TIO.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('@TIO')
                setTitle('@TIO Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!", end="")
                os.startfile("@TIO.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/AstraaDev/Discord-All-Tools-In-One/archive/refs/heads/master.zip")
                with open("Discord-All-Tools-In-One-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Discord-All-Tools-In-One-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Discord-All-Tools-In-One-main.zip")
                cwd = os.getcwd()+'\\Discord-All-Tools-In-One-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                setTitle('@TIO Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!")
                if os.path.exists(os.getcwd()+'setup.bat'):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd()+'start.bat'):
                    os.startfile("start.bat")
                os._exit(0)
