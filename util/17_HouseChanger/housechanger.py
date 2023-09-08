import requests
from colorama import Fore
from util.plugins.commun import * 

def hypesquadchanger():
    setTitle("HypeSquad Changer")
    clear()
    housechangertitle()
    print(f"{y}[{b}#{y}]{w} Which house do you want to be part of:\n\n\n          {y}[{w}01{y}]{w} Bravery\n\n          {y}[{w}02{y}]{w} Brilliance\n\n          {y}[{w}03{y}]{w} Balance\n\n\n")
    print(f"{y}[{w}+{y}]{w} Enter your House choice")
    house = input(f"{y}[{b}#{y}]{w} Choice: ").lstrip("0")
    print(f"\n{y}[{w}+{y}]{w} Enter the token of the account you want to change HypeSquad House")
    token = str(input(f"{y}[{b}#{y}]{w} Token: "))
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} Invalid token")
        input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
        main()
    else:
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if house == "1": payload = {'house_id': 1}
        elif house == "2": payload = {'house_id': 2}
        elif house == "3": payload = {'house_id': 3}
        else:
            print(f"          {y}[{Fore.LIGHTRED_EX }#{y}]{w} Invalid Choice")
            input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
            main()
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        if r.status_code == 204:
          print(f" \n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Hypesquad House changed")
          input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
          main()
        else:
            print(f" \n{y}[{Fore.LIGHTRED_EX }!{y}]{w} An error occurred, please retry")
            input(f"\n{y}[{b}#{y}]{w} Press ENTER to exit")
            main()

     
          
hypesquadchanger()
