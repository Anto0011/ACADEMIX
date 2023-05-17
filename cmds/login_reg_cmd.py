from discord.ext import commands
import login_register

@commands.group()
async def user(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not exist")


#Register command
@user.command()
async def register(ctx):
    msg = login_register.register_user("ali", "ali@gmail.com", "anto1.")
    await ctx.send(msg)

#Login command
@user.command()
async def login(message):
    id = login_register.login_user("alllli@gmail.com", "anto1.")
    if id != False:
        await message.send("Login successfull")
        student_id = id
        await message.send("student id = ", student_id)
    else:
        await message.send("Incorrect email or password")


async def setup(bot):
    bot.add_command(user) 