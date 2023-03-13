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

rating_scale_string = "Song Rating Scale:\n :pinched_fingers: = Already in playlist\n <:pogandthenvomit:981790516704321536> = Added to " \
                      "playlist\n <:puggers:834872002330099774> = Great\n <:pugde:981786329551601715> = " \
                      "Decent\n <:honk:692203239730446389> = Okay\n <:perish:732352949824782417> = Not a fan"

async def send_msg_on_time():
    pst = pytz.timezone('America/Los_Angeles')
    now = datetime.now(pst)
    month_name = calendar.month_name[now.month]
    if now.hour == 0:
        await discord_channel.send("Bumbling up some new bops... :bee: :point_down:")
        new_thread = await discord_channel.create_thread(name=f"{month_name} {now.day}",
                                                         type=discord.ChannelType.public_thread)
        await new_thread.send(rating_scale_string)

@client.event
async def on_ready():
    global discord_channel
    guild = discord.utils.get(client.guilds, id=GUILD)

    discord_channel = guild.get_channel(CHANNEL) 

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_msg_on_time, trigger='interval', hours=1)
    scheduler.start()

client.run(TOKEN)
