import os
import asyncio
import discord
from discord.ext import commands
from four.bot.helpers import get_value_from_secrets


def main():
    discord_token = get_value_from_secrets("DISCORD_TOKEN")
    bot = commands.Bot(command_prefix='4')
    my_id = get_value_from_secrets("MY_ID")

    def author_is_me(ctx):
        return ctx.message.author.id == my_id

    @bot.event
    async def on_ready():
        print("Bot is online")

    @bot.command(hidden=True)
    @commands.check(author_is_me)
    async def load(ctx, extension):
        bot.load_extension(f"four.bot.cogs.{extension}")

    @bot.command(hidden=True)
    @commands.check(author_is_me)
    async def unload(ctx, extension):
        bot.unload_extension(f"four.bot.cogs.{extension}")

    @bot.command(hidden=True)
    @commands.check(author_is_me)
    async def rc(ctx, extension):
        await unload(ctx, extension)
        await load(ctx, extension)
        print(f"{extension} reloaded.")

    for filename in os.listdir("four/bot/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"four.bot.cogs.{filename[:-3]}")
    

    bot.run(discord_token)

if __name__ == "__main__":
    main()