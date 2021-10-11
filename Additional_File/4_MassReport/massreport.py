import json, requests, time, threading, os, ctypes
from tkinter.constants import W
from colorama import Fore

class massreport:
    def __init__(self):
        os.system('cls')
        massreporttitle()
        print(f"""{y}[{w}+{y}]{w} Enter the ID of the server where the message to be reported is located: """)
        self.GUILD_ID = str(input(f"""{y}[{b}#{y}]{w} Guild ID: """))
        print(f"""\n{y}[{w}+{y}]{w} Enter the ID of the channel in which the message to be reported is located: """)
        self.CHANNEL_ID = str(input(f"""{y}[{b}#{y}]{w} Channel ID: """))
        print(f"""\n{y}[{w}+{y}]{W} Enter the ID of the message to be reported: """)
        self.MESSAGE_ID = str(input(f"""{y}[{b}#{y}]{w} Message ID: """))
        print(f"""\n{y}[{w}+{y}]{w} Choose the reason for the report: """)
        print(f"""          {y}[{w}1{y}]{w} Illegal content""")
        print(f"""          {y}[{w}2{y}]{w} Harassment""")
        print(f"""          {y}[{w}3{y}]{w} Spam or phishing links""")
        print(f"""          {y}[{w}4{y}]{w} Self-harm""")
        print(f"""          {y}[{w}5{y}]{w} NSFW content\n""")
        REASON = input(f"""{y}[{b}#{y}]{w} Choice: """)

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
            print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Your request is invalid !""")
            time.sleep(2)
            main()

        self.RESPONSES = {f"""
            401: Unauthorized: {y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid Discord token,
            Missing Access: {y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing access to channel or guild,
            You need to verify your account in order to perform this action: {y}[{Fore.LIGHTRED_EX }!{y}]{w} Unverified"""}
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
            print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Reported successfully""")
        elif status in (401, 403):
            self.errors += 1
            print(self.RESPONSES[report.json()['message']])
        else:
            self.errors += 1
            print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {report.text} | Status Code: {status}""")

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
            print(f"""\n{y}[{w}+{y}]{w} Enter your token: """)
            self.TOKEN = input(f"""{y}[{b}#{y}]{w} Token: """)
            with open(config_json, 'w') as f:
                json.dump({'discordToken': self.TOKEN}, f)
        print()
        self._multi_threading()

mr = massreport()
mr.setup()
