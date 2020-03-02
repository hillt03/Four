import discord
import asyncio
from discord.ext import commands
from four.pandascore.pandascore import PandaScoreWrapper
from four.bot.helpers import get_json

class CS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_token = get_json("four/data/secrets.json")["PANDASCORE_TOKEN"]
        self.ps = PandaScoreWrapper(self.api_token)
    
    @commands.command(help="List upcoming CSGO matches")
    async def cs(self, ctx):
        matches = self.ps.get_upcoming_matches()
        if not matches:
            await ctx.send("No matches found.")
            return

        embed = discord.Embed(title="Upcoming CSGO Matches", description="Timezone: EST", color=0x00ff00)
        for match in matches:
            
            name = match["name"]
            status = match["status"]
            live_url = match["live_url"]
            begin_at = self.ps.get_formatted_time(match["begin_at"])

            
            upcoming_matches = ""
            if live_url:
                upcoming_matches += f"Watch at: {live_url}\n"
            upcoming_matches += f"{begin_at}\n"
            embed.add_field(value=name, name=upcoming_matches, inline=True)

        await ctx.send(embed=embed)

                

def setup(bot):
    bot.add_cog(CS(bot))