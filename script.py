print("Welcome to the Simple Multiplication Quiz!")
print("You will be given 5 multiplication problems to solve.\n")

score = 0

# Problem 1
print("Problem 1: What is 3 x 4?")
answer = int(input("Your answer: "))
if answer == 12:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was 12.\n")

# Problem 2
print("Problem 2: What is 5 x 6?")
answer = int(input("Your answer: "))
if answer == 30:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was 30.\n")

# Problem 3
print("Problem 3: What is 2 x 7?")
answer = int(input("Your answer: "))
if answer == 14:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was 14.\n")

# Problem 4
print("Problem 4: What is 9 x 3?")
answer = int(input("Your answer: "))
if answer == 27:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was 27.\n")

# Problem 5
print("Problem 5: What is 4 x 8?")
answer = int(input("Your answer: "))
if answer == 32:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer was 32.\n")

# Final score
print(f"You scored {score} out of 5. Well done!")
