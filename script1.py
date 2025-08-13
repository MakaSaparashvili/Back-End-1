import random

print("Welcome to the Simple Multiplication Quiz!")
print("You will be given 5 random multiplication problems to solve.\n")

score = 0
num_questions = 5

for i in range(1, num_questions + 1):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    correct_answer = a * b

    print(f"Problem {i}: What is {a} x {b}?")
    try:
        answer = int(input("Your answer: "))
        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.\n")
    except ValueError:
        print(f"Invalid input. The correct answer was {correct_answer}.\n")

print(f"You scored {score} out of {num_questions}. Well done!")
