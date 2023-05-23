import openai
import settings
import courseManagement

#Load Openai api key
openai.api_key = settings.OPENAI_API_KEY

#Define propmpt structure as a function
def prompt(Prompt, num, temp):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= Prompt,
    max_tokens= int(num) * 50,
    temperature= temp)
    return response

#Define ask_gpt function
def ask_gpt(msg, temp):
    response = prompt(msg, 2, temp)
    result = response["choices"][0]["text"] #type: ignore
    answer = result.find("A:")
    final = result[answer + 3:].strip()
    return final

#Define generate_question
def generate_question(course_name, topic_name, difficulty_level):
    Prompt = f"""Generate a question and answer for {course_name} on {topic_name} topic for a student preparing for exam. 
    Ensure that your question covers key concepts and information, and are accurate and factually correct. Avoid giving unfinished sentences. Change the difficulty of the question based on this difficulty level: {difficulty_level}.
    Desired Format: 
    Q:
    A: """

    response = prompt(Prompt, 2, 0.5)
    result = response["choices"][0]["text"] #type: ignore
    
    # Find the index of the question and answer separators
    question_start = result.find("Q:")
    question_end = result.find("A:")

    # Extract the question and answer from the text
    question = result[question_start + 3:question_end].strip()
    answer = result[question_end + 3:].strip()
    return question,answer

