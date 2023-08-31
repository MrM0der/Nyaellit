import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ban')
    async def _ban(self, ctx):
        await ctx.send('иди нахуй')

async def setup(bot: commands.Bot):
    await bot.add_cog(Ban(bot))