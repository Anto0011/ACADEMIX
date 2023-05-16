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
print(openai.api_key)

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
    result = response["choices"][0]["text"] #type: ignore
    return result

#Question and answer database management
def add_question(question, topic_name, level, student_id):
    #Get the primary key of the course
    id = courseManagement.keys(topic_name)

    #Check if the question already exists
    sql = "SELECT question_content FROM Questions WHERE question_content REGEXP(%s)"
    mycursor.execute(sql, (question))#type: ignore
    result = mycursor.fetchall()

    sql = "INSERT INTO group1.Questions (question_context, course_id, question_level) VALUES (%s, %s, %s);"
    mycursor.execute(sql, (question, id, level))
    


def add_answer(answer, subject_name, topic_content):
    
