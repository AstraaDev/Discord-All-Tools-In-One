import json, requests, time, threading, os, ctypes
from colorama import Fore

class Main:
    def __init__(self):
        ctypes.windll.kernel32.SetConsoleTitleW("Mass Report - Made by Astraa")
        massreport()
        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the ID of the server where the message to be reported is located: """)
        self.GUILD_ID = str(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Guild ID: """))
        print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the ID of the channel in which the message to be reported is located: """)
        self.CHANNEL_ID = str(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Channel ID: """))
        print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the ID of the message to be reported: """)
        self.MESSAGE_ID = str(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Message ID: """))
        print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Choose the reason for the report: """)
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }1{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Illegal content""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }2{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Harassment""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }3{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Spam or phishing links""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }4{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Self-harm""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }5{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } NSFW content\n""")
        REASON = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Choice: """)

        if REASON == '1':
            self.REASON = 0
        elif REASON == '2':
            self.REASON = 1
        elif REASON == '3':
            self.REASON = 2
        elif REASON == '4':
            self.REASON = 3
        elif REASON == '5':
            self.REASON = 4
        else:
            print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Your request is invalid !""")
            time.sleep(2)
            exit(0)

        self.RESPONSES = {f"""
            401: Unauthorized: {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Invalid Discord token,
            Missing Access: {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Missing access to channel or guild,
            You need to verify your account in order to perform this action: {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Unverified"""}
        self.sent = 0
        self.errors = 0

    def _reporter(self):
        report = requests.post(
            'https://discordapp.com/api/v8/report', json={
                'channel_id': self.CHANNEL_ID,
                'message_id': self.MESSAGE_ID,
                'guild_id': self.GUILD_ID,
                'reason': self.REASON
            }, headers={
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'sv-SE',
                'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                'Content-Type': 'application/json',
                'Authorization': self.TOKEN
            }
        )
        if (status := report.status_code) == 201:
            self.sent += 1
            print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Reported successfully""")
        elif status in (401, 403):
            self.errors += 1
            print(self.RESPONSES[report.json()['message']])
        else:
            self.errors += 1
            print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Error: {report.text} | Status Code: {status}""")

    def _update_title(self):
        while True:
            os.system(f'title [Discord Reporter] - Sent: {self.sent} ^| Errors: {self.errors}')
            time.sleep(0.1)

    def _multi_threading(self):
        threading.Thread(target=self._update_title).start()
        while True:
            if threading.active_count() <= 300:
                time.sleep(1)
                threading.Thread(target=self._reporter).start()

    def setup(self):
        recognized = None
        if os.path.exists(config_json := 'temp/Config.json'):
            with open(config_json, 'r') as f:
                try:
                    data = json.load(f)
                    self.TOKEN = data['discordToken']
                except (KeyError, json.decoder.JSONDecodeError):
                    recognized = False
                else:
                    recognized = True
        else:
            recognized = False

        if not recognized:
            print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter your token: """)
            self.TOKEN = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """)
            with open(config_json, 'w') as f:
                json.dump({'discordToken': self.TOKEN}, f)
        print()
        self._multi_threading()

main = Main()
main.setup()