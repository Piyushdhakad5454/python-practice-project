def quiz_game():
    questions = {
        "What is the capital of France? ": "paris",
        "What is 5 + 7? ": "12",
        "What is the color of the sky? ": "blue"
    }
    score = 0

    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")

    print(f"\nYour score: {score}/{len(questions)}")

quiz_game()
