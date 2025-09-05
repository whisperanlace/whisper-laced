# cogs/admin.py
from discord.ext import commands
from core.bot import bot
from core.logger import logger

ADMIN_IDS = []  # Fill with Discord IDs of admins

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="reload", description="Reload Whisper bot cogs (admin only)")
    async def reload(self, ctx):
        if ctx.author.id not in ADMIN_IDS:
            await ctx.send("You are not authorized to use this command.")
            return

        for cog in list(bot.cogs):
            try:
                bot.reload_extension(f"cogs.{cog}")
            except Exception as e:
                await ctx.send(f"Failed to reload {cog}: {e}")
        await ctx.send("All cogs reloaded successfully!")
        logger.info(f"Admin {ctx.author} reloaded cogs.")

def setup(bot):
    bot.add_cog(AdminCog(bot))
