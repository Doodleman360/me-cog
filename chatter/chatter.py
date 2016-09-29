from chatterbot import ChatBot
import discord
from discord.ext import commands
from .utils import checks

class chatter:
    """chatter with a user."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def chat(self, format_msg):
        """chat"""
        chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
        chatbot.train("chatterbot.corpus.english")
        await self.bot.say(chatbot.get_response(format_msg))

def setup(bot):
    bot.add_cog(chatter(bot))

