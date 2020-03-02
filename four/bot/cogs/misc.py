import discord
from discord.ext import commands
import requests

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command(help="Lists astronauts currently in space")
    async def cosmos(self, ctx):
        astros = requests.get("http://api.open-notify.org/astros.json")
        if astros.status_code != 200:
            await ctx.send("Data unavailable.")
        astros = astros.json()

        description = "There are currently " + str(astros["number"]) + " astronauts in space."
        embed = discord.Embed(title="Astronauts In Space", description=description, color=0xfff78c)
        embed.set_image(url="https://i.imgur.com/zReLsRn.png")
        embed.set_author(name="Four", icon_url="https://i.imgur.com/6Cqkof8.png")
        embed.set_thumbnail(url="https://i.imgur.com/6Cqkof8.png")
        counter = 1
        for astro in astros["people"]:
            value = f"{astro['name']}\nCraft: {astro['craft']}"
            embed.add_field(name="Astronaut " + str(counter), value=value, inline=False)
            counter += 1
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))