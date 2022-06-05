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

    try:
        res = requests.get(f"https://discord.com/api/v9/invites/{invitelink}")
    except:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()

    if res.status_code == 200:
        res_json = res.json()
        invite_link = f'https://discord.gg/{res_json["code"]}'
        invite_channel_name = res_json["channel"]["name"]
        invite_channel_id = res_json["channel"]["id"]
        invite_expires_at = res_json["expires_at"]

        inviter_username = f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'
        inviter_user_id = res_json["inviter"]["id"]

        server_name = res_json["guild"]["name"]
        server_id = res_json["guild"]["id"]
        banner = res_json["guild"]["banner"]
        description = res_json["guild"]["description"]
        custom_invite_link = res_json["guild"]["vanity_url_code"]
        verification_level = res_json["guild"]["verification_level"]
        splash = res_json["guild"]["splash"]
        features = res_json["guild"]["features"]

        print(f"""\n{y}[{b}#{y}]{w} Invitation Information:""")
        print(f"""          {y}[{w}+{y}]{w} Invite Link: {invite_link}""")
        print(f"""          {y}[{w}+{y}]{w} Channel: {invite_channel_name} ({invite_channel_id})""")
        print(f"""          {y}[{w}+{y}]{w} Expiration Date: {invite_expires_at}\n\n""")

        print(f"""{y}[{b}#{y}]{w} Inviter Information:""")
        print(f"""          {y}[{w}+{y}]{w} Username: {inviter_username}""")
        print(f"""          {y}[{w}+{y}]{w} User ID: {inviter_user_id}\n\n""")

        print(f"""{y}[{b}#{y}]{w} Server Information:""")
        print(f"""          {y}[{w}+{y}]{w} Name: {server_name}""")
        print(f"""          {y}[{w}+{y}]{w} Server ID: {server_id}""")
        print(f"""          {y}[{w}+{y}]{w} Banner: {banner}""")
        print(f"""          {y}[{w}+{y}]{w} Description: {description}""")
        print(f"""          {y}[{w}+{y}]{w} Custom Invite Link: {custom_invite_link}""")
        print(f"""          {y}[{w}+{y}]{w} Verification Level: {verification_level}""")
        print(f"""          {y}[{w}+{y}]{w} Splash: {splash}""")
        print(f"""          {y}[{w}+{y}]{w} Features: {features}""")
        
    else:
        input(f"""          {y}[{Fore.LIGHTRED_EX }#{y}]{w} An error occurred while sending request""")
        main()
    
    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

serverlookup()
