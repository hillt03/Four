import os
import discord
from four.bot.helpers import get_json


class FourBot(discord.Client):

    def __init__(self):
        super().__init__()
    
    async def on_ready(self):
        print(f"{self.user} has connected.")
    




def main():
    secrets = get_json("four/data/secrets.json")
    discord_token = secrets["DISCORD_TOKEN"]
    pandascore_token = secrets["PANDASCORE_TOKEN"]
    bot = FourBot()
    bot.run(discord_token)

if __name__ == "__main__":
    main()