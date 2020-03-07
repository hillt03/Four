import asyncio
import discord
from discord.ext import commands
import random

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help="Gives a pong")
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! :ping_pong: {int(self.bot.latency*1000)}ms :ping_pong:")
    
    @commands.command(help="Counts down from 4", aliases=["c"])
    async def count(self, ctx):
        message = await ctx.send(":stop_sign: :stop_sign: :stop_sign: :stop_sign: :four: :stop_sign: :stop_sign: :stop_sign: :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":stop_sign: :stop_sign: :stop_sign: :stop_sign: :three: :stop_sign: :stop_sign: :stop_sign: :stop_sign:")
        await asyncio.sleep(1)
        await message.edit(content=":yellow_circle: :yellow_circle: :yellow_circle: :yellow_circle: :two: :yellow_circle: :yellow_circle: :yellow_circle: :yellow_circle:")
        await asyncio.sleep(1)
        await message.edit(content=":yellow_circle: :yellow_circle: :yellow_circle: :yellow_circle: :one: :yellow_circle: :yellow_circle: :yellow_circle: :yellow_circle:")
        await asyncio.sleep(1)
        await message.edit(content=":green_circle: :green_circle: :green_circle: :green_circle:\n:green_circle: :regional_indicator_g: :regional_indicator_o: :green_circle:\n:green_circle: :green_circle: :green_circle: :green_circle:")
    
    @commands.command(hidden=True)
    async def getid(self, ctx):
        await ctx.send(ctx.message.author.id)
    
    @commands.command(help="Selects a random value from passed in arguments", aliases=['r'])
    async def random(self, ctx, *args):
        await ctx.send(random.choice(args))
        


def setup(bot):
    bot.add_cog(Misc(bot))