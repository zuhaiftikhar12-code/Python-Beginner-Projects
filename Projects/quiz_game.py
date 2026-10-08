questions = (
    ("What is the capital of France?"),
    ("Which planet is known as the Red Planet?"),
    ("What is 8 × 7?"),
    ("Which language is used in this quiz?"),
    ("How many continents are there?"),
)
options = (
    ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. 54", "B. 56", "C. 64", "D. 58"),
    ("A. Java", "B. C++", "C. Python", "D. JavaScript"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
)

guesses = []
question_no = 0
answers =("C", "B", "B", "C", "C")
score = 0
for question in questions:
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter(A,B,C,D)").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        score += 1
        print("Correct👏👏")
    else:
        print("Incorrect😞😞")
        print(f"{answers[question_no]} is the correct answer")
    question_no += 1
    print("---------------------------")

result = score / len(questions) * 100
print(f"total score: {result}")
print("---------------------------")

print(f"Answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("---------------------------")
print(f"Guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("---------------------------")
