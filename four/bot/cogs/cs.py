import discord
import asyncio
from discord.ext import commands
from four.bot.helpers import get_value_from_secrets
from four.pandascore.pandascore import PandaScoreHelper


class CS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        api_token = get_value_from_secrets("PANDASCORE_TOKEN")
        self.ps = PandaScoreHelper(api_token)
    
    @commands.command(help="Lists upcoming CSGO matches")
    async def cs(self, ctx):
        matches = self.ps.get_upcoming_matches()
        if not matches:
            await ctx.send("No matches found.")
            return
        embed = discord.Embed(title="Upcoming CSGO Matches", description="Timezone: EST", color=0xfff78c)
        embed.set_image(url="https://i.imgur.com/i9OfSCF.png")
        embed.set_thumbnail(url="https://i.imgur.com/zX5VBbt.png")
        embed.set_author(name="Four", icon_url="https://cdn.discordapp.com/avatars/681986669020184627/1dac2d38461df3015ab64481beb7318d.png?size=128")
        counter = 1
        for match in matches:
            name = match["name"]
            status = match["status"]
            live_url = match["live_url"]
            league = match["league"]["name"]
            begin_at = self.ps.get_formatted_time(match["begin_at"])
            
            if live_url:
                upcoming_match = f"[{name}]({live_url})"
            else:
                upcoming_match = name
            embed.add_field(name="Match " + str(counter), value=upcoming_match, inline=True)
            embed.add_field(name="Date/Time", value=begin_at, inline=True)
            embed.add_field(name="League", value=league, inline=True)
            
            counter += 1

        await ctx.send(embed=embed)

                

def setup(bot):
    bot.add_cog(CS(bot))