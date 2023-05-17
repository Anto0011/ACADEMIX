import os
import openai
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

def check_answer(user_answer):
    #answers = usrString.split("A:")
    Prompt = f"""You are a professor at a university and you have to grade a students answer. Check the answer using correct answer and student answer and score it out of 100. Explain in one sentence how the student can improve the answer. If the student answer captures the essence of the topic don't reduce points. 
    Correct: "Two-sided network effects, also known as indirect network effects, are a phenomenon in which the value of a product or service increases for both sides of the market as more users join the network. This is in contrast to direct network effects, which only increase the value for one side of the market. An example of a two-sided network effect is the marketplace of eBay. As more buyers join eBay, more sellers are incentivized to join the platform, and vice versa. This creates a virtuous cycle in which the value of the platform increases for both buyers and sellers. As the network grows, eBay is able to offer more products and services, which further increases the value of the platform for both buyers and sellers."
    Student: "{user_answer}"
    
    Desired format:
    Score = 
    explanation = 
    """
    response = prompt(Prompt, 1)
    result = response["choices"][0]["text"] # type: ignore
    print(result)

def check_answer2(question):
    Prompt = """"""

# Analytics and progress tracking functions
def update_user_progress(user_id, topic_id, ):
    #number of questions answered correctly and total questions answered
    #add progress command to bot
    pass

def get_user_progress():
    # TODO: Retrieve the progress of the current user
    pass


