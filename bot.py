import discord
import os
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.AutoShardedBot(
  commands.when_mentioned_or("sb."),
  description="Nothing to see here!",
  intents=discord.Intents().all(),
  case_insensitive=True,
  strip_after_prefix=True,)


for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(name=f"cogs.{filename[:-3]}")



@bot.event
async def on_ready():
    activity = discord.Game(name="Playing sb.help !", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print(f"Status Changed!")
    print(f"Bot is ready!")
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


bot.run(TOKEN)