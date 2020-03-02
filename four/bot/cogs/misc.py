import asyncio
import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help="Gives a pong")
    async def ping(self, ctx):
        await ctx.send(f"Pong! :ping_pong: {int(self.bot.latency*1000)}ms")
    
    @commands.command(help="Counts down from 4")
    async def count(self, ctx):
        message = await ctx.send(":stop_sign: Four :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":stop_sign: Three :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":stop_sign: Two :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":stop_sign: One :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":green_circle: :metal: :green_circle:  GO!!!! :green_circle:  :metal: :green_circle: ")
        


def setup(bot):
    bot.add_cog(Misc(bot))