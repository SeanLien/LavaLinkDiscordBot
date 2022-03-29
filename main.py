import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.command()
async def play(ctx, url: str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    # Check to see if bot already in a voice channel, if in voice channel nothing happens.

    if not voice.is_connected:
        await voiceChannel.connect()

@client.command()
# Leaving the voice channels
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel right now.")

@client.command()
# Pause the music
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No audio is currently playing.")

@client.command()
# Resume the music.
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is not currently paused")




client.run("OTU4MTczMTE5Njk1MTc5ODA2.YkJeQQ.ozMLUD3a0s-gF4nofcABZGcI_EE")
