import re
import random
from openai import OpenAI

def openai_response(user_input, MaxToken=50, outputs=1):
    # using OpenAI's Completion module that helps execute
    # any tasks involving text


    client = OpenAI()

    response = client.completions.create(
        # model name used here is text-davinci-003
        # there are many other models available under the
        # umbrella of GPT-3
        model="gpt-3.5-turbo-instruct",
        # passing the user input
        prompt=user_input,
        # generated output can have "max_tokens" number of tokens
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
    )

    return response.choices[0].text


# Running the chatbot
print("Bot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    print("Bot:", openai_response(user_input))
