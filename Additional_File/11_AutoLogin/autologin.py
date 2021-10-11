import os, sys, time, os.path, pyperclip, pyautogui, ctypes
from colorama import Fore
from selenium import webdriver

def autologin() :
    os.system('cls')
    autologintitle()
    print(f"""{y}[{w}+{y}]{w} Enter the token of the account you want to connect to: """)
    print()
    entertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))
    print("\n\n")
    if len(entertoken) >= 59:
        driver = webdriver.Chrome(executable_path=r'Additional_File/11_AutoLogin/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            os.system('cls')
            autologintitle()
            print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Connection Failed""")
            driver.close()
        else:
            os.system('cls')
            autologintitle()
            print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Connection Established""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
        main()
    else:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} There is a problem with your Token.""")
        time.sleep(2)
        os.system('cls')
        main()

autologin()
