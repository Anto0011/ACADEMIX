import discord
from discord.ext import commands
import settings
from discord import app_commands

#Initialize logger
logger = settings.logging.getLogger("bot")

#Define main loop
def run():
    #Define intents
    Intents = discord.Intents.default()
    Intents.message_content = True
    Intents.guilds = True
    Intents.members = True
    Intents.dm_messages = True

    #initialize bot instance
    bot = commands.Bot(command_prefix="/", intents=Intents)

    #Create on_ready event to set up extensions
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")#type: ignore

        #Load the required discord commands
        await bot.load_extension("slashcmds.course")
        await bot.load_extension("slashcmds.LogReg")
        await bot.load_extension("slashcmds.GPT")


        #Sync the commands with discord server
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)


    #Global error handling
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
           await ctx.send("Handled error globally, missing argument")
    
    #Provide api key and enable logging
    bot.run(settings.DISCORD_API_KEY, root_logger=True)

#Run the bot
if __name__ == "__main__":
    run()

