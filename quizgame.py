import random

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Mars", "C. Venus", "D. Mercury"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    }
]

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

def play_quiz(quiz_questions):
    score = 0
    for question_data in quiz_questions:
        display_question(question_data)
        user_answer = input("Enter your answer (A, B, C, or D): ")
        if user_answer.upper() == question_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question_data["answer"])
    return score

def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")
    random.shuffle(quiz_questions)
    score = play_quiz(quiz_questions)
    print("Quiz completed! Your final score is:", score)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
