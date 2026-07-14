import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Alex. You are a helpful and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#I think that if I delete the word history from the code then the chatbot will not be able to remember the previous messages in the conversation.
#the ai doesn't have memory

#I don't think that deleting load_dotenv() would affect the chatbot's ability to function, but it would prevent the program from loading environment variables from a .env file.
#
#I think deleting temperature=0.7 will automatically set the temperature to its default value, which may affect the randomness and creativity of the chatbot's responses.