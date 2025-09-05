# cogs/persona.py
from discord.ext import commands
from core.bot import bot
from core.logger import logger
from personality import base_persona, seductive, playful, romantic, custom

PERSONA_MAP = {
    "base": base_persona,
    "seductive": seductive,
    "playful": playful,
    "romantic": romantic,
    "custom": custom
}

current_persona = base_persona

class PersonaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="persona", description="Switch Whisper's persona")
    async def persona(self, ctx, persona_name: str):
        global current_persona
        persona_name = persona_name.lower()
        if persona_name not in PERSONA_MAP:
            await ctx.send(f"Unknown persona '{persona_name}'. Available: {', '.join(PERSONA_MAP.keys())}")
            return

        current_persona = PERSONA_MAP[persona_name]
        logger.info(f"Switched persona to {persona_name}")
        await ctx.send(f"Whisper persona switched to {persona_name}!")

def setup(bot):
    bot.add_cog(PersonaCog(bot))
