import discord
from discord.ext import commands
from .utils import checks

class CleanAll:
    """Cleans all messages in a chanell."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def CleanAll(self, ctx):
        """Cleans all messages from a channel."""
        channel = ctx.message.channel
        tmp = ctx.message
        async for message in self.bot.logs_from(channel, limit=10000000,before=tmp):
            try:
                await self.bot.delete_message(message)
            except:
                pass
            tmp = message

    async def slow_deletion(self, messages):
        for message in messages:
            try:
                await self.bot.delete_message(message)
            except:
                pass

def setup(bot):
    bot.add_cog(CleanAll(bot))

