import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
from cogs.utils.settings import Settings
import os
import asyncio

default_settings = {"AUTODEL": True}

class DM:
    """DM a user."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/DM/settings.json", "load")
    
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dmToggle(self, ctx):
        """Turns on/off auto delete"""
        server = ctx.message.server
        self.settings["AUTODEL"] = not self.settings["AUTODEL"]
        if self.settings[server.id]["AUTODEL"]:
            await self.bot.say("I will now auto delete.")
        else:
            await self.bot.say("I will no longer auto delete.")
        fileIO("data/DM/settings.json", "save", self.settings)

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def dm(self, ctx, user : discord.Member, format_msg):
        """DM a user."""
        channel = ctx.message.channel
        await self.bot.send_message(user, format_msg)
        await self.bot.purge_from(channel, limit=1)

def check_folders():
    paths = ("data/DM", "data/DM/files")
    for path in paths:
        if not os.path.exists(path):
            print("Creating {} folder...".format(path))
            os.makedirs(path)

def check_files():
    f = "data/DM/settings.json"
    if not dataIO.is_valid_json(f):
        print("Creating empty settings.json...")
        dataIO.save_json(f, [])

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(DM(bot))

