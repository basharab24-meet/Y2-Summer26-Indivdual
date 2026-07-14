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
        print(response) 
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

#usage.input_tokens: The number of tokens the AI read.
#usage.output_tokens: The number of tokens the AI generated as a response

#I think deleting temperature=0.7 will automatically set the temperature to its default value, which may affect the randomness and creativity of the chatbot's responses.
#tempature controls how unique the answer is.(How creative it is)

#There will be 6 messages in the history: 3 user messages and 3 ChatBot responses
#The api needs the full history every single time so it would be able to create the most fitting and specific responses.

#Reflection: In my day to day life, I see how snacks brands reduce the amount of snacks in their products, and then they don't have to raise prises.
#Another thing I see is that when you rent electrial bicycles, they charge you for the time you use it, and then they charge you for the distance you travel. This is similar to how the AI charges for the number of tokens used in a conversation.

# Delete: history.append({'role': 'user', 'content': user_input})
# The AI no longer receives the user's message in the conversation history, so it cannot remember or respond to it correctly.

# Delete: history.append({'role': 'assistant', 'content': reply})
# The AI forgets its previous replies, so only the user's messages are remembered and the input token count grows more slowly.

# Delete: print("History so far:", history)
# The chatbot behaves exactly the same, but you can no longer see the conversation history for debugging.

#I didn't have bugs