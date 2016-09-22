import discord
from discord.ext import commands
from .utils import checks

class DM:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.admin_or_permissions(manage_server=True)
    async def DM(self, user : discord.Member, format_msg):
        """DM a user."""
        await self.bot.say(format_msg)
        await self.bot.send_message(user, format_msg)

def setup(bot):
    bot.add_cog(DM(bot))
