import requests
import discord
from discord.ext import commands
from four.bot.helpers import get_json_from_api

class APIData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Lists astronauts currently in space")
    async def cosmos(self, ctx):
        astros = get_json_from_api("http://api.open-notify.org/astros.json")
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
    bot.add_cog(APIData(bot))