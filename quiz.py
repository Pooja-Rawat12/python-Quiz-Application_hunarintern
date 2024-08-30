questions = [
    {
        "question": "Who is the vice president of india 2024?",
        "options": ["A. bankim  Chandra Chatterjee", "B. jagdeep Dhankhar", "C. Mohammad Hamid Ansari", "D. draupati Murmur"],
        "answer": "B"
    },
    {
        "question": "Who is the Author of Panchtantra Series?",
        "options": ["A. Deepu Pradip", "B. Basil Joseph", "C. Vishnu Sharma", "D. Usha Rajesh"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer (A, B, C, D): ").strip().upper()
    return answer == question_data["answer"]

def play_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()  # Print a blank line for readability
    
    print(f"Quiz finished! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    play_quiz()
