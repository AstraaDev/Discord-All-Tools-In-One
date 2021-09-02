import requests
from colorama import Fore
import ctypes

class BlockBypass:
    ctypes.windll.kernel32.SetConsoleTitleW("ByPass Discord Block - Made by Astraa")
    def __init__(self, tokenenter, userId):
        self.channelId = None
        self.userId = userId
        self.api = 'https://discord.com/api/v8/'
        self.headers = {
            'Authorization': tokenenter,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def generateChannel(self):
        request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [ self.userId ]}, headers=self.headers)

        if request.status_code == 200:
            print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Successfully created channel\n""")
            self.channelId = request.json()['id']
            self.main()
        else:
            print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Un-Successfully Couldn\'t create a channel!""")
            print(f"""          {request.status_code} {request.json()}""")
            input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to exit""")
            exit(0)

    def sendMessage(self, message):
        request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

        if request.status_code == 200:
            print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message sent with success\n""")
        else:
            print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Un-Successfully""", request.json(), '\n')

        self.main()

    def main(self):
        content = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message To Send: """)
        self.sendMessage(content)

blockbypass()
print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Disfunction: \n""")
print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Patched\n\n\n""")
print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter your account token: """)
tokenenter = str(input(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """))
print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the UserId of the account you want to talk to: """)
userId = str(input(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } UserID: """))
print('\n')
yesnt = BlockBypass(tokenenter, userId)
yesnt.generateChannel()
yesnt.main()