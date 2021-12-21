import discord
import os
import platform
from discord.ext import commands

class Random(commands.Cog):

  def __init__(self, bot):
        self.bot = bot

  @commands.command()
  async def rtesting(self, ctx):
   await ctx.send(f"Testing Completed!!")



def setup(bot):
  bot.add_cog(Random(bot))