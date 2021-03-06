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
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("https://yande.re/post/random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="highres").get("href")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def konachan(self, i):
        """Random Image From Konachan"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("https://konachan.com/post/random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="highres").get("href")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def e621(self, i):
        """Random Image From e621"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("https://e621.net/post/random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="highres").get("href")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def rule34(self, i):
        """Random Image From rule34"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://rule34.xxx/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say('http:' + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def danbooru(self, i):
        """Random Image From Danbooru"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://danbooru.donmai.us/posts/random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say('http://danbooru.donmai.us' + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def gelbooru(self, i):
        """Random Image From Gelbooru"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://www.gelbooru.com/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def tbib(self, i):
        """Random Image From DrunkenPumken"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://www.tbib.org/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say("http:" + image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def xbooru(self, i):
        """Random Image From Xbooru"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://xbooru.com/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def furrybooru(self, i):
        """Random Image From Furrybooru"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://furry.booru.org/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def drunkenpumken(self, i):
        """Random Image From DrunkenPumken"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
                query = ("http://drunkenpumken.booru.org/index.php?page=post&s=random")
                page = await aiohttp.get(query)
                page = await page.text()
                soup = BeautifulSoup(page, 'html.parser')
                image = soup.find(id="image").get("src")
                await self.bot.say(image)
        except Exception as e:
            await self.bot.say(":x: **Error:** `{}`".format(e))

    @rnsfw.command(no_pm=True)
    async def lolibooru(self, i):
        """Random Image From Lolibooru"""
        num = int(i)
        if num > 11:
            num = 10
        try:
            for rand in range(0,num):
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

