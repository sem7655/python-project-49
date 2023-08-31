import prompt
import random


def generate_progression():
    start = random.randint(1, 20)
    diff = random.randint(1, 5)
    progression = [str(start + i * diff) for i in range(10)]
    hidden_index = random.randint(0, 9)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = ".."
    return " ".join(progression), hidden_number


def play_game():
    print('brain-progression')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + "!")
    print("What number is missing in the progression?")

    correct_answers_count = 0
    while correct_answers_count < 3:
        progression, hidden_number = generate_progression()

        print("Question:", progression)
        user_answer = prompt.string("Your answer: ")

        if user_answer == hidden_number:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            return

    print("Congratulations,", name + "!")


play_game()
