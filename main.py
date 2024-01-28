import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.BOT(command_prefix='!', intents=intents)

@bot.events
async def on_ready():
  print('Bot is ready!')
  print('---------')

@bot.command()
async def ping(ctx):
  await ctx.send("pong!")

bot.run("PUT YOUR DISCORD BOT TOKEN HERE!")
