import requests


def generer_bilde(tekst, apiKey):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey,
    }
    data = {
        "prompt": tekst,
        "n": 2,
        "size": "1024x1024"
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    print(data)
    return [i["url"] for i in data["data"]]


def generer_svar(tekst, apiKey):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey,
    }
    data = {
        "model": "text-davinci-003",
        "prompt": tekst,
        "max_tokens": 800,
        "temperature": 0.2,
        "n": 1
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    return data["choices"][0]["text"]
