import discord
from discord.ext import commands

class Nyaellit(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='x.', intents=discord.Intents().all())

        self.remove_command('help')

    async def setup_hook(self):
        await self.load_extension('jishaku')

        for guild_id in []:
            self.tree.copy_global_to(guild=discord.Object(id=guild_id))
            await self.tree.sync(guild=discord.Object(id=guild_id))

    async def on_ready(self):
        pass

if __name__ == '__main__':
    bot = Nyaellit()
    bot.run('token')