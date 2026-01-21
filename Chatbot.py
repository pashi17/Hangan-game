def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that."


print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    reply = chatbot_reply(user_message)
    print("ChatBot:", reply)

    if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
        break
