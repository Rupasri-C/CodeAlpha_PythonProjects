def chatbot():
    print("=" * 40)
    print("      WELCOME TO MY CHATBOT")
    print("=" * 40)
    print("Type 'exit' to end the chat.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great! How about you?")

        elif user == "i am fine" or user == "fine":
            print("Bot: That's great to hear!")

        elif user == "what is your name":
            print("Bot: My name is CodeBot.")

        elif user == "who created you":
            print("Bot: I was created by Rupasri as a CodeAlpha internship project.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions and chat with you.")

        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")

        elif user == "bye" or user == "exit":
            print("Bot: Goodbye! Have a wonderful day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

chatbot()