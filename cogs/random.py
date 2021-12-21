import discord
import os
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

class Random(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  
  @commands.command()
  async def hello(self, ctx):
   await ctx.send(f"Hello!")


def setup(bot):
  bot.add_cog(Random(bot))