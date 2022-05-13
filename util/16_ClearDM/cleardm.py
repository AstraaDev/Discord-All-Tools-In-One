import os, os.path, discord
from discord.ext import commands
from colorama import Fore
from util.plugins.commun import * 

setTitle("Clear DM")
clear()
cleardmtitle()
print(f"""{y}[{w}+{y}]{w} Enter your token""")
token = input(f"""{y}[{b}#{y}]{w} Token: """)
print(f"""\n{y}[{b}#{y}]{w} Write "!clear" in one of your DMs to delete your messages""")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"\n{y}[{w}+{y}]{w} Removed {passed} messages with {failed} fails")
    input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()

bot.run(token, bot=False)