import discord
from discord.ext import commands

class Xeellit(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='x.')

        self.remove_command('help')

    async def setup_hook(self):
        await self.load_extension('jishaku')

        for guild_id in []:
            self.tree.copy_global_to(guild=discord.Object(id=guild_id))
            await self.tree.sync(guild=discord.Object(id=guild_id))

    async def on_ready(self):
        pass

if __name__ == '__main__':
    bot = Xeellit()
    bot.run('token')