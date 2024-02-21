import discord
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta

class GodnattCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
    
    async def play_sound(self, channel):
        if channel:
            voice_client = await channel.connect()
            source = discord.FFmpegPCMAudio('media/augh.mp3')
            voice_client.play(source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()

    @commands.command()
    async def godnatt(self, ctx, hour: int = None, minute: int = None):
        if hour is None or minute is None:
            await ctx.send('Please specify the time, usage: !godnatt hh mm')
        elif not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("You need to be in a voice channel to use this command.")
        else:
            await ctx.send(f'Alright, saying goodnight at {hour}:{minute}')
            channel = ctx.author.voice.channel
            current_time = datetime.now()
            desired_time = current_time.replace(hour=hour, minute = minute, second = 0, microsecond = 0)
            if desired_time < current_time: 
                desired_time += timedelta(days=1)
            time_diff = (desired_time - current_time).total_seconds()
            await asyncio.sleep(time_diff)
            await self.play_sound(channel)


async def setup(bot):
    await bot.add_cog(GodnattCog(bot))