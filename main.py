import discord
from discord.ext import commands
from discord import Member
import random
import keep_alive
import requests
from collections import namedtuple
import asyncio
import functools
import itertools
import math
import os
import json
import youtube_dl
from async_timeout import timeout
import lyricsgenius as genius

youtube_dl.utils.bug_reports_message = lambda: ''

cogs_folder = "./cogs"

guild_ids = [766180992150274048]
WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
names = ['alphoneclient']

api = genius.Genius('TDbZbNJiKKhyJvLMK1FoZbMaEs6Nq1PCCyXo2tiBzjGTZ7oSSKPPvqo0wy-s5kuL')

description = '''IAJ's MCIsAGame Bot - Still in testing\nNote All commands are NOT case sensative.'''
bot = commands.Bot(command_prefix='.', description=description, case_insensitive = True,) #intents=intents)

image_types=('.jpg','.png','.gif','.jpeg') #add image types if needed


folders={'Image Folder':'memes','Sent Folder':'sent_images'}
for folder in folders.values():
	if not os.path.isdir(folder):
		os.mkdir(folder)

for file in cogs_folder:
  if file.endswith(".py"):
    try:
      bot.load_extension(f"cogs.{file[:-3]}")
      print(f"Loaded: {file}")
    except:
      print(f"Could not load: {file}")

bot.remove_command('help')

@bot.event
async def on_ready():
    game = discord.Game("Minecraft is a Game!")
    await bot.change_presence(status=discord.Status.online, activity=game)

extensions = [
	'cogs.tests' 
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension) 

@bot.command()
async def pfp(ctx, member: Member = None):
 if not member:
  member = ctx.author
 await ctx.send(member.avatar_url)

@bot.command(name="id")
async def _id(ctx):
    author = ctx.message.author
    await ctx.send('Your ID is: ' + str(author.id))

@bot.command()
async def kill(ctx, user : discord.Member):
  author = ctx.message.author
  if user.id == 728559741462249523:
    await ctx.send("Not gonna kill IAJ he is so cool")
  elif user == author:
    await ctx.send("DONT DO IT YOU HAVE SO MUCH TO LIVE FOR")
  else:
    await ctx.send("Killed " + user.mention)

@bot.command()
async def quote(ctx):
    line = random.choice(open('texts/quote.txt').readlines())
    await ctx.send(line)

@bot.command()
async def fortune(ctx):
    line = random.choice(open('texts/name.txt').readlines())
    will = random.choice(open('texts/will.txt').readlines())
    name = random.choice(open('texts/name.txt').readlines())
    line2=line.rstrip()
    will2=will.rstrip()
    name2=name.rstrip()
    await ctx.send(line2 + " " + will2 + " " + name2)

@bot.command()
async def name(ctx):
    pep = random.choice(open('texts/name.txt').readlines())
    await ctx.send(pep)

@bot.command()
async def will(ctx):
    ac = random.choice(open('texts/will.txt').readlines())
    await ctx.send(ac)

@bot.command()
async def farmers(ctx):
    await ctx.send("https://farmersonly.com")

@bot.command()
async def magicball(ctx):
    ball = random.choice(open('texts/ball.txt').readlines())
    await ctx.send(ball)

@bot.command(pass_context=True)
async def curry(ctx):
    await ctx.send(file=discord.File(r'mp3/TheCurrySong.mp3'))

@bot.command(pass_context=True)
async def speedrun(ctx):
    await ctx.send(file=discord.File(r'mp3/DreamSpeedrun.mp3'))

@bot.command(pass_context=True)
async def boys(ctx):
    await ctx.send(file=discord.File(r'mp3/Miles.mp3'))

@bot.command(pass_context=True)
async def rick(ctx):
    await ctx.send(file=discord.File(r'mp3/Rick.mp3'))

@bot.command(pass_context=True)
async def justeat(ctx):
    await ctx.send("Did somebody say:")
    await ctx.send(file=discord.File(r'mp3/JustEat.mp3'))

@bot.command(pass_context=True)
async def hi(ctx):
    author = ctx.message.author
    if author.id == 728559741462249523:
        await ctx.send("Hello IAJ my amazing creator")
    elif author.id == 643194187423940641:
        await ctx.send("hey cameron :sparkles:")
    elif author.id == 579651160281972738:
        await ctx.send("Whatupp small man")
    elif author.id == 665877018096959518:
        await ctx.send("hey toogood :flushed:")
    elif author.id == 620310336603422721:
        await ctx.send("Bitch imma run you over with a truck")
    elif author.id == 265490663213236224:
        await ctx.send("Can I box you like a fish")
    elif author.id == 755838754073084036:
        await ctx.send("hey raj!")
        await ctx.send(file=discord.File(r'mp3/TheCurrySong.mp3'))
    elif author.id == 525780985099583503:
        await ctx.send("I dont want to speak to you")

