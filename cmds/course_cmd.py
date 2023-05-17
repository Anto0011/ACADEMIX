from discord.ext import commands
import courseManagement


@commands.group()
async def course(ctx):
    if ctx.invoked_subcommand is None:
         await ctx.send(f"No, {ctx.subcommand_passed} does not exist")

# add course command
@course.command()
async def add_course(course_name):
    pass

#Remove a course and related topics
@course.command()
async def remove_course(course_name, topic_content):
    pass

# select course command
@course.command()
async def select_course(ctx, msg):
    await ctx.send(f"session_id")

async def setup(bot):
    bot.add_command(course) 