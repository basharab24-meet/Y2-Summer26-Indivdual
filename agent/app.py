import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Rick. You are a music Teacher with over 30 years of experience. Teach music theory / rhythm theory (According to what I ask). You should respond in a friendly way but be like a music teacher - be serious about the teaching. Never teach something that is not checked or verified or not correct. Allways answer with clarity, Make your responses organized. If the user types /summary, you will show a summary of the conversation, but it has to be well organized."

    history = []
    user_goal = input("What is your goal for this lesson? ")
    history.append({'role': 'user', 'content': user_goal})
    while True:

        user_input = input(
    f"[Turn {sum(1 for m in history if m['role'] == 'user')}]: you>> "
)

        #user_input = input("[Turn " + str(len(history)) + "]: you>> ")

        if user_input.lower() == 'exit':
            break
        

        history.append({'role': 'user', 'content': user_input})
        #print('History:', history)
        
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        #print(response) 

        reply = response.content[0].text
        print(f'Rick: {reply}')
        
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

#Reflection lab 3:
#Something invisible that shapes how something behaves that outsiders never see is post-traumatic stress disorder (PTSD). People with PTSD may have flashbacks, nightmares, and severe anxiety that can affect their behavior and interactions with others. This is something that outsiders may not see or understand, but it can have a significant impact on the person's life.
#system=system_message: Without this line, the Ai would not be special, it will have no context, so it will have no purpose, unlike with the line of code.
#After running the code, I see that the code can't run without this line, because there are other lines reffering to it, and without it there is an error.
#After deleting one always/ never rule from the system message, the Ai doesn't follow the rule anymore, and it can give wrong answers. For example, if I deleted the rule "Never teach something that is not checked and verified or not correct", the Ai could give me a wrong answer about music theory.
#After deleting response-format from the system message, the Ai doesn't follow the format anymore, and it can give me answers that are not organized or clear. For example.
#I didn't have any bugs in this lab.

