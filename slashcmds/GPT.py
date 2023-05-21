import discord
from discord import app_commands
from discord.ext import commands
from login_register import login_manager
from question import generate_question, ask_gpt
from courseManagement import get_existing_courses, get_existing_topics
import typing
from re import A
import asyncio


class GPT(app_commands.Group):

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

    #autocompletion for difficulty
    async def difficulty_autocompletion(self, 
        interaction: discord.Interaction, 
        current: str) -> typing.List[app_commands.Choice[str]]:        
        data = [app_commands.Choice(name="Easy", value="Easy"), app_commands.Choice(name="Medium", value="Medium"), app_commands.Choice(name="Hard", value="Hard")]
        return data



    @app_commands.command()
    @app_commands.autocomplete(course=course_autocompletion, topic=topic_autocompletion, difficulty=difficulty_autocompletion)
    async def generate_question(self, interaction: discord.Interaction, course: str, topic: str, difficulty: str):
        if login_manager.is_logged_in(interaction.user.name):
            # Defer the initial response
            await interaction.response.defer()

            #Generate the question/answer
            Question,Answer = generate_question(course, topic, difficulty)

            # Wait for a specific duration (if necessary)
            await asyncio.sleep(3)

            user = interaction.user
            dm_channel = await user.create_dm()
            await dm_channel.send(content=f"Question: {Question}\n\n Answer: ||{Answer}||")
        else:
            await interaction.response.send_message(f"Please login first", ephemeral=True)

    @app_commands.command()
    async def ask_gpt(self, interaction: discord.Interaction, question: str, temp: float):
        if login_manager.is_logged_in:
            # Defer the initial response
            await interaction.response.defer()

            #Generate the question/answer
            answer = ask_gpt(question, temp)

            user = interaction.user
            dm_channel = await user.create_dm()
            await dm_channel.send(content=f"Question: {question}\n\n Answer: {answer}")
        else:
            await interaction.response.send_message(f"Please login first", ephemeral=True)
    

#Setup
async def setup(bot):
    bot.tree.add_command(GPT(name="gpt", description="Question generation"))