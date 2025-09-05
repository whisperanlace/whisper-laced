# cogs/fun.py
from discord.ext import commands
from core.bot import bot

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="tease", description="Whisper teases you")
    async def tease(self, ctx):
        await ctx.send("Oh, you think you can keep up with me? 😏")

def setup(bot):
    bot.add_cog(FunCog(bot))
