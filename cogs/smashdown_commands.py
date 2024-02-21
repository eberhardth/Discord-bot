
from discord.ext import commands
from smashdown import Smashdown

class SmashCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.smashdown_instance = None

    @commands.command()
    async def smashdown(self, ctx, *player_names: str):
        if not player_names:
            await ctx.send("Please provide at least one player name.")
            return
        
        self.smashdown_instance = Smashdown(player_names)
        match = self.smashdown_instance.matchup()
        await ctx.send(match)

    @commands.command()
    async def new(self, ctx):
        match = self.smashdown_instance.matchup()
        await ctx.send(match)

    @commands.command()
    async def remaining(self, ctx):
        if self.smashdown_instance is None:
            ctx.send("No smashdown in progress")
            return
        remaining_fighters = self.smashdown_instance.remaining_fighters()
        await ctx.send(remaining_fighters)
        
    @commands.command()
    async def win(self,ctx, name: str = None):
        if name is None:
            await ctx.send("Who was the winner?")
            return
        
        success = self.smashdown_instance.add_point(name)
        if success:
            match = self.smashdown_instance.matchup()
            await ctx.send(match)
        else:
            await ctx.send("Player not found.")

    @commands.command()
    async def board(self, ctx):
        leaderboard = self.smashdown_instance.leaderboard()
        await ctx.send(leaderboard)

    @commands.command()
    async def winner(self, ctx):
        champion = self.smashdown_instance.get_winner()
        await ctx.send(champion)


async def setup(bot):
    await bot.add_cog(SmashCog(bot))