# cogs/conversation.py
from discord.ext import commands
from core.bot import bot
from core.logger import logger
from conversation.response_engine import generate_response
from conversation.context_manager import get_context, update_context
from conversation.emotional_engine import apply_emotion
from cogs.persona import current_persona
from cogs.emotions import current_emotion

class ConversationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="chat", description="Talk to Whisper")
    async def chat(self, ctx, *, message: str):
        user_id = str(ctx.author.id)
        context = get_context(user_id)
        response = generate_response(message, context, current_persona)
        response = apply_emotion(response, current_emotion)
        await ctx.send(response)
        update_context(user_id, message, response)

def setup(bot):
    bot.add_cog(ConversationCog(bot))
