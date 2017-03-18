import discord
import praw
import prawcore
from discord.ext import commands
from .utils import checks

class reddit:
    """pulls a picture from reddit."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def reddit(self, sub):
        """pulls a picture from reddit."""
        try:
            reddit.subreddit(sub).id
            await self.bot.say("sub does exist")
        except prawcore.exceptions.Redirect:
            await self.bot.say("sub does not exist")

def setup(bot):
    bot.add_cog(reddit(bot))

