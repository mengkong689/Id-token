import discord
from discord.ext import commands
import requests

TOKEN = 'YOUR_BOT_TOKEN_HERE' # Replace with your bot token
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
print(f'Logged in as {bot.user}')

@bot.command()
async def grabtoken(ctx, user_id: int):
url = f'https://discord.com/api/v9/users/{user_id}'
headers = {
'Authorization': f'Bot {TOKEN}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
data = response.json()
await ctx.send(f'Token for User ID {user_id}: {data["token"]}')
else:
await ctx.send('Failed to retrieve token.')

@bot.command()
async def sendmessage(ctx, channel: discord.TextChannel, *, message: str):
await channel.send(message)

@bot.command()
async def deletemessage(ctx, message_id: int):
message = await ctx.fetch_message(message_id)
await message.delete()

@bot.command()
async def listmembers(ctx):
members = ctx.guild.members
member_list = '\n'.join([member.name for member in members])
await ctx.send(f'Members in {ctx.guild.name}:\n{member_list}')

bot.run(TOKEN)
