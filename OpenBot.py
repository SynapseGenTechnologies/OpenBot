import time
print("Initiating")
time.sleep(3.5)
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Define AI chatbot function using GPT-3.5-turbo
def chat():
    print("OpenBot: Hello, I'm OpenBot, an AI chatbot developed by InsightAI. How may I help you?")
    
    # Initialize conversation history as an empty list
    conversation_history = []
    
    # Define fallback message for unknown questions
    fallback_response = "I'm still learning. Is there anything else I can help you with?"
    
    while True:
        user_input = input("User: ")
        if 'bye' in user_input:
            print("OpenBot: Goodbye!")
            break
        else:
            # Append user input to conversation history
            conversation_history.append("User: " + user_input)
            
            # Pass the conversation history to the OpenAI API
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt="\n".join(conversation_history),
                max_tokens=3240,
                n=1,
                stop=None,
                temperature=0.2
            )
            
            bot_response = response.choices[0].text.strip()
            
            # Append AI response to conversation history
            conversation_history.append("OpenBot: " + bot_response)
            
            print("OpenBot:", bot_response)
            
            # Remove user input from the conversation history (optional)
            conversation_history = conversation_history[:-2]

# Function to check if the user input matches unknown question patterns
def is_unknown_question(user_input):
    # Add your logic here to identify unknown question patterns
    # Return True if it matches, False otherwise
    return False

# Start the AI chatbot
chat()
