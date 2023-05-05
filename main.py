import os
from dotenv import load_dotenv
from data_generation.bitcoin_data_generator import BitcoinDataGenerator

# Load in API Key from .env file
load_dotenv()
api_keys = {"openai": os.getenv("OPENAI_API_KEY")}

# Example Data Generation
bitcoin_topic = "Cold Storage Best Practices"
number_of_questions_to_generate = 3
question_save_location = "data/questions/data.csv"
answer_save_location = "data/answers/data.csv"

question_model = "gpt3.5 question (v0.1)"
answer_model = "gpt3.5 (v0.1)"
# Create BitcoinDataGenerator instance with the desired model names for generating and answering questions
question_data_generator = BitcoinDataGenerator(model_name=question_model, api_keys=api_keys)
answer_data_generator = BitcoinDataGenerator(model_name=answer_model, api_keys=api_keys)
# Generate questions
print("generating questions")
questions = question_data_generator.generate_bitcoin_questions(bitcoin_topic, number_of_questions_to_generate)
print("saving questions")
# Save questions to CSV and store their IDs
question_ids = []
for question in questions:
    question_id = question_data_generator.save_question_to_csv(question_save_location, question, question_model, bitcoin_topic)

    question_ids.append(question_id)

# Answer questions and save answers to CSV
print("answering questions")
answers = answer_data_generator.answer_questions(questions)
print("saving answers")
for question_id, answer in zip(question_ids, answers):
    answer_data_generator.save_answer_to_csv(answer_save_location, question_id, answer_model, answer)


