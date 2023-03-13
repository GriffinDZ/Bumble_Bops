# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import pytz
import calendar

load_dotenv()
TOKEN = os.getenv('TEST_DISCORD_TOKEN')
GUILD = int(os.getenv('TEST_DISCORD_GUILD'))
CHANNEL = int(os.getenv('TEST_DISCORD_CHANNEL'))

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

rating_scale_string = "Song Rating Scale:\n :pinched_fingers: = Already in playlist\n :pogandthenvomit: = Added to " \
                      "playlist\n :puggers: = Great\n :pugde: = " \
                      "Decent\n :honk: = Okay\n :perish: = Not a fan"

async def send_msg_on_time():
    pst = pytz.timezone('America/Los_Angeles')
    now = datetime.now(pst)
    month_name = calendar.month_name[now.month]
    if True:
        await discord_channel.send("Bumbling up some new bops... :bee: :point_down:")
        new_thread = await discord_channel.create_thread(name=f"{month_name} {now.day}", type=discord.ChannelType.public_thread)
        await new_thread.send(rating_scale_string)

@tree.command(name = "spotifytoyoutube", description = "Convert a Spotify link to a YouTube link", guild=discord.Object(id=GUILD)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "youtubetospotify", description = "Convert a YouTube link to a Spotify link", guild=discord.Object(id=GUILD)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    global discord_channel
    guild = discord.utils.get(client.guilds, id=GUILD)
    await tree.sync(guild=guild)

    discord_channel = guild.get_channel(CHANNEL) 

    scheduler = AsyncIOScheduler()
    # scheduler.add_job(send_msg_on_time, trigger='interval', seconds=5)
    scheduler.add_job(send_msg_on_time)

    scheduler.start()

client.run(TOKEN)