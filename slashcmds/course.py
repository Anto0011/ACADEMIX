import discord
from discord import app_commands
from courseManagement import add_course, add_topic, remove_course, remove_topic, get_existing_courses, get_existing_topics
import typing
from re import A
from login_register import login_manager


class courses(app_commands.Group):

    #autocompletion for courses
    async def course_autocompletion(self, 
        interaction: discord.Interaction, 
        current: str) -> typing.List[app_commands.Choice[str]]:
        # Retrieve existing courses from the database
        existing_courses = get_existing_courses(interaction.user.name)

        # Generate autocomplete choices based on existing courses
        data = []
        if login_manager.is_logged_in(interaction.user.name):
            for course_name in existing_courses: #type: ignore
                if current.lower() in course_name.lower():
                    data.append(app_commands.Choice(name=course_name, value=course_name))
            return data
        else:
            return data

    #autocompletion for topics
    async def topic_autocompletion(self, 
        interaction: discord.Interaction, 
        current: str) -> typing.List[app_commands.Choice[str]]:
        # Retrieve existing courses from the database
        existing_topics = get_existing_topics(interaction.user.name)

        # Generate autocomplete choices based on existing courses
        data = []
        if login_manager.is_logged_in(interaction.user.name):
            for topic_name in existing_topics: #type: ignore
                if current.lower() in topic_name.lower():
                    data.append(app_commands.Choice(name=topic_name, value=topic_name))
            return data
        else:
            return data
    
    # Add course command
    @app_commands.command()
    async def add_course(self, interaction: discord.Interaction, coursename: str):
        # Check if the user is logged in
        if login_manager.is_logged_in(interaction.user.name):
            # Add the course
            result = add_course(coursename, interaction.user.name)

            # Send a response message
            await interaction.response.send_message(f"{result}", ephemeral=True)
        else:
            # Send an error message for not being logged in
            await interaction.response.send_message(f"Please login first", ephemeral=True)


    # Add topics command
    @app_commands.command()
    @app_commands.autocomplete(course_name=course_autocompletion)
    async def add_topic(self, interaction: discord.Interaction, course_name: str, topic_name: str):
        # Check if the user is logged in
        if login_manager.is_logged_in(interaction.user.name):
            # Add the topic
            result = add_topic(course_name, topic_name)

            # Send a response message
            await interaction.response.send_message(f"{result}", ephemeral=True)
        else:
            # Send an error message for not being logged in
            await interaction.response.send_message(f"Please login first", ephemeral=True)


    # Remove course command
    @app_commands.command()
    @app_commands.autocomplete(course_name=course_autocompletion)
    async def remove_course(self, interaction: discord.Interaction, course_name: str):
        # Check if the user is logged in
        if login_manager.is_logged_in(interaction.user.name):
            # Remove the course
            result = remove_course(course_name, interaction.user.name)

            # Send a response message
            await interaction.response.send_message(f"{result}", ephemeral=True)
        else:
            # Send an error message for not being logged in
            await interaction.response.send_message(f"Please login first", ephemeral=True)


    # Remove topic command
    @app_commands.command()
    @app_commands.autocomplete(course_name=course_autocompletion, topic_name=topic_autocompletion)
    async def remove_topic(self, interaction: discord.Interaction, course_name: str, topic_name: str):
        # Check if the user is logged in
        if login_manager.is_logged_in(interaction.user.name):
            # Remove the topic
            result = remove_topic(topic_name, interaction.user.name)

            # Send a response message
            await interaction.response.send_message(f"{result}", ephemeral=True)
        else:
            # Send an error message for not being logged in
            await interaction.response.send_message(f"Please login first", ephemeral=True)



#Setup
async def setup(bot):
    bot.tree.add_command(courses(name="study_guide", description="Course management commands"))
