import openai
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


openai.api_key = os.getenv('api_key')


def get_response(message: str) -> str:
    p_message = message.lower()

    if "!" in p_message:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": p_message}
            ]
        )
        return completion['choices'][0]['message']['content']

    if "/" in p_message:
        response = openai.Image.create(
            prompt=p_message,
            n=1,
            size="256x256",
        )
        return response["data"][0]["url"]


def get_response_private(message: str) -> str:
    p_message = message.lower()

    if "!" in p_message:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": p_message}
            ]
        )
        return completion['choices'][0]['message']['content']
    if "/" in p_message:
        response = openai.Image.create(
            prompt=p_message,
            n=1,
            size="256x256",
        )
        return response["data"][0]["url"]
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": p_message}
            ]
        )
        return completion['choices'][0]['message']['content']
