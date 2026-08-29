import sys 
import os 
import wave
from ollama import Client
from ollama import chat

client = Client(headers={'Authorization': f"Bearer {os.getenv('OLLAMA_API_KEY')}"})

def fetch_content(text):
    response = client.web_search(text)
    link = response['results'][0]['url']
    print("Retrieved URL: ", link)

    summ = client.web_fetch(link)
    content = summ['content']
    # print(content)
    return content


def summarize_news(content):
    prompt = "Summarize this into a short text, keep the key information and do not make up any unmentioned information. \n" + content
    final = chat(model = 'qwen3:4b', messages=[{'role': 'user', 'content': f'{prompt}'}], stream=True)

    to_speak = ""

    print("*** SUMMARIZED NEWS ***")
    for i in final:
        to_speak += i['message']['content']
        print(i['message']['content'], end='')
    print("\n*** DONE NEWS ***\n")

    return to_speak