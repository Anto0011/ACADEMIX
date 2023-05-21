import openai
import settings
import courseManagement
import mysql.connector

ht="193.204.40.146"
user="gr1"
pwd="group1#23"
db="group1"

mydb = mysql.connector.connect(
    host = ht,
    user = user,
    password = pwd,
    database = db
)

mycursor = mydb.cursor()

#Openai api key
openai.api_key = settings.OPENAI_API_KEY

#Define propmpt and question functions
def prompt(Prompt, num, temp):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= Prompt,
    max_tokens= int(num) * 50,
    temperature= temp)
    return response


def ask_gpt(msg):
    response = prompt(msg, 1, 0.35)
    print(response)


def generate_questions(course_id, topic_id, num_questions, difficulty_level):
    Prompt = f"""Generate {num_questions} question(s) and answers for {course_id} on {topic_id} for students preparing for exams and tests. 
    Ensure that your questions and answers cover key concepts and information, and are accurate and factually correct. Difficulty level: {difficulty_level}.
    Desired Format: 
    Q:
    A: """

    response = prompt(Prompt, num_questions, 0.25)
    result = response["choices"][0]["text"] #type: ignore
    return result

#Question and answer database management
def add_question(question, topic_name, level, student_id):
    ...
    


def add_answer(answer, subject_name, topic_content):
    pass
