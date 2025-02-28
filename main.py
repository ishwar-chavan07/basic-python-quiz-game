print("Welcome to the computer quiz!")

playing = input("Do you want to play the game? (yes/no) ")
if playing.lower() != "yes":
    quit()

print("Okay, let's play!")

# List of questions and answers
questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply unit",
    "What does ROM stand for? ": "read only memory",
    "What does HDD stand for? ": "hard disk drive"
}

score = 0  # Initialize score

# Loop through the questions
for question, correct_answer in questions.items():
    answer = input(question)
    if answer.lower() == correct_answer:
        print("Correct!")
        score += 1  # Increment score for correct answer
    else:
        print("Incorrect. The correct answer is:", correct_answer)

# Display the final score
print(f"Your final score is: {score}/{len(questions)}")
print("Thanks for playing!")