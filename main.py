import os
import openai
from dotenv import load_dotenv


def request(question: str) -> str:
    openai.organization = os.getenv('ORG_ID')
    openai.api_key = os.getenv('API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    load_dotenv()

    question = ""
    print("Olá sou o chat GPT no seu PC! me pergunte algo ou escreva fim\n")

    while question == "":
        question = input("\nPode Perguntar:\n")
        if question.lower() == "fim":
            break
        print(request(question))
        question = ""


