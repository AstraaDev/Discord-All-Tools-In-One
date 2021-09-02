import os, sys, time, os.path, pyperclip, pyautogui, ctypes
from colorama import Fore
from selenium import webdriver

def main() :   
    ctypes.windll.kernel32.SetConsoleTitleW("AutoLogin - Made by Astraa")
    autologin()
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } You must use a basic revolution (1920/1080 16:9)\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Do not touch your mouse or keyboard while running the script\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter a valid token (minimum 59 characters must be entered)\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the token of the account you want to connect to: """)
    print()
    entertoken = str(input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """))
    if len(entertoken) >= 59:
        driver = webdriver.Chrome(executable_path=r'Additional_File/11_AutoLogin/chromedriver.exe')
        driver.maximize_window()
        pyperclip.copy("""function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }""")
        driver.get('https://discord.com/login')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 'i')
        time.sleep(1)
        pyautogui.click(x=1540, y=130, button='left')
        pyautogui.click(x=1410, y=155, button='left')
        pyautogui.click(x=1400, y=177, button='left')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('login')
        pyperclip.copy("('")
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy(entertoken)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy("')")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(x=525, y=700, button='left')
        pyautogui.click(x=1906, y=128, button='left')
        time.sleep(5)
        if driver.current_url == 'https://discord.com/channels/@me':
            print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Connection Established""")
        else:
            print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Connection Failed""")
            driver.close()
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to exit""")
        exit(0)
    else:
        print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } There is a problem with your Token.""")
        time.sleep(2)
        os.system('cls')
        exit(0)

main()