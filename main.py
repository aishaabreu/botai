import os
import requests
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_KEY', default='')
API_URL = os.getenv('API_URL', default='https://api.openai.com/v1/completions')
IA_MODEL = os.getenv('IA_MODEL', default='text-davinci-003')


def ask_something(question):
    data = {
        'prompt': question,
        'model': IA_MODEL,
    }

    response = requests.post(API_URL, json=data, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }).json()

    return response.get(
        'choices', [{
            'text': 'ERRO: ' + response.get('error', {}).get('message')
        }]
    )[0].get('text').strip()


if __name__ == '__main__':
    while True:
        question = input('> ')
        if question.lower().strip() == 'exit':
            break
        print(ask_something(question))
