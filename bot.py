# bot.py
import os
import discord
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import pytz
import calendar

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
CHANNEL = int(os.getenv('DISCORD_CHANNEL'))

client = discord.Client(intents=discord.Intents.default())

async def send_msg_on_time():
    pst = pytz.timezone('America/Los_Angeles')
    now = datetime.now(pst)
    month_name = calendar.month_name[now.month]
    if now.hour == 0:
        await discord_channel.create_thread(name=f"{month_name} {now.day}", type=discord.ChannelType.public_thread)

@client.event
async def on_ready():
    global discord_channel
    guild = discord.utils.get(client.guilds, id=GUILD)

    discord_channel = guild.get_channel(CHANNEL) 

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_msg_on_time, trigger='interval', hours=1)
    scheduler.start()

client.run(TOKEN)
