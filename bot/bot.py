from pathlib import Path

import discord
from discord.ext import commands


class MusicBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True, intents=discord.Intents.all(),) # possible error

    def setup(self):
        print("Running music bot setup....")

        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f" Loaded '{cog}' cog.")
        print("Setup complete")

    def run(self):
        self.setup()

        with open("Data/token.0", "r", encoding="utf-8") as f:
            TOKEN = f.read()

        print("Running bot..")
        super().run(TOKEN, reconnect=True)

        # TODO buggy shutdown, can do await super().close() in terminal

    async def shutdown(self):
        print("Closing the Discord bot down")
        await self.logout()

    async def close(self):
        print("Closing on any key press...")
        await self.shutdown()

    async def on_connect(self):
        print(f"Connected to Discrd (latency: {self.latency * 1000} ms) ")

    async def on_resumed(self):
        print("Bot resumed.")

    async def on_disconnect(self):
        print("Bot disconnected")

    async def on_ready(self):
        self.client_id = (await self.application_info()).id
        print("Bot ready")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or("+")(bot,msg)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg,cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        await self.process_commands(msg)

