import os
import openai
from dotenv import load_dotenv
import progress


#Load api key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY


#print(openai.Model.list())

#Define propmpt and question functions
def prompt(Prompt, num):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= Prompt,
    max_tokens= int(num) * 50,
    temperature=0.25)
    return response

def generate_questions(course_id, topic_id, num_questions, difficulty_level):
    Prompt = f"""Generate {num_questions} questions and answers for {course_id} on {topic_id} for students preparing for exams and tests. 
    Ensure that your questions and answers cover key concepts and information, and are accurate and factually correct. Difficulty level: {difficulty_level}.
    Desired Format: 
    Q:
    A: """

    response = prompt(Prompt, num_questions)
    result = response["choices"][0]["text"] # type: ignore
    print(result)


#Call generate_question function

question = "Describe the concept of 2 sided network effects focusing on its distinctive characteristics and provide a company as an example"


answer = """Two sided network effects should contain two types of entities, like buyers and sellers.
As an example we can choose uber because they have drivers and users who each benefit from each others existence.
As the network of Uber grows it gets more beneficial for two sides (drivers and users)."""

response = prompt(question, 2)
response = response["choices"][0]["text"] # type: ignore
print(response)

progress.check_answer(answer)

