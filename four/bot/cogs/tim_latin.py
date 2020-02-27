import discord
from discord.ext import commands
from four.timlatin.timlatin import TimlatinTranslator

class TimLatin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = TimlatinTranslator("four/data/tl.json")
    
    @commands.command()
    async def t(self, ctx):
        user_input = ctx.message.content[3:]
        if user_input:
            await ctx.send(self.translator.translate_text(user_input))

def setup(bot):
    bot.add_cog(TimLatin(bot))