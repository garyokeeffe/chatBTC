import data_generation.data_gen_helpers as dg
import os
from dotenv import load_dotenv

# Load in API Key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Example Data Gra
bitcoin_topic = "Bitcoin mining"
number_of_questions_to_generate = 10
location_to_save = "data_generation/training_data/chatgpt_training_data.csv"
bitcoin_questions = dg.BitcoinQuestions(openai_api_key)

questions = bitcoin_questions.generate_bitcoin_questions(bitcoin_topic, number_of_questions_to_generate)
answers = bitcoin_questions.answer_questions(questions)
bitcoin_questions.save_training_data_to_csv(location_to_save, questions, answers)

