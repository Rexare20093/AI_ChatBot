import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response('I\'m a basic chatbot. I can understand simple greetings and questions!', ['who', 'are', 'you'], required_words=['who', 'you'])
    response('I was created as a simple demonstration of pattern matching in Python.', ['who', 'created', 'you'], required_words=['created', 'you'])
    response('I don\'t have personal experiences or emotions, but I\'m here to chat!', ['how', 'do', 'you', 'feel'], required_words=['you', 'feel'])

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match


def user_bye(user_input):
    if "bye" in user_input.lower():
        return True

    return False

def unknown():
    response = ["Could you please rephrase that? ",
                "...",
                "Sounds interesting.",
                "What does that mean?"][random.randrange(4)]
    return response

# Running the chatbot
print("Bot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    print("Bot:", get_response(user_input))
    if user_bye(user_input):
        break