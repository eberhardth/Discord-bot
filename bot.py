import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
bot_key = os.getenv("BOT_KEY") 

intents = discord.Intents.default()  
intents.message_content = True 
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension('cogs.smashdown_commands')
    await bot.load_extension('cogs.godnatt_commands')   
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(aliases=['hjälp', 'plz'])
async def Help(ctx):
    embed = discord.Embed(title='Commands', description='List of available commands:')
    embed.add_field(name='smashhelp', value='Shows the commands for a random smashdown.')
    embed.add_field(name='godnatt', value='Set a time for Mio to remind you to sleep.\nUsage: !godnatt hh mm')
    await ctx.send(embed=embed)

bot.run(bot_key)