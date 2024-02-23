import discord
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta
from dateutil import parser
import random

class GodnattCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
    
    async def play_sound(self, channel):
        if channel:
            voice_client = await channel.connect()
            if random.random() < 0.05:
                source = discord.FFmpegPCMAudio('media/augh.mp3')
            else:
                source = discord.FFmpegPCMAudio('media/mio.mp3')
            voice_client.play(source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()

    @commands.command(aliases=['goodnight', 'gn'])
    async def godnatt(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('Please specify the time, usage: !godnatt hh mm')
        elif not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send("You need to be in a voice channel to use this command.")
        else:
            time = ''.join([f'{x}:' for x in args])[:-1]
            try: 
                parsed_time = parser.parse(time)
                formatted_time = parsed_time.strftime('%H:%M')
                await ctx.send(f'Alright, saying goodnight at {formatted_time}')
                channel = ctx.author.voice.channel
                current_time = datetime.now()
                if parsed_time < current_time: 
                    parsed_time += timedelta(days=1)
                time_diff = (parsed_time - current_time).total_seconds()
                await asyncio.sleep(time_diff)
                await self.play_sound(channel)
            except ValueError:
                await ctx.send('Huh? What time did you mean?')
            



async def setup(bot):
    await bot.add_cog(GodnattCog(bot))