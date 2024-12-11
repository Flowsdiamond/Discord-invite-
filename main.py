import discord 
from discord.ext import commands


TOKEN = 'TOKEN'
WELCOME_CHANNEL_ID = Канал ID куда отправляется сообщение


intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix="!", intents=intents)




@bot.event
async def on_ready():
    print(f'Начал свою работу {bot.user.name}')


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f'Добро пожаловать на сервер {member.mention}! 🎉')

bot.run(TOKEN)