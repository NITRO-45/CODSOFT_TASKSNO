print("College Assistant Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! How can I help you?")

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a Rule-Based College Assistant Chatbot.")

    # College timings
    elif "timing" in user_input or "college time" in user_input:
        print("Bot: College timings are from 9:00 AM to 4:00 PM.")

    # Library
    elif "library" in user_input:
        print("Bot: The library is open from 9:00 AM to 6:00 PM.")

    # Courses
    elif "course" in user_input or "courses" in user_input:
        print("Bot: Our college offers BSc AI, BSc CS, BCA and other courses.")

    # Exam
    elif "exam" in user_input or "examination" in user_input:
        print("Bot: Please check the college notice board for the latest exam timetable.")

    # Fees
    elif "fee" in user_input or "fees" in user_input:
        print("Bot: Please contact the college office for detailed fee information.")

    # Help
    elif "help" in user_input:
        print("Bot: I can help you with timings, courses, library, exams and fees.")

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    # Unknown question
    else:
        print("Bot: Sorry, I don't understand that question.")