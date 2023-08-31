import prompt# ипартируем модули
import random

print('brain-games')# выводим приветсвия
print('Welcome to the Brain Games!')


def is_even(number):# создаем функцию которая выполняет проверку на четность
    return number % 2 == 0


def play_game():
    name = prompt.string('May I have your name? ')#запрашиваем имя
    print('Hello!', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print('Question', number)
        user_answer = input('Your answer: ')

        if (is_even(number) and user_answer == "yes") or (not is_even(number) and user_answer == "no"):# смотрим что вводит user
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = "yes" if is_even(number) else "no"
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again, " + name + "!")
            return

    print("Congratulations, " + name + "!")
    play_game()


play_game()# вызываем функцию
