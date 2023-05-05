import csv
import os
from datetime import datetime
from utils.model_factory import ModelFactory
import uuid

class BitcoinDataGenerator:
    def __init__(self, model_name,  api_keys=None):
        model_factory = ModelFactory(api_keys)
        self.model = model_factory.get_model(model_name)

    def generate_bitcoin_questions(self, bitcoin_topic, number_of_questions_to_generate):
        user_input = f"Generate a unique question about: {bitcoin_topic}."
        number_token_ids = list(range(0, 10))  # Token ids for numbers 0-9
        log_bias = {str(token_id): -5.0 for token_id in number_token_ids}

        unique_questions = set()
        max_retries = number_of_questions_to_generate*5
        retry_count = 0

        while len(unique_questions) < number_of_questions_to_generate and retry_count < max_retries:
            question = self.model.respond_to_prompt(user_input, log_bias=log_bias)
            
            if question and question not in unique_questions:
                unique_questions.add(question)
            retry_count += 1

        if retry_count == max_retries:
            print(f"Warning: Unable to generate the desired number of unique questions within {max_retries} attempts.")
            
        return list(unique_questions)

    def answer_questions(self, questions):
        answers = []
        for question in questions:
            answer = self.model.respond_to_prompt(question)
            answers.append(answer if answer else "No answer found.")
        return answers

    def save_question_to_csv(self, filename, question, model_name, topic):
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)

            if not file_exists:
                csv_writer.writerow(["QuestionID", "ModelName", "Topic", "Question", "Datetime"])

            question_id = uuid.uuid4()
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            csv_writer.writerow([question_id, model_name, topic, question, current_datetime])

        return question_id

    def save_answer_to_csv(self, filename, question_id, model_name, answer):
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)

            if not file_exists:
                csv_writer.writerow(["QuestionID", "ModelName", "Answer", "Datetime"])

            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            csv_writer.writerow([question_id, model_name, answer, current_datetime])

