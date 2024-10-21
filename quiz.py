# This is a quiz game
# developed by Rana Nasmin

questions = ("What is the capital city of Japan? ",
             "Which planet is known as the Red Planet? ",
             "Who wrote the play 'Romeo and Juliet'? ",
             "What is the largest ocean on Earth? ",
             "Which country is famous for the Eiffel Tower? ",
             "Which element has the chemical symbol 'O'? ",
             "Who was the first person to step on the moon? ")

options = (("A. Seoul", "B. Tokyo", "C. Beijing", "D. Bangkok"),
           ("A. Mars", "B.Jupiter", "C. Saturn", "D. Venus"),
           ("A. Charles Dickens", "B.J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"),
           ("A. Atlantic Ocean", " B.Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"),
           ("A. Spain", "B.Germany", "C. France", "D. Italy"),
           ("A. Oxygen", "B.Gold", "C. Osmium", "D. Carbon"),
           ("A. Yuri Gagarin", "B. Neil Armstrong", "C. Buzz Aldrin", "D. Michael Collins"))

answers = ("B", "A", "C", "D", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Select one(A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT ANSWER")
    else:
        print("Wrong Answer")
        print(f"{answers[question_num]} is the correct answer")


    question_num += 1

print("+++++++++++++++++++++++++++++++++++++++++++++")

print("+++++++++++++++++++++++++++++++++++++++++++++")
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score {score}")

