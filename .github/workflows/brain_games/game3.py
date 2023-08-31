import prompt
import random
import math


def find_gcd(a, b):
    return str(math.gcd(a, b))


def play_game():
    print('brain-gcd')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + "!")
    print("Find the greatest common divisor of given numbers.")

    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = find_gcd(num1, num2)

        print("Question:", num1, num2)
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print("Congratulations,", name + "!")


play_game()
