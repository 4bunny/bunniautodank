import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "$"

#use the .env feature to hide your token

keep_alive()
token = ()
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Hepi Autodanker", color=420699, description=f"**{prefix}autodank**\nsends pls beg, pls fish, pls hunt and pls dep all every 50 seconds.\n\n**{prefix}stopautodank**\nstops autodank.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839038715745402894/839043776444891156/unknown-7.png")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}succefully begged")
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succefully fished")
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succefully hunt")
			await ctx.send('pls dep all')
			print(f"{Fore.GREEN}succefully deposited all")
			await asyncio.sleep(47)


@bot.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **disabled**!')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="T'_T", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██║░██╔╝██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██║███████║██╔██╗██║█████═╝░█████╗░░██████╔╝
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░██║██╔══██║██║╚████║██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║░╚███║██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

selfbot is ready!
''')

bot.run(token, bot=False)

