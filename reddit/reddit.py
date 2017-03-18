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
    async def reddit(self, ctx, format_msg):
        """pulls a picture from reddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        
        #r.subreddit(sub).id
        for submission in r.subreddit(format_msg).hot(limit=2):
            await self.bot.say(vars(submission))
def setup(bot):
    bot.add_cog(reddit(bot))

