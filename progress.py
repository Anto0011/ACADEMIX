import os
import openai
import pandas as pd
from dotenv import load_dotenv

#Load api key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY


def prompt(Prompt, num):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= Prompt,
    max_tokens= 50,
    temperature=0.25)
    return response


# Practice mode functions
def get_random_question(topic_id, difficulty_level):
    # TODO: Retrieve a random question from the specified topic and difficulty level
    pass


usrString = "A: The chemical reactions are the same. A: The same poles repel each other. A: Rain only falls when there's a temperature change."



def check_answer(question_id, answer_id, user_answer):
    #answers = usrString.split("A:")
    Prompt = """You are a professor at a university and you have to grade a students answer. Check the answer using correct answer and student answer and score it out of 100. Explain in one sentence how the student can improve the answer.
    Correct: "A dictionary in Python is an unordered collection of data values, used to store data in key-value pairs."
    Student: "A dictionary can hold 2 matching values with value and key"
    
    Desired format:
    Score = 
    explanation = 
    """
    response = prompt(Prompt, 1)
    result = response["choices"][0]["text"] # type: ignore
    print(result)



# Analytics and progress tracking functions
def update_user_progress(user_id, topic_id, ):
    #number of questions answered correctly and total questions answered
    #add progress command to bot
    pass

def get_user_progress():
    # TODO: Retrieve the progress of the current user
    pass

