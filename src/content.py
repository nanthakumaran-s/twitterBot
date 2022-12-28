import openai

def generate(openai_key):
    openai.api_key=openai_key
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Write a tweet about python in less than 120 characters",
        max_tokens=64,
    )
    return completion["choices"][0]["text"]