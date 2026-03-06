# Simple Python Chatbot

def chatbot():
    print("Bot: Hello! I am a simple chatbot.")
    print("Bot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I help you?")
        
        elif user_input == "how are you":
            print("Bot: I am fine! How about you?")
        
        elif user_input == "your name":
            print("Bot: I am a Python chatbot.")
        
        elif user_input == "what can you do":
            print("Bot: I can chat with you and answer simple questions.")
        
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
