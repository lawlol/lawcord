import asyncio
from lawcord.lawcord import LawcordBot

bot = LawcordBot(prefix="prefix - here", intents=32767) # 32767 = all

bot.run("token - here")
