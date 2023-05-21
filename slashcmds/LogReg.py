import discord
from discord import app_commands
from discord.ext import commands
import login_register
from login_register import login_manager

class access(app_commands.Group):

    #Register command
    @app_commands.command()
    @app_commands.describe(Email="Enter your email address", Password="Enter your password")
    @app_commands.rename(Email="email", Password="password")
    async def register(self, interaction: discord.Interaction, Email: str, Password: str):
        studentName = interaction.user.name
        print(studentName)
        result = login_register.register_user(studentName, Email, Password)
        await interaction.response.send_message(f"{result} {interaction.user.mention}")


    #Login command
    @app_commands.command()
    @app_commands.describe(Email="Enter your email address", Password="Enter your password")
    @app_commands.rename(Email="email", Password="password")
    async def login(self, interaction: discord.Interaction, Email: str, Password: str):
        result = login_register.login_user(Email, Password)
        if result != False:
            login_manager.login(interaction.user.name)
            await interaction.response.send_message(f"Welcome back {interaction.user.mention}!")
        else:
            await interaction.response.send_message(f"Incorrect username or password")

    #Logout command
    @app_commands.command()
    async def logout(self, interaction: discord.Interaction):
        if login_manager.is_logged_in(interaction.user.name):
            login_manager.logout(interaction.user.name)
            if login_manager.is_logged_in != True:
                await interaction.response.send_message(f"Logged out successfully!", ephemeral=True)
            else:
                print("Couldn't log out")
        else:
            await interaction.response.send_message(f"You can't log out without logging in first")

#Setup
async def setup(bot):
    bot.tree.add_command(access(name="access", description="User registration and login functions"))
