import discord
from discord import app_commands
from discord.ext import commands
import login_register
from login_register import login_manager

class access(app_commands.Group):


    # Register command
    @app_commands.command()
    @app_commands.describe(Email="Enter your email address", Password="Enter your password")
    @app_commands.rename(Email="email", Password="password")
    async def register(self, interaction: discord.Interaction, Email: str, Password: str):
        # Get the name of the student
        studentName = interaction.user.name

        # Check if the user is already logged in
        if login_manager.is_logged_in(studentName):
            await interaction.response.send_message("You are already logged in. Please log out before registering.")
            return

        # Register the user
        result = login_register.register_user(studentName, Email, Password)

        # Send a response message
        await interaction.response.send_message(f"{result} {interaction.user.mention}")


    # Login command
    @app_commands.command()
    @app_commands.describe(Email="Enter your email address", Password="Enter your password")
    @app_commands.rename(Email="email", Password="password")
    async def login(self, interaction: discord.Interaction, Email: str, Password: str):
        # Attempt to login the user
        result = login_register.login_user(Email, Password)

        # Check if the login was successful
        if result:
            # Mark the user as logged in
            login_manager.login(interaction.user.name)

            # Send a welcome message
            await interaction.response.send_message(f"Welcome back {interaction.user.mention}!")
        else:
            # Send an error message for incorrect username or password
            await interaction.response.send_message(f"Incorrect username or password")


    # Logout command
    @app_commands.command()
    async def logout(self, interaction: discord.Interaction):
        # Check if the user is logged in
        if login_manager.is_logged_in(interaction.user.name):
            # Logout the user
            login_manager.logout(interaction.user.name)

            # Check if the logout was successful
            if not login_manager.is_logged_in(interaction.user.name):
                await interaction.response.send_message(f"Logged out successfully!", ephemeral=True)
            else:
                print("Couldn't log out")
        else:
            await interaction.response.send_message(f"You can't log out without logging in first")


#Setup
async def setup(bot):
    bot.tree.add_command(access(name="access", description="User registration and login"))
