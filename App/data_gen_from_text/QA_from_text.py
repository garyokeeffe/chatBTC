import openai
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

openai.api_key  = os.getenv('OPENAI_API_KEY')
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
},
{
  "Question_ID":".."
  "Question": ".."
  "Answer": ".."
},
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

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_response(text, filename='BTC'):

    prompt = f"""
        From the following article:

        -------

        {text}

        --------

        extract 5 questions and answers from the article, the Answers should be informative and at least 50 word

        and put them in the following JSON format


        {json_format}

        """

    response = get_completion(prompt)
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        clean_text = response.replace('\n','')
        clean_text = clean_text.replace('\\','')
        json_name = f'App/data_gen_from_text/data/json/{filename}_{timestamp}.json'
        with open(json_name, 'w') as f:
            f.write(clean_text)
        print('saved:' +json_name)
    except Exception as error:
        print(error)

    

