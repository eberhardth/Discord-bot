import discord
from discord.ext import commands
from smashdown import Smashdown

class SmashCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.smashdown_instance = None

    @commands.command(aliases=['smash'])
    async def smashdown(self, ctx, *player_names: str):
        """Creates and starts a randomized smashdown.\nalt: smash\nUsage: !smashdown [player names]"""
        if not player_names:
            await ctx.send("Please provide at least one player name.")
            return
        
        self.smashdown_instance = Smashdown(player_names)
        match = self.smashdown_instance.matchup()
        await ctx.send(match)

    @commands.command(aliases=['ny', 'match'])
    async def new(self, ctx):
        """Generates a new match.\nalt: ny, match"""
        match = self.smashdown_instance.matchup()
        await ctx.send(match)

    @commands.command(aliases=['kvar', 'fighters'])
    async def remaining(self, ctx):
        """Shows a list of the fighters yet to be played.\nalt: kvar. fighters"""
        if self.smashdown_instance is None:
            ctx.send("No smashdown in progress")
            return
        remaining_fighters = self.smashdown_instance.remaining_fighters()
        await ctx.send(remaining_fighters)
        
    @commands.command(aliases=['vinst'])
    async def win(self,ctx, name: str = None):
        """Adds a point to the winner and generates a new match.\nalt: vinst\nUsage: !win [player name]"""
        if name is None:
            await ctx.send("Who was the winner?")
            return
        
        success = self.smashdown_instance.add_point(name)
        if success:
            match = self.smashdown_instance.matchup()
            await ctx.send(match)
        else:
            await ctx.send("Player not found.")

    @commands.command(aliases=['leaderboard'])
    async def board(self, ctx):
        """Posts the leaderboard.\nalt: leaderboard"""
        leaderboard = self.smashdown_instance.leaderboard()
        await ctx.send(leaderboard)

    @commands.command(aliases=['vinnare', 'avslut'])
    async def winner(self, ctx):
        """Determines the winner.\nalt: vinnare, avslut"""
        champion = self.smashdown_instance.get_winner()
        await ctx.send(champion)

    @commands.command()
    async def smashhelp(self, ctx):
        """Shows this message."""
        embed = discord.Embed(title='Smashdown commands', description='List of available commands:')
        for command in self.get_commands():
            embed.add_field(name=command.name, value=command.help, inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SmashCog(bot))