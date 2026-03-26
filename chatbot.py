def chatbot():
    print("🤖 Chatbot started! (type 'exit' to stop)\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Bye bro 👋")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello bro! 👋")

        elif "how are you" in user:
            print("Bot: I'm doing great! 😊")

        elif "your name" in user:
            print("Bot: I am your AI chatbot 🤖")

        elif "help" in user:
            print("Bot: I can chat with you! Try saying hello 😄")

        elif "project" in user:
            print("Bot: I am your internship project 😎")

        else:
            print("Bot: Sorry, I don't understand 😅")

chatbot()