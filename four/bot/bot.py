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

    @bot.command()
    async def load(ctx, extension):
        bot.load_extension(f"four.bot.cogs.{extension}")

    @bot.command()
    async def unload(ctx, extension):
        bot.unload_extension(f"four.bot.cogs.{extension}")

    for filename in os.listdir("four/bot/cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"four.bot.cogs.{filename[:-3]}")
    

    bot.run(discord_token)

if __name__ == "__main__":
    main()