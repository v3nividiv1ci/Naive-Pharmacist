import os
import time
import random
from openai import OpenAI
import json
from retrying import retry
import requests

class GPT4:
    def __init__(self, model) -> None:
        self.key_ind = 0
        self.model = model
        self.url = os.environ["OPENAI_BASE_URL"] + '/chat/completions'
        self.key = os.environ["OPENAI_API_KEY"] 

        print(f'keys: {self.key}')
        print(f'use model of {self.model}')

    def openai_call(self, content ,args = {}):
        api_key = self.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        parameters = {
            "model": self.model,
            "messages": [{'role': 'user', 'content': content}],
            **args,
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=parameters
        )

        response = json.loads(response.content.decode("utf-8"))
        if 'error' in response:
            assert False, str(response)
        return response['choices'][0]['message']['content']

    @retry(wait_fixed=100, stop_max_attempt_number=3)
    def call(self, content, args = {}):
        return self.openai_call(content, args)