# cogs/prompts.py
from discord.ext import commands
from core.bot import bot
from core.bridge import laced_bridge
from core.logger import logger

class PromptCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="prompt", description="Generate a prompt for Laced")
    async def prompt(self, ctx, *, prompt_text: str):
        await ctx.defer()
        user_id = str(ctx.author.id)
        logger.info(f"Received prompt from {ctx.author}: {prompt_text}")

        result = await laced_bridge.send_prompt(prompt_text, user_id)
        if "error" in result:
            await ctx.followup.send(f"Error: {result['error']}")
        else:
            await ctx.followup.send(f"Prompt sent successfully! Generated {len(result.get('images', []))} images.")

def setup(bot):
    bot.add_cog(PromptCog(bot))
