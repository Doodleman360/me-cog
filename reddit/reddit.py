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
    #@checks.admin_or_permissions(manage_server=True)
    async def randR(self):
        """pulls a random nsfw picture from reddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        
        #r.subreddit(sub).id
        done = False
        while not done:
            for submission in r.subreddit("randnsfw").new(limit=1):
                if "i.imgur.com/" in submission.url:
                    await self.bot.say(submission.url)
                    done = True

    @commands.command(pass_context=True)
    #@checks.admin_or_permissions(manage_server=True)
    async def redditNew(self, ctx, format_msg):
        """pulls a new post from reddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        for submission in r.subreddit(format_msg).new(limit=1):
            await self.bot.say(submission.url)

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def redditHot(self, ctx, format_msg):
        """pulls a new post from reddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        for submission in r.subreddit(format_msg).hot(limit=1):
            await self.bot.say(submission.url)

    @commands.command(pass_context=True)
    #@checks.admin_or_permissions(manage_server=True)
    async def redditTop(self, ctx, format_msg):
        """pulls the top post from a subreddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        for submission in r.subreddit(format_msg).top("all", limit=1):
            await self.bot.say(submission.url)

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def redditBomb(self, ctx, format_msg):
        """pulls the top post from a subreddit."""
        #r = praw.Reddit(user_agent="Get top wallpaper from /r/{subreddit} by /u/ssimunic".format(subreddit=sub))
        #r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', password='pass', user_agent='testscript by /u/fakebot3', username='Doodleman360_')
        r = praw.Reddit(client_id='W0qqIJPsyqrKbA', client_secret='D8KHLMo62Nu8Q1wJMJRtq-FBD18', user_agent='testscript by /u/Doodleman360_')
        try:
            for submission in r.subreddit(format_msg).top("all",limit=100):
                if "i.imgur.com/" in submission.url or "gfycat.com/" in submission.url:
                    await self.bot.say(submission.url)
        except:
            await self.bot.say("subreddit does not exist :P")


def setup(bot):
    bot.add_cog(reddit(bot))

