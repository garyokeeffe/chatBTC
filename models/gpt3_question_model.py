# gpt3_question_model.py
from utils.openai_api import create_payload, make_request_and_process_response, url

class GPT3QuestionModel:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.headers = {"Authorization": f"Bearer {openai_api_key}"}

    def respond_to_prompt(self, prompts, log_bias=None, temperature=0.8, max_tokens=500, stop=None):
        if not isinstance(prompts, list):
            prompts = [prompts]

        initial_prompt = [
            {"role": "system", "content": "You are an expert at Bitcoin Onboarding and you know all the challenging and easy questions so that you can learn everything about Bitcoin."},
        ]

        for prompt in prompts:
            initial_prompt.append({"role": "user", "content": prompt})

        payload = create_payload("gpt-3.5-turbo", initial_prompt, temperature, stop=stop, max_tokens=max_tokens, logit_bias=log_bias)

        response = make_request_and_process_response(url, self.headers, payload)
        return response[0] if response else "No answer found."

