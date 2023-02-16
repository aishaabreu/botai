import os
import requests
import telebot
from dotenv import load_dotenv
load_dotenv()

BOT_KEY = os.getenv('BOT_KEY', default='')
API_KEY = os.getenv('API_KEY', default='')
API_URL = 'https://api.openai.com/v1/completions'
IA_MODEL = 'text-davinci-003'
IA_CONTEXT = os.getenv('IA_CONTEXT', default='')

bot = telebot.TeleBot(BOT_KEY)


@bot.message_handler(func=lambda m: True)
def responder(mensagem):
    text = f"""
    {IA_CONTEXT}
    {mensagem.text}
    """
    bot.send_message(mensagem.chat.id, ask_something(text))


def ask_something(question):
    data = {
        'prompt': question,
        'model': IA_MODEL,
        'max_tokens': 4000,
        'n': 1
    }

    response = requests.post(API_URL, json=data, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }).json()

    return response.get(
        'choices', [{
            'text': 'ERRO: ' + response.get('error', {}).get('message', '')
        }]
    )[0].get('text').strip()


if __name__ == '__main__':
    bot.polling()
