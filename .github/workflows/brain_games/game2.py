import prompt
import random 

def calculate(expression):
    return str(eval(expression))


def play_game():
    print('brain-calc')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + "!")
    print("What is the result of the expression?")

    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        expression = f"{num1} {operator} {num2}"
        correct_answer = calculate(expression)

        print("Question:", expression)
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
