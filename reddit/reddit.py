import discord
from discord.ext import commands
from .utils import checks

class reddit:
    """pulls a picture from reddit."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def reddit(self):
        """pulls a picture from reddit."""
        await self.bot.say("test")

def setup(bot):
    bot.add_cog(reddit(bot))

