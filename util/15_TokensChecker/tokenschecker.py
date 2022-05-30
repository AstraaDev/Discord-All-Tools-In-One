import requests, time
from colorama import Fore
from util.plugins.commun import * 

clear()
tokenscheckertitle()
setTitle("Mass Tokens Checker")

print(f"{y}[{w}+{y}]{w} Enter the file path (It must be in .txt and it must contain 1 token per line): ")
global filePath, tokens, donetokenlist
filePath = input(f"{y}[{b}#{y}]{w} File path: ")
sort = "\""
for sort in sort:
    filePath = filePath.replace(sort, '')
donetokenlist = []

def load_token():
    loaded_amount = 0
    try:
        checklist = open(f"{filePath}", "r")
        tokenlist = checklist.readlines()
        checklist.close()
        for token in tokenlist:
            donetokenlist.append(token[:-1])
            loaded_amount += 1
        print(f"\n{y}[{Fore.LIGHTGREEN_EX}!{y}]{w} {loaded_amount} Tokens Loaded")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to start""")
    except:
        print(f"          {y}[{Fore.LIGHTRED_EX}!{y}]{w} File not found")
        input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()


def checkvalidity():
    valid = 0
    locked = 0
    invalid = 0
    totaltoken = 0
    validtokens = []
    invite_code = "cQ7xRv3S5x"
    clear()
    for token in donetokenlist:
        while True:
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
            r1 = str(r1)
            if "429" not in r1:
                break
            if "429" in r1:
                print(f'{y}[{Fore.LIGHTRED_EX}!{y}]{w} Rate limited...')
                time.sleep(.3)
        r1 = str(r1)
        totaltoken = int(totaltoken) + 1
    
        if "400" in r1:
            print(f'{Fore.RED}[!] Invalid: {w}'+token)
            invalid += 1
    
        if "200" in r1:
            while True:
                r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": token})
                r = str(r)
                if "429" not in r:
                    break
                if "429" in r:
                    print(f'{y}[{Fore.LIGHTRED_EX}!{y}]{w} Rate limited...')
            r = str(r)
    
            if "200" in r:
                print(f'{Fore.LIGHTGREEN_EX}[!] Valid: {w}'+token)
                validtokens.append(token)
                validfile = open("output/valids.txt", "a")
                validfile.writelines(token+"\n")
                validfile.close()
                valid += 1
    
            if "403" in r:
                print(f'{Fore.LIGHTRED_EX}[!] Verification required: {w}'+ token)
                locked += 1

    print(f"""\n
{y}[{b}+{y}]{w} Results:\n
          {y}[{Fore.LIGHTGREEN_EX}!{y}]{w} Valid: {valid}""")
    if valid >=1:
        print("               You can find the list of valid tokens in output/valids.txt")
    print(f"""          {y}[{Fore.LIGHTRED_EX}!{y}]{w} Verification required: {locked}
          {y}[{Fore.RED}!{y}]{w} Invalid: {invalid}""")

    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

load_token()
checkvalidity()
