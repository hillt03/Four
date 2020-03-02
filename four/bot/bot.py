import os
import discord
from discord.ext import commands
from four.bot.helpers import get_value_from_secrets


def main():
    discord_token = get_value_from_secrets("DISCORD_TOKEN")
    bot = commands.Bot(command_prefix='4')

    @bot.event
    async def on_ready():
        print("Bot is online")

    @bot.command(hidden=True)
    async def load(ctx, extension):
        if ctx.message.author.id == get_value_from_secrets("MY_ID"):
            bot.load_extension(f"four.bot.cogs.{extension}")

    @bot.command(hidden=True)
    async def unload(ctx, extension):
        if ctx.message.author.id == get_value_from_secrets("MY_ID"):
            bot.unload_extension(f"four.bot.cogs.{extension}")

    @bot.command(hidden=True)
    async def rc(ctx, extension):
        if ctx.message.author.id == get_value_from_secrets("MY_ID"):
            await unload(ctx, extension)
            await load(ctx, extension)
            print(f"{extension} reloaded.")

    for filename in os.listdir("four/bot/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"four.bot.cogs.{filename[:-3]}")
    

    bot.run(discord_token)

if __name__ == "__main__":
    main()