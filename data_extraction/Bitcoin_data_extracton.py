import openai
import os
from dotenv import load_dotenv
import datetime

class ResponseGenerator:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

    def get_response(self, text, filename='BTC'):
        json_format = """
        {
          "Question_ID":".."
          "Question": ".."
          "Answer": ".."
        },
        {
          "Question_ID":".."
          "Question": ".."
          "Answer": ".."
        }
        """

        prompt = f"""
        From the following article:

        -------

        {text}

        --------

        extract 10 questions and answers from the article, the Answers should be informative and at least 50 word

        and put them in the following JSON format

        {json_format}
        """

        response = self.get_completion(prompt)
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            clean_text = response.replace('\n','')
            clean_text = clean_text.replace('\\','')
            json_name = f'{filename}_{timestamp}.json'
            with open(json_name, 'w') as f:
                f.write(clean_text)
            print('saved:' +json_name)
        except Exception as error:
            print(error)



# generator = ResponseGenerator()
# generator.get_response("Saifedean_Ammous__How_Bitcoin_ENDS_Inflation.txt", "Saifedean_Ammous__How_Bitcoin_ENDS_Inflation")
