import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp
from bs4 import BeautifulSoup
import random

class rnsfw:
    """repetes nsfw."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(pass_context=True)
    async def rnsfw(self, ctx):
        """rnsfw Commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @rnsfw.command(no_pm=True)
    async def yandere(self, i):
        """Random Image From Yandere"""
        if i > int(11):
            i = 10
        try:
            for num in range(0,int(i)):
                query = ("https://yande.re/post/random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="highres").get("href")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def konachan(self):
        """Random Image From Konachan"""
        try:
            query = ("https://konachan.com/post/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="highres").get("href")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def e621(self):
        """Random Image From e621"""
        try:
            query = ("https://e621.net/post/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="highres").get("href")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def rule34(self):
        """Random Image From rule34"""
        try:
            query = ("http://rule34.xxx/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say('http:' + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def danbooru(self):
        """Random Image From Danbooru"""
        try:
            query = ("http://danbooru.donmai.us/posts/random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say('http://danbooru.donmai.us' + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def gelbooru(self):
        """Random Image From Gelbooru"""
        try:
            query = ("http://www.gelbooru.com/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def tbib(self):
        """Random Image From DrunkenPumken"""
        try:
            query = ("http://www.tbib.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say("http:" + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def xbooru(self):
        """Random Image From Xbooru"""
        try:
            query = ("http://xbooru.com/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def furrybooru(self):
        """Random Image From Furrybooru"""
        try:
            query = ("http://furry.booru.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def drunkenpumken(self):
        """Random Image From DrunkenPumken"""
        try:
            query = ("http://drunkenpumken.booru.org/index.php?page=post&s=random")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def lolibooru(self):
        """Random Image From Lolibooru"""
        try:
            query = ("https://lolibooru.moe/post/random/")
            page = await aiohttp.get(query)
            page = await page.text()
            soup = BeautifulSoup(page, 'html.parser')
            image = soup.find(id="image").get("src")
            image = image.replace(' ','%20')
            await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

def setup(bot):
    bot.add_cog(rnsfw(bot))

