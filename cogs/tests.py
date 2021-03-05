import discord
from discord.ext import commands


class tests(commands.Cog, name='Developer Commands'):

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name="test12")
	async def test12(self, ctx):
		await ctx.send("Cogs running")

def setup(bot):
	bot.add_cog(tests(bot))