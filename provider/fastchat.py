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
        print(response.request.__dict__)
        if response.ok:
            print(response.request.body)
            print(response.json())
            return response.json()["data"][0].replace("\n", "\n")
        print("Response not OK")
        return "ERROR"
