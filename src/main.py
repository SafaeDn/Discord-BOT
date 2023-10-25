from discord.ext import commands
import discord
import random
from discord.utils import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 000000  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    num = random.randint(0, 6)
    await ctx.send(num)

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send(f"Salut tout seul {message.author.mention}")
    await bot.process_commands(message)

@bot.command()
async def admin(ctx, username):
    role = get(ctx.guild.roles, name="Admin")
    if role is None:
        role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions(administrator=True))
    member = get(ctx.guild.members, name=username)
    if member:
        print(member)
        await member.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {member} has been given a role called: {role.name}")



token = ""
bot.run(token)  # Starts the bot