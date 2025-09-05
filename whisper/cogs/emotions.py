# cogs/emotions.py
from discord.ext import commands
from core.bot import bot
from core.logger import logger
from personality import emotions as emotion_module

current_emotion = "neutral"

class EmotionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="mood", description="Set Whisper's emotional tone")
    async def mood(self, ctx, emotion_name: str):
        global current_emotion
        if emotion_name not in emotion_module.EMOTIONS:
            await ctx.send(f"Unknown emotion '{emotion_name}'. Available: {', '.join(emotion_module.EMOTIONS.keys())}")
            return

        current_emotion = emotion_name
        logger.info(f"Set Whisper emotion to {emotion_name}")
        await ctx.send(f"Whisper's mood is now {emotion_name}.")

def setup(bot):
    bot.add_cog(EmotionCog(bot))