@bot.command(pass_context=True)
async def sparkles(ctx):
    await ctx.send(":rolling_eyes: :nail_care: :sparkles:")

@bot.command(pass_context=True)
async def lettuce(ctx):
    await ctx.send(file=discord.File(r'mp3/lettuce.mp3'))

@bot.command(pass_context=True)
async def longmanners(ctx):
    await ctx.send(file=discord.File(r'mp3/Manners.mp3'))

@bot.command(pass_context=True)
async def manners(ctx):
    await ctx.send(file=discord.File(r'mp3/ShortManners.mp3'))

@bot.command(pass_context=True)
async def mlg(ctx):
    await ctx.send(file=discord.File(r'mp4/TommyInnit-MLG.mp4'))

@bot.command()
async def stan(ctx, s):
  if s == "trump":
    await ctx.send("Not gonna stan trump")
  elif s == "miles":
    await ctx.send("OMFG WE STAN MILES")
  elif s == "toogood":
    await ctx.send(":flushed:")
  elif s == "iaj":
    await ctx.send("everyone should stan iaj cause he is so pog")
  elif s == "karl":
    await ctx.send(file=discord.File(r'img/karl.png'))
  else:
    await ctx.send("Stanning {}".format(s))

@bot.command(pass_context=True)
async def mcdonalds(ctx):
    await ctx.send(file=discord.File(r'mp4/YA_Mcd.mp4'))

@bot.command(pass_context=True)
async def Tommy(ctx):
    await ctx.send(file=discord.File(r'mp4/TommyInnit-TheEmbarrassment.mp4'))

@bot.command(pass_context=True)
async def wrd(ctx):
    await ctx.send(file=discord.File(r'mp4/WrdMiles.mp4'))

@bot.command(pass_context=True)
async def cashew(ctx):
    await ctx.send(file=discord.File(r'mp4/cashew.mp4'))

@bot.command(pass_context=True)
async def uwu(ctx):
    await ctx.send(file=discord.File(r'mp3/uwu.mp3'))

@bot.command(pass_context=True)
async def wow(ctx):
    await ctx.send(file=discord.File(r'mp4/WowMiles.mp4'))

@bot.command(pass_context=True)
async def miles(ctx):
    await ctx.send(file=discord.File(r'img/Miles.png'))

@bot.command(pass_context=True)
async def noah(ctx):
    await ctx.send(file=discord.File(r'img/noah.jpg'))

@bot.command(pass_context=True)
async def ariana(ctx):
    await ctx.send(file=discord.File(r'img/ariana.png'))

@bot.command(pass_context=True)
async def pogchamp(ctx):
    await ctx.send(file=discord.File(r'img/PogChamp.png'))

@bot.command(pass_context=True)
async def dodie(ctx):
    await ctx.send(file=discord.File(r'img/dodie.png'))

@bot.command()
async def meme(ctx):
  rmeme=random.choice(open('meme.txt', encoding='utf-8').readlines())
  rmeme2=rmeme.rstrip()
  if rmeme2 == "memes/meme24.png":
    await ctx.send(file=discord.File(rmeme2))
    await ctx.send("Meme by V2splashy#4841")
  elif rmeme2 == "memes/meme22.png":
    await ctx.send("Meme by V2splashy#4841")
    await ctx.send(file=discord.File(rmeme2))
  elif rmeme2 == "memes/meme8.png":
    await ctx.send("Meme by V2splashy#4841")
    await ctx.send(file=discord.File(rmeme2))
  else:
    await ctx.send(file=discord.File(rmeme2))

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {bot.latency}')
    
