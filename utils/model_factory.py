from models import GPT3PromptEngModel, GPT3QuestionModel, GPT3DefaultModel

class ModelFactory:
    def __init__(self, api_keys=None):
        self.api_keys = api_keys or {}

    def get_model(self, model_name):
        if model_name == "gpt3.5 (v0.1)":
            openai_api_key = self.api_keys.get("openai")
            if not openai_api_key:
                raise ValueError("An OpenAI API key is required for this model.")
            return GPT3PromptEngModel(openai_api_key)
        elif model_name == "gpt3.5 question (v0.1)":
            openai_api_key = self.api_keys.get("openai")
            if not openai_api_key:
                raise ValueError("An OpenAI API key is required for this model.")
            return GPT3QuestionModel(openai_api_key)
        elif model_name == "gpt3.5 default":
            openai_api_key = self.api_keys.get("openai")
            if not openai_api_key:
                raise ValueError("An OpenAI API key is required for this model.")
            return GPT3DefaultModel(openai_api_key)
        # Add more conditions here for different models
        else:
            raise ValueError(f"Model '{model_name}' not supported.")
