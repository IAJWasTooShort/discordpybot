import discord
from discord.ext import commands


class help(commands.Cog, name='Help'):

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name="test12")
	async def help(ctx):
    embed=discord.Embed(title="MinecraftSMP Bot", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Staff ", value="Shows Staff members", inline=False)
    embed.add_field(name="Add", value="Adds two numbers together.", inline=False)
    embed.add_field(name="Changelog", value="Bot Changelog", inline=False)
    embed.add_field(name="Choose ", value="Chooses between multiple choices", inline=False)
    embed.add_field(name="Credits ", value="Bot Credits", inline=False)
    embed.add_field(name="Crispy", value="The COOLEST guy! :sunglasses:",inline=False)
    embed.add_field(name="Ping", value="Ping", inline=False)
    embed.add_field(name="Hello", value=" Says Hi. Usage hello me / hello name.", inline=False)
    embed.add_field(name="Help", value="Shows this message", inline=False)
    embed.add_field(name="Joined", value="Says when a member joined", inline=False)
    embed.add_field(name="Membercount", value="Shows Membercount", inline=False)
    embed.add_field(name="Plans", value="Plans", inline=False)
    embed.add_field(name="Repeat", value="Repeats a message multiple times | Turned off because spam", inline=False)
    embed.add_field(name="Roll", value="Rolls a dice in NdN format", inline=False)
    embed.add_field(name="Status", value="Checks Our Website's Status", inline=False)
    embed.add_field(name="Quote", value="Chooses a random quote from the quote book", inline=False)
    embed.add_field(name="Name", value="Chooses a random one of our names", inline=False)
    embed.add_field(name="Name", value="Chooses a name", inline=False)
    embed.add_field(name="Play", value="Chooses an action", inline=False)
    embed.add_field(name="Lvl", value="Shows your level", inline=False)
    embed.add_field(name="MagicBall", value="oooo magic", inline=False)
    embed.add_field(name="ID", value="Get your ID", inline=False)
    embed.add_field(name="Kill", value="Kill someone", inline=False)
    embed.add_field(name="Curry", value="Sends the curry song", inline=False)
    embed.add_field(name="Rick", value="roll", inline=False)
    embed.add_field(name="justeat", value="Did somebody say?", inline=False)
    embed.add_field(name="Speedrun", value="Sped", inline=False)
    embed.add_field(name="Lettuce", value="Sends the Lettuce song", inline=False)
    embed.add_field(name="Tommy", value="Jump in da", inline=False)
    embed.add_field(name="MLG", value="MLG MY GUY", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")

    miles=discord.Embed(title="MinecraftSMP Miles Commands", color=0x800080)
    miles.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    miles.add_field(name="Miles", value="Picture", inline=False)
    miles.add_field(name="Manners", value="Miles Has Good Manners", inline=False)
    miles.add_field(name="LongManners", value="Miles Has Good Manners LONG", inline=False)
    miles.add_field(name="Wrd", value="WORD", inline=False)
    miles.add_field(name="Wow", value="Wow Miles", inline=False)
    miles.add_field(name="Cashew", value="I'm a cashew", inline=False)

    embed1=discord.Embed(title="MinecraftSMP Music Commands", color=0x800080)
    embed1.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed1.add_field(name="Join/Summon", value="Gets The Bot to Join VC", inline=False)
    embed1.add_field(name="Leave/Disconnect", value="Gets the bot to leave VC", inline=False)
    embed1.add_field(name="Volume", value="Changes volume", inline=False)
    embed1.add_field(name="Now/Current/Playing", value="Shows what is playing rn", inline=False)
    embed1.add_field(name="Pause", value="Pauses", inline=False)
    embed1.add_field(name="Resume", value="Resumes", inline=False)
    embed1.add_field(name="Stop", value="Stops the music", inline=False)
    embed1.add_field(name="Skip", value="Skips", inline=False)
    embed1.add_field(name="Queue", value="Looks at the queue", inline=False)
    embed1.add_field(name="MagicBall", value="oooo magic", inline=False)
    embed1.add_field(name="Shuffle", value="Shuffles Queue", inline=False)
    embed1.add_field(name="Remove", value="Remove a song from queue", inline=False)
    embed1.add_field(name="Loop", value="Loops song", inline=False)
    embed1.add_field(name="Play", value="Plays song", inline=False)

    embed1.set_footer(text="Bot designed and coded by IAJ")

    await ctx.send(embed=embed)
    await ctx.send(embed=embed1)
    await ctx.send(embed=miles)

def setup(bot):
	bot.add_cog(help(bot))