@bot.command()
async def crispy(ctx):
    await ctx.send("Crispy is a cool guy! :sunglasses:")

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Minecraft SMP Info", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="IP and Port:", value="IP: max-is-a.minecraftnoob.com \n PORT: 19132", inline=False)
    embed.add_field(name="Who made this epic bot?", value="Isaac did.", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")
    await ctx.send(embed=embed)

@bot.command()
async def test11(ctx):
    path = random.choice(os.listdir('memes'))
    print(os.listdir('memes'))
    await ctx.send(file=discord.File(path))

@bot.command()
async def iaj(ctx):
    embed=discord.Embed(color=0xff00a2)
    embed.add_field(name ="IAJ", value="IAJ is so cool wdym")
    await ctx.send(embed=embed)

@bot.command()
async def status(ctx):
  def get_status(site):
    try:
        response = requests.head(site, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status

  for name in names:
      site = 'https://{}.ml'.format(name)
      website_status = get_status(site)
      await ctx.send("{0:30} {1:10} {2:10}"
            .format("<" + site + ">", website_status.status_code,website_status.reason))

@bot.command()
async def help(ctx):
    """Help."""
    embed=discord.Embed(title="MinecraftSMP Bot", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Add", value="Adds two numbers together.", inline=False)
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
    embed.add_field(name="Meme", value="Shows a random meme", inline=False)
    embed.add_field(name="Pfp", value="Shows someones pfp", inline=False)
    embed.add_field(name="Fortune", value="Tells your fortune", inline=False)
    embed.add_field(name="Hi", value="Say hello", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")

    miles=discord.Embed(title="MinecraftSMP People Commands", color=0x800080)
    miles.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    miles.add_field(name="Karl", value="KARL", inline=False)
    miles.add_field(name="Miles", value="MILES", inline=False)
    miles.add_field(name="Manners", value="Miles Has Good Manners", inline=False)
    miles.add_field(name="LongManners", value="Miles Has Good Manners LONG", inline=False)
    miles.add_field(name="Wrd", value="WORD", inline=False)
    miles.add_field(name="Wow", value="Wow Miles", inline=False)
    miles.add_field(name="Cashew", value="I'm a cashew", inline=False)
    miles.add_field(name="Noah", value="NOAH", inline=False)
    miles.add_field(name="Stan", value="Tells the bot who to stan", inline=False)
    miles.add_field(name="Ariana", value="Ariana.", inline=False)
    miles.add_field(name="Dodie", value="doddleoddle", inline=False)

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
    embed1.add_field(name="Lyrics", value="Shows song lyrics", inline=False)

    embed1.set_footer(text="Bot designed and coded by IAJ")

    await ctx.send(embed=embed)
    await ctx.send(embed=embed1)
    await ctx.send(embed=miles)

@bot.command()
async def pages(ctx):
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
    embed.add_field(name="Curry", value="Sends the curry song", inline=False)
    embed.add_field(name="Quote", value="Chooses a random quote from the quote book", inline=False)
    embed.add_field(name="Name", value="Chooses a random one of our names", inline=False)
    embed.add_field(name="Play", value="Plays a song/video", inline=False)
    embed.add_field(name="Name", value="Chooses a name", inline=False)
    embed.add_field(name="Play", value="Chooses an action", inline=False)
    embed.add_field(name="Miles", value="MILES", inline=False)
    embed.add_field(name="Lvl", value="Shows your level", inline=False)
    embed.add_field(name="MagicBall", value="oooo magic", inline=False)
    embed.add_field(name="Join/Summon", value="Gets The Bot to Join VC", inline=False)

    embed.set_footer(text="Bot designed and coded by IAJ")

    page1 = ""
    contents = [page1, "This is page 2!", "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

#@bot.command()
#async def repeat(ctx, times: int, content='repeating...'):
#    """Repeats a message multiple times."""
#    for i in range(times):
#       await ctx.send(content)


@bot.command(name='credits', aliases=['c'], help='Bot Credits')
async def credits(ctx):
    embed=discord.Embed(title="Credits", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Design/Code", value="IAJ", inline=False)
    embed.add_field(name="Moral Support", value="Fax and Crispy", inline=False)

    await ctx.send(embed=embed)


@bot.command(name='changelog', aliases=['h'], help='Bot Changelog')
async def changelog(ctx):    
    embed=discord.Embed(title="Minecraft SMP Bot", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Added: ", value="Lots of commands", inline=False)
    embed.add_field(name="Fixed", value="Major Bugs", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")

    await ctx.send(embed=embed)

@bot.command()
async def botcount(ctx):
    bot_count = len(ctx.guild.members)
    await ctx.send(bot_count)

@bot.command()
async def OnlineMembers(ctx):
    OnlineMembers = len([m for m in ctx.guild.members if not m.bot])
    await ctx.send(OnlineMembers)

@bot.command()
async def membercount(ctx):
    a=ctx.guild.member_count
    b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0x800080)))
    await ctx.send(embed=b)


@bot.command()
async def owner(ctx):
    guild = bot.get_guild(750139640836784172)
    await ctx.sent(guild.owner)

@bot.command()
async def plans(ctx):
    await ctx.send('-\n')

@bot.command()
async def staff(ctx):
    embed=discord.Embed(title="MinecraftSMP Bot", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Cool Guy", value="IAJ", inline=False)
    embed.add_field(name="Max", value="Max", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def admin(ctx):
    await ctx.send('You have perms')

@bot.command()
async def gay(ctx):
  await ctx.send("No")

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.kick()
    await ctx.send(f"**{user}** has been kicked for **no reason**.")
  else:
    await user.kick(reason=reason)
    await ctx.send(f"**{user}** has been kicked for **{reason}**.")

@bot.command()
async def links(ctx):
    """Help."""
    embed=discord.Embed(title="Links", color=0x800080)
    embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/789961691894644756/b135a9befb6ea1dfb746673731764a94.png?size=64")
    embed.add_field(name="Alphone Website:", value="https://alphoneclient.ml", inline=False)
    embed.add_field(name="My temp Website:", value="https://iaj7648.ml", inline=False)
    embed.add_field(name="Discord Link:", value="https://discord.gg/6wJ99d8", inline=False)
    embed.add_field(name="POG Website:", value="https://wiki.vg", inline=False)
    embed.add_field(name="IAJ's Music Archive thing idk:", value="https://archive.org/details/iajmusicarchive_", inline=False)
    embed.set_footer(text="Bot designed and coded by IAJ")

    await ctx.send(embed=embed)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send('Restarting...')
    await bot.close()


@bot.group()
async def hello(ctx):
    """Says Hi. Usage $hello me / $hello name."""
    if ctx.invoked_subcommand is None:
        await ctx.send('Hello to {0.subcommand_passed}!'.format(ctx))


@hello.command(name='me')
async def _me(ctx):
    await ctx.send('Hello you!')


@bot.event
async def on_message(message):
    if not message.author.bot:
        #print('function load')
        with open('level.json','r') as f:
            users = json.load(f)
            #print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != '757383943116030074':
    if lvl_start < lvl_end:
      await channel.send('{} has leveled up to Level {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@bot.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = discord.Color.green())
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = discord.Color.green())
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)

youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = bot.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.bot.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.bot.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.

        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    @commands.has_permissions(manage_guild=True)
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    @commands.has_permissions(manage_guild=True)
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    @commands.has_permissions(manage_guild=True)
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='stop')
    @commands.has_permissions(manage_guild=True)
    async def _stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if not ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        iaj = ctx.message.author.id
        if iaj == 728559741462249523:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.

        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.

        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.

        If there are songs in the queue, this will be queued until the
        other songs finished playing.

        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Queued {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

#@bot.command()
#async def lyrics(ctx, artist,*, title):
#    async with aiohttp.ClientSession() as session:
#        async with session.get(f"https://api.lyrics.ovh/v1/{artist}/{title}") as response:
#            data = await response.json()
#            lyrics = data['lyrics']
#            if lyrics is None:
#                await ctx.send("Song not found! Please enter correct Artist and Song title")
#            if len(lyrics) > 2048:
#                  lyrics = lyrics[:2048]
#            emb = discord.Embed(title = f"{title}" , description = f"{lyrics}" , color = 0xa3a3ff)
#            await ctx.send(embed=emb)
#    await session.close()

@bot.command()
async def lyrics(ctx, artist,*, title):
    userID = ctx.author.id
    await ctx.send("Searching for the lyrics to  *{}*  by  *{}* ...".format(title, artist))
    song = api.search_song(title, artist)
    if song:
      url = song.url
      lyrics = song.lyrics.split("\n")
      for line in lyrics:
        if line == '':
          lyrics.remove(line)
        else:
          await ctx.send("*{}*".format(line))
    else:
      await ctx.send("Couldnt find ur song L " +
      "Check for typos and try again.")

@bot.command()
async def savelyrics(ctx, artist,*, title): 
  userID = ctx.author.id
  await ctx.send("Searching for the lyrics to  *{}*  by  *{}* ...".format(title, artist))
  song_to_save = api.search_song(title, artist)
  if song_to_save:
    await ctx.send("Downloading the lyrics for  *{}*  by  *{}*  to the bot's host computer...".format(title, artist))
    song_to_save.save_lyrics(format_='txt')

    await ctx.send("Here is a snippet of the lyrics you've requested: ")
    song_to_save_list = api.search_song(title, artist).lyrics.split("\n")
    snippet = song_to_save_list[1:8]

    for line in snippet:
      if line == '':
        snippet.remove(line)
      else:
        await ctx.send("*{}*".format(line))
  else:
    await ctx.send("I was unable to find the queried song. My apologies, I'm only a genius in name. " +
    "Check for typos and try again.")

bot.add_cog(Music(bot))

#keep_alive.keep_alive()

bot.run('ODA4NzEzMzQ0MDI2NDExMDY5.YCKi_g.f8NrqPI2NtCtzIoER_pV-d05rtQ')  