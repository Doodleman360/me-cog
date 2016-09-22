import discord
from discord.ext import commands
from .utils import checks

class DM:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dm(self, ctx, user : discord.Member, format_msg):
        """DM a user."""
        channel = ctx.message.channel
        await self.bot.send_message(user, format_msg)
        await self.bot.purge_from(channel, limit=1)

def setup(bot):
    bot.add_cog(DM(bot))

