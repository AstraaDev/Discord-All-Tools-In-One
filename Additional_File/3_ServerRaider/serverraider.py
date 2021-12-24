import os, time, requests, os.path, json, threading, string, random, pyautogui, re, http.client
import emoji as ej

def serverraider():

    os.system('cls')
    raidtitle()
    ur = 'https://discord.com/api/v9/channels/messages'
    if not os.path.exists('tokens.txt'):
        fichier = open("tokens.txt", "a")
        fichier.close
        verif = input(f"""{y}[{b}#{y}]{w} Write your tokens in the file "tokens.txt" then ENTER to launch the raid""")

    tokens = open('tokens.txt', 'r').read().splitlines()
    print()
    def randstr(lenn):
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        text = ''
        for i in range(0, lenn):
            text += alpha[random.randint(0, len(alpha) - 1)]
        return text
    def spammer():
        valid = 0
        invalid = 0
        tokens = open('tokens.txt', 'r').read().splitlines()
        choiceraid = input(f"""{y}[{b}#{y}]{w} Choice: """)
        if choiceraid == 'spam':
            tokens = open("tokens.txt", "r").read().splitlines()
            print(f"""{y}[{w}+{y}]{w} Enter the channel ID: """)
            channel = input(f'{y}[{b}#{y}]{w} Channel ID: ')
            print(f"""{y}[{w}+{y}]{w} Enter your message: """)
            mess = input(f'{y}[{b}#{y}]{w} Message: ')
            print(f"""{y}[{w}+{y}]{w} Enter a delay between each message: """)
            delay = float(input(f'{y}[{b}#{y}]{w} Delay: '))
            ch = input(f'{y}[{b}#{y}]{w} Do you want append random string (Y/N) ? ').lower()
            def spam(token, mess):
                if ch == 'y':
                    mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
                else:
                    pass
                url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
                payload = {"content": mess, "tts": False}
                header = {"authorization": token,
                        "accept": "*/*",
                        "accept-language": "en-GB",
                        "content-length": "90",
                        "content-type": "application/json",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    time.sleep(delay)
                    src = requests.post(url, headers=header, json=payload)
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                        invalid += 1
                        time.sleep(float(ratelimit['retry_after']))
                    elif src.status_code == 200:
                        print(f'{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} {mess} sent')
                        valid += 1
                    elif src.status_code == 401:
                        print(f'{y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid token')
                        invalid += 1
                    elif src.status_code == 404:
                        print(f'{y}[{Fore.LIGHTRED_EX }!{y}]{w} Not found')
                        invalid += 1
                    elif src.status_code == 403:
                        print(f'{y}[{Fore.LIGHTRED_EX }!{y}]{w} Token havent got access to this channel')
                        invalid += 1
            def thread():
                text = mess
                for token in tokens:
                    threading.Thread(target=spam, args=(token, text)).start()
            start = input(f'{y}[{b}#{y}]{w} Press any key to start')
            start = thread()
            os.system('cls' if os.name == 'nt' else 'clear')
            serverraidertitle()
            print(f'{y}[{b}#{y}]{w} Successfully spam guild')
            print(f"""\n{y}[{b}+{y}]{w} Results:\n\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Message Sended: {valid}\n\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} Message Error: {invalid}""")
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'dmspam':
            def DMSpammer(idd, message, token):
                header = {
                    'Authorization': token,
                    "accept": "*/*",
                    "accept-language": "en-GB",
                    "content-length": "90",
                    "content-type": "application/json",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                payload = {'recipient_id': idd}
                r1 = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=header,
                                json=payload)
                if chrr == 'y':
                    message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
                elif chrr == 'n':
                    pass
                else:
                    pass
                payload = {"content": message, "tts": False}
                j = json.loads(r1.content)
                valid = 0
                invalid = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    r2 = requests.post(f"https://discordapp.com/api/v9/channels/{j['id']}/messages",
                                    headers=header, json=payload)
                    if r2.status_code == 429:
                        ratelimit = json.loads(r2.content)
                        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                        invalid += 1
                        time.sleep(float(ratelimit['retry_after']))
                    elif r2.status_code == 200:
                        print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} DM sent to {idd}!")
                        valid += 1
            tokens = open("tokens.txt", "r").read().splitlines()
            print(f"""{y}[{w}+{y}]{w} Enter the user ID: """)
            user = input(f'{y}[{b}#{y}]{w} User ID: ')
            print(f"""{y}[{w}+{y}]{w} Enter your message: """)
            message = input(f'{y}[{b}#{y}]{w} Message: ')
            chrr = input(f'{y}[{b}#{y}]{w} Do you want append random string (Y/N) ? ').lower()
            def thread():
                for token in tokens:
                    threading.Thread(target=DMSpammer, args=(user, message, token)).start()
            start = input(f'{y}[{b}#{y}]{w} Press any key to start')
            start = thread()
            os.system('cls' if os.name == 'nt' else 'clear')
            serverraidertitle()
            print(f'{y}[{b}#{y}]{w} Successfully spam user')
            print(f"""\n{y}[{b}+{y}]{w} Results:\n\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Message Sended: {valid}\n\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} Message Error: {invalid}""")
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'fspam':
            def friender(token, user):
                os.system('cls' if os.name == 'nt' else 'clear')
                valid = 0
                invalid = 0
                try:
                    user = user.split("#")
                    headers = {
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-GB",
                        "authorization": token,
                        "content-length": "90",
                        "content-type": "application/json",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                    }
                    payload = {"username": user[0], "discriminator": user[1]}
                    src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                        json=payload)
                    if src.status_code == 204:
                        print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Friend request sent to {user[0]}#{user[1]}!")
                        valid += 0
                except Exception as e:
                    print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error: {e}!")
                    invalid += 1
            print(f"""{y}[{w}+{y}]{w} Enter the Username#Tag: """)
            user = input(f"{y}[{b}+{y}]{w} Username#Tag: ")
            tokens = open("tokens.txt", "r").read().splitlines()
            print(f"""{y}[{w}+{y}]{w} Enter a delay between each message: """)
            delay = float(input(f'{y}[{b}#{y}]{w} Delay: '))
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=friender, args=(token, user)).start()
            start = input(f'{y}[{b}#{y}]{w} Press any key to start')
            os.system('cls' if os.name == 'nt' else 'clear')
            serverraidertitle()
            print(f'{y}[{b}#{y}]{w} Successfully spam user')
            print(f"""\n{y}[{b}+{y}]{w} Results:\n\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Friend Request Sended: {valid}\n\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} Friend Request Error: {invalid}""")
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'rspam':
            def reaction(chd, iddd, start, org, token):
                headers = {'Content-Type': 'application/json',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US',
                        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        'DNT': '1',
                        'origin': 'https://discord.com',
                        'TE': 'Trailers',
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                        'authorization': token,
                        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                        }
                emoji = ej.emojize(org, use_aliases=True)
                a = requests.put(
                    f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                    headers=headers)
                if a.status_code == 204:
                    print(f"{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Reaction {org} added! ")
                    valid += 1
                else:
                    print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error")
                    invalid += 1
            tokens = open('tokens.txt', 'r').read().splitlines()
            print(f"""{y}[{w}+{y}]{w} Enter the channel ID: """)
            chd = input(f'{y}[{b}#{y}]{w} Channel ID: ')
            print(f"""{y}[{w}+{y}]{w} Enter the message ID: """)
            iddd = input(f'{y}[{b}#{y}]{w} Message ID: ')
            print(f"""{y}[{w}+{y}]{w} Enter the emoji: """)
            emoji = input(f'{y}[{b}#{y}]{w} Emoji: ')
            start = input(f'{y}[{b}#{y}]{w} Press any key to start')
            valid = 0
            invalid = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            for token in tokens:
                threading.Thread(target=reaction, args=(chd, iddd, start, emoji, token)).start()
            os.system('cls' if os.name == 'nt' else 'clear')
            serverraidertitle()
            print(f'{y}[{b}#{y}]{w} Successfully spam guild')
            print(f"""\n{y}[{b}+{y}]{w} Results:\n\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Reaction added: {valid}\n\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} Reaction Error: {invalid}""")
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()
            
        elif choiceraid == 'tspam':
            print(f"""{y}[{w}+{y}]{w} Enter your message: """)
            message = input(f'{y}[{b}#{y}]{w} Message: ')
            print(f"""{y}[{w}+{y}]{w} Enter the amount of messages: """)
            amount = int(input(f"{y}[{b}+{y}]{w} Amount: "))
            print(f"""{y}[{w}+{y}]{w} Enter a delay between each message: """)
            delay = float(input(f'{y}[{b}#{y}]{w} Delay: '))
            print(f"{y}[{b}+{y}]{w} 10 seconds to typing spam")
            for seconds in range(10, 0, -1):
                print(seconds)
                time.sleep(1)
            print(f'{y}[{b}#{y}]{w} Spamming...')
            for i in range(0, amount):
                if message != "":
                    pyautogui.typewrite(message)
                    pyautogui.press("enter")
                else:
                    pyautogui.hotkey("ctrl", "v")
                    pyautogui.press("enter")
                print(f'{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} {message} sent')
                time.sleep(delay)
            print(f'{y}[{b}#{y}]{w} Successfully spam guild')
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'join':
            http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
            tokens = open("tokens.txt", "r").read().splitlines()
            valid = 0
            invalid = 0
            def join(invite, token):
                token = token.replace("\r", "")
                token = token.replace("\n", "")
                headers = {
                    ":authority": "discord.com",
                    ":method": "POST",
                    ":path": "/api/v9/invites/" + invite,
                    ":scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US",
                    "Authorization": token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                rrr = requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)
                if rrr.status_code == 204 or 200:
                    print(f'{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} User Joined')
                    valid += 1
                else:
                    print(f'{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error')
                    invalid += 1
            print(f"""{y}[{w}+{y}]{w} Enter the discord server invite: """)
            invite = input(f"{y}[{w}+{y}]{w} Invite: ")
            invite = invite.replace("https://discord.gg/", "")
            invite = invite.replace("discord.gg/", "")
            invite = invite.replace("https://discord.com/invite/", "")
            print(f"""{y}[{w}+{y}]{w} Enter a delay between each message: """)
            delay = float(input(f'{y}[{b}#{y}]{w} Delay: '))
            os.system('cls' if os.name == 'nt' else 'clear')
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=join, args=(invite, token)).start()
            time.sleep(3)
            bj = input(f'{y}[{w}+{y}]{w} Do you want to bypass member screening (Y/N) ? ').lower
            if bj == 'y':
                headers = {
                    ":authority": "discord.com",
                    ":method": "POST",
                    ":path": "/api/v9/invites/" + invite,
                    ":scheme": "https",
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US",
                    "Authorization": token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                def bps(invite_code, guild_id):
                    vur = f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false&invite_code=" + invite_code
                    rr = requests.get(vur, headers=headers).json()
                    data = {}
                    data['version'] = rr['version']
                    data['form_fields'] = rr['form_fields']
                    data['form_fields'][0]['response'] = True
                    fv = f"https://discord.com/api/v9/guilds/{str(guild_id)}/requests/@me"
                    requests.put(fv, headers=headers, json=data)
                print(f"""{y}[{w}+{y}]{w} Enter the guild ID: """)
                sID = input(f'{y}[{b}#{y}]{w} Guild ID: ')
                tokens = open('tokens.txt', 'r').read().splitlines()
                for token in tokens:
                    threading.Thread(target=bps, args=(invite, sID)).start()
            elif b == 'n':
                pass
            os.system('cls' if os.name == 'nt' else 'clear')
            serverraidertitle()
            print(f'{y}[{b}#{y}]{w} Successfully join guild')
            print(f"""\n{y}[{b}+{y}]{w} Results:\n\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} User Joined: {valid}\n\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} User Error: {invalid}""")
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'leave':
            token = open("tokens.txt", "r").read().splitlines()
            print(f"""{y}[{w}+{y}]{w} Enter the guild ID: """)
            ID = input(f'{y}[{b}#{y}]{w} Guild ID: ')
            apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)
            with open('tokens.txt', 'r') as handle:
                tokens = handle.readlines()
                for i in tokens:
                    token = i.rstrip()
                    headers = {
                        'Authorization': token,
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    requests.delete(apilink, headers=headers)
                print(f'\t[#] Successfully left guild\n')
            print(f'{y}[{b}#{y}]{w} Successfully left guild')
            input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()

        elif choiceraid == 'exit':
            print()
            main()

        elif choiceraid == 'help':
            print(f"""\n\tTool Command\tDescription\n\t------------\t-----------\n\tspam\t\tSpammer\n\tdmspam\t\tDM Spammer\n\tfspam\t\tFriends Spammer\n\trspam\t\tReactions Spammer\n\ttspam\t\tTypings Spammer\n\tjoin\t\tJoiner\n\tleave\t\tLeaver\n""")

        else:
            print(f"""\tInvalid command\n""")
            main()
      
    spammer()
serverraider()