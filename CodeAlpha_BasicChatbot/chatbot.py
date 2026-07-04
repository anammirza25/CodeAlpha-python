def chatbot():
    print("=" * 40)
    print("🤖 Welcome to My Basic Chatbot")
    print("Type 'bye' to exit.")
    print("=" * 40)

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            print("Bot: Hello! Nice to meet you.")
        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")
        elif user == "what is your name":
            print("Bot: My name is CodeAlpha ChatBot.")
        elif user == "who made you":
            print("Bot: I was created by Anam using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()