import random

def simple_chatbot(user_input):
    rules = {
        'hello': ['Hi there!', 'Hello!', 'Hey!'],
        'how are you': ['I am good, thank you!', 'I\'m doing well, thanks for asking. How about you?'],
        'bye': ['Goodbye!', 'See you later!', 'Bye!'],
        'default': ['I\'m not sure how to respond to that.', 'Could you please rephrase that?', 'I didn\'t understand.']
    }

    user_input_lower = user_input.lower()

    for key in rules:
        if key in user_input_lower:
            return random.choice(rules[key])

    return random.choice(rules['default'])

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)

    print("Chatbot:", response)
