import prompt
import random


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game():
    print('brain-prime')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + "!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_prime(number) else "no"

        print("Question:", number)
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
