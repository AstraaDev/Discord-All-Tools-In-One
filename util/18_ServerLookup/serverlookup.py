import requests
from colorama import Fore
from util.plugins.commun import * 

def serverlookup():
    setTitle("Server Lookup")
    clear()
    serverlookuptitle()
    print(f"""{y}[{Fore.LIGHTBLUE_EX }#{y}]{w} You can find: \n\n""")
    print(f"""          {y}[{w}+{y}]{w} Invite Link           {y}[{w}+{y}]{w} Inviter Username      {y}[{w}+{y}]{w} Guild Banner          {y}[{w}+{y}]{w} Guild Splash\n""")
    print(f"""          {y}[{w}+{y}]{w} Channel Name          {y}[{w}+{y}]{w} Inviter ID            {y}[{w}+{y}]{w} Guild Descrpition     {y}[{w}+{y}]{w} Guild Features\n""")
    print(f"""          {y}[{w}+{y}]{w} Channel ID            {y}[{w}+{y}]{w} Guild Name            {y}[{w}+{y}]{w} Custom Invite Link\n""")
    print(f"""          {y}[{w}+{y}]{w} Expiration Date       {y}[{w}+{y}]{w} Guild ID              {y}[{w}+{y}]{w} Verification Level\n\n\n\n""")
    print(f"{y}[{w}+{y}]{w} Insert end part of link of discord server link: ")
    invitelink = input(f"""{y}[{b}#{y}]{w} Invite link: """)
    clear()
    try:
        res = requests.get(f"https://discord.com/api/v9/invites/{invitelink}")
    except:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()

    if res.status_code == 200:
        res_json = res.json()

        print(f"""\n{y}[{b}#{y}]{w} Invitation Information:""")
        print(f"""          {y}[{w}+{y}]{w} Invite Link: {f'https://discord.gg/{res_json["code"]}'}""")
        print(f"""          {y}[{w}+{y}]{w} Channel: {res_json["channel"]["name"]} ({res_json["channel"]["id"]})""")
        print(f"""          {y}[{w}+{y}]{w} Expiration Date: {res_json["expires_at"]}\n""")

        print(f"""{y}[{b}#{y}]{w} Inviter Information:""")
        print(f"""          {y}[{w}+{y}]{w} Username: {f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'}""")
        print(f"""          {y}[{w}+{y}]{w} User ID: {res_json["inviter"]["id"]}\n""")

        print(f"""{y}[{b}#{y}]{w} Server Information:""")
        print(f"""          {y}[{w}+{y}]{w} Name: {res_json["guild"]["name"]}""")
        print(f"""          {y}[{w}+{y}]{w} Server ID: {res_json["guild"]["id"]}""")
        print(f"""          {y}[{w}+{y}]{w} Banner: {res_json["guild"]["banner"]}""")
        print(f"""          {y}[{w}+{y}]{w} Description: {res_json["guild"]["description"]}""")
        print(f"""          {y}[{w}+{y}]{w} Custom Invite Link: {res_json["guild"]["vanity_url_code"]}""")
        print(f"""          {y}[{w}+{y}]{w} Verification Level: {res_json["guild"]["verification_level"]}""")
        print(f"""          {y}[{w}+{y}]{w} Splash: {res_json["guild"]["splash"]}""")
        print(f"""          {y}[{w}+{y}]{w} Features: {res_json["guild"]["features"]}""")
    else:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()
    
    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

serverlookup()
