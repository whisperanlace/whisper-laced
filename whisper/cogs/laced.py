# cogs/laced.py
from discord.ext import commands
from core.bot import bot
from core.bridge import laced_bridge
from core.logger import logger

class LacedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="generate", description="Send prompt directly to Laced for image generation")
    async def generate(self, ctx, *, prompt_text: str):
        await ctx.defer()
        user_id = str(ctx.author.id)
        logger.info(f"Sending prompt to Laced: {prompt_text}")

        result = await laced_bridge.send_prompt(prompt_text, user_id)
        if "error" in result:
            await ctx.followup.send(f"Laced API Error: {result['error']}")
        else:
            images = result.get("images", [])
            if images:
                await ctx.followup.send(f"Generated {len(images)} images successfully!")
            else:
                await ctx.followup.send("No images generated.")

def setup(bot):
    bot.add_cog(LacedCog(bot))
