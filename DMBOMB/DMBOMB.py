import discord
from discord.ext import commands
from .utils import checks

class DMBOMB:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dmBOMB(self, ctx, user : discord.Member, format_msg):
        """DM a user."""
        channel = ctx.message.channel
        await self.bot.purge_from(channel, limit=1)
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        for submission in r.subreddit(format_msg).top("all"):
            if "i.imgur.com/" in submission.url or "gfycat.com/" in submission.url:
                await self.bot.send_message(submission.url)

def setup(bot):
    bot.add_cog(DMBOMB(bot))

