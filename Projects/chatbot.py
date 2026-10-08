def chatbot(message):
    message = message.lower()

    if message == "hello" or message == "hi" or message == "hey":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif (
        message == "what is your name"
        or message == "your name"
        or message == "what's your name"
    ):
        return "My name is ChatBot."

    elif message == "who made you":
        return "I was created using Python."

    elif message == "what can you do":
        return "I can answer simple questions."

    elif message == "thank you" or message == "thanks":
        return "You're welcome!"

    elif message == "good morning":
        return "Good morning! Have a nice day."

    elif message == "good night":
        return "Good night! Sweet dreams."

    elif message == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand."


print("=" * 30)
print("      BASIC CHATBOT")
print("=" * 30)
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    print("Bot:", chatbot(user))

    if user.lower() == "bye":
        break
