from discord.ext import commands
import question

#Create the question command group
@commands.group()
async def qst(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not exist")

#Ask question command
@qst.command()
async def ask(ctx, *msg):
    string = " ".join(msg)
    author = ctx.author.mention  # Mention the author using `ctx.author.mention`
    result = question.ask_gpt(string)
    await ctx.send(f"{author} {result}")  # Include the author mention in the message content        

#Error handling for !ask function
@qst.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("handled error locally")

async def setup(bot):
    bot.add_command(qst) 