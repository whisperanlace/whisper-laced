# core/bot.py
import discord
from discord.ext import commands
from core.config import config
from core.logger import logger

intents = discord.Intents.default()
intents.message_content = True  # Needed for message reading

bot = commands.Bot(
    command_prefix=config.COMMAND_PREFIX,
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user} | ID: {bot.user.id}")
    logger.info("------")

def run():
    bot.run(config.BOT_TOKEN)
