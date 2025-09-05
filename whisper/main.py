# main.py
from core.bot import run
from core.bot import bot
from core.logger import logger
import os

# Load all cogs
COGS = [
    "cogs.prompts",
    "cogs.laced",
    "cogs.persona",
    "cogs.emotions",
    "cogs.conversation",
    "cogs.admin",
    "cogs.fun"
]

for cog in COGS:
    try:
        bot.load_extension(cog)
        logger.info(f"Loaded cog: {cog}")
    except Exception as e:
        logger.exception(f"Failed to load cog {cog}: {e}")

if __name__ == "__main__":
    run()
