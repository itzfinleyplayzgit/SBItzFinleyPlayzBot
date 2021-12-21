import discord
import os
import platform
from time import time
from discord.ext import commands
from discord.ui import Button, View
from typing import Union, Optional
from datetime import datetime
from dotenv import load_dotenv


class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    load_dotenv()

    @commands.command(name="ping", brief="Ping the bot", description="Get the bot's latency values (websocket and REST)")
    async def ping(self, ctx):
        api_start = time()
        msg = await ctx.send("Ping...")
        api_end = time()
        
        em = discord.Embed(title="Pong!", color=ctx.author.color, timestamp=datetime.utcnow())
        em.set_author(url="https://cdn.discordapp.com/attachments/922830600849752104/922830618964942868/lightbulb-variant-outline.png", name="")
        em.add_field(name="WS Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        em.add_field(name="REST Latency", value=f"{round((api_end - api_start) * 1000)}ms", inline=True)
        await msg.edit(content=None, embed=em)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def reload(self, ctx):
            await ctx.send("Reloading cogs")
            for ext in os.listdir("./cogs/"):
                if ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                    except:
                        await ctx.send("Could not reload all extensions.")
    


def setup(bot):
    bot.add_cog(Utils(bot))