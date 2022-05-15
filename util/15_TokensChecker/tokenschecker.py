import requests
from colorama import Fore
from util.plugins.commun import * 

clear()
tokenscheckertitle()
setTitle("Mass Tokens Checker")

print(f"{y}[{w}+{y}]{w} Enter the file path (It must be in .txt and it must contain 1 token per line): ")
global filePath, tokens
filePath = input(f"{y}[{b}#{y}]{w} File path: ")
tokens = []

def load_token():
    try:
        with open(f'{filePath}', 'r') as f:   
            for x in f.readlines():
                tokens.append(x.replace('\n',''))
    except:
        print(f"          {y}[{Fore.LIGHTRED_EX}!{y}]{w} File not found")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()
        

def checkvalidity():
    valid = 0
    needverif = 0
    invalid = 0
    clear()
    for x in tokens:
        setTitle(f"Mass Tokens Checker - {valid} Valid | {needverif} Verification required | {invalid} Invalid")
        src = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': x})
        if src.status_code == 200:
            res_json = src.json()
            verified = res_json['verified']
            if verified == True:
                print(f'{Fore.LIGHTGREEN_EX}[!] Valid: {w}'+x)
                with open("output/valids.txt", "a") as save:
                    save.write(x+"\n")
                    valid += 1
            else:
                print(f'{Fore.LIGHTRED_EX}[!] Verification required: {w}'+x)
                needverif += 1
        else:
            print(f'{Fore.RED}[!] Invalid: {w}'+x)
            invalid += 1
    
    print(f"""\n
{y}[{b}+{y}]{w} Results:\n
          {y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Valid: {valid}""")
    if valid >=1:
        print("               You can find the list of valid tokens in temp/valids.txt")
    print(f"""          {y}[{Fore.LIGHTRED_EX}!{y}]{w} Verification required: {needverif}
          {y}[{Fore.RED}!{y}]{w} Invalid: {invalid}""")

    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

load_token()     
checkvalidity()
