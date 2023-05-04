import requests
from Config import Config

CFG = Config()


class AIProvider:
    def instruct(self, prompt):
        response = requests.post(
            f"{CFG.AI_PROVIDER_URI}/v1/chat/completions",
            json={
                "model": CFG.AI_MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": CFG.AI_TEMPERATURE,
                "max_tokens": CFG.MAX_TOKENS
            },
            headers={
                "User-Agent": "curl/7.54"  # the default causes a httpx.ReadTimeout exception?!
            }
        )
        if response.ok:
            return response.json()["choices"][0]["message"]["content"]
        return "ERROR"
