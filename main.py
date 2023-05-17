import discord
from discord.ext import commands
import question
import settings
from cogs.greetings import Greetings

logger = settings.logging.getLogger("bot")

class NotOwner(commands.CheckFailure):
    ...

def is_owner():
    async def predicate(ctx):
        if ctx.author.id != ctx.guild.owner_id:
            raise NotOwner("Hey, you are not the owner")
        return True
    return commands.check(predicate)

def run():
    Intents = discord.Intents.default()
    Intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=Intents)

    #Create on_ready event to set up extensions and logger
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")#type: ignore

        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")


    #Load, Unload, and Reload extensions
    @bot.command()
    #@is_owner()
    async def load(ctx, cog: str):
        await bot.load_extension(f"cogs.{cog.lower()}")

    @bot.command()
    #@is_owner()
    async def unload(ctx, cog: str):
        await bot.unload_extension(f"cogs.{cog.lower()}")

    @bot.command()
    #@is_owner()
    async def reload(ctx, cog: str):
        await bot.reload_extension(f"cogs.{cog.lower()}")

    #Error handling for load unload and reload
    @load.error
    async def load_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")
    
    @unload.error
    async def unload_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")
    
    @reload.error
    async def reload_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")


    #Global error handling for 
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
           await ctx.send("handled error globally")
    
    bot.run(settings.DISCORD_API_KEY, root_logger=True)

if __name__ == "__main__":
    run()

