from inspect import indentsize
import discord
import config
from discord.ext import commands
import login_register





# Initialize bot
bot = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all())

# Setup
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"{config.PREFIX}help"))
    print("-------")
    print("Bot is online ✅")
    print("-------")

# Run the bot
on_ready()


def run():
    Intents = discord.Intents.default()
    Intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=Intents)

    #Register command


    #Login command
    @bot.command()
    async def login(message):


    # select course command
    @bot.command()
    async def select_course(ctx):
       await ctx.send(f"session_id")

    # add course command
    @bot.command()
    async def add_course(course_name):
        pass

    # #Add a new topic under a course command
    @bot.command()
    async def add_topic(course_name, topic_content):
        pass

    #Remove a course and related topics
    @bot.command()
    async def remove_course(course_name, topic_content):

        pass

    # Remove a topic under a course
    @bot.command()
    async def remove_topic(course_name, topic_content):
        pass

    # Remove all topics under a course
    @bot.command()
    async def remove_all_topics(course_name, topic_content):
        pass
    
    bot.run(config.TOKEN)

run()

