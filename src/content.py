import openai

def generate(openai_key):
    openai.api_key=openai_key
    completion = openai.Completion.create(engine="text-davinci-003", prompt="Tweet about k8s and microservice architecture")
    print(completion)