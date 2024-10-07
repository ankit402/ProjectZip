import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS= 5
logo =''' ___ _ _ ___ ___ ___   | |_| |_ ___    ___ _ _ _____| |_ ___ ___ 
| . | | | -_|_ -|_ -|  |  _|   | -_|  |   | | |     | . | -_|  _|
|_  |___|___|___|___|  |_| |_|_|___|  |_|_|___|_|_|_|___|___|_|  
|___|  '''
print(logo)
def check_answer(guessed_number,answer,attempts):
    guessed_number = int(guessed_number)
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"Your answer is right... the answer was {answer} ")

def set_difficulty(level_chosen):
    if level_chosen =='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def game():
    print('let me think the number between 1 to  50')
    answer = random.randint(1,50)
    print(answer)
    level = input("Choose level of difficulty....Type 'easy' or 'hard':").lower()

    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("You are entered wrong data for play game try again")
        return
    guessed_number=0
    while guessed_number != answer:
        print(f"You have {attempts} remaining to guess the numbers")
        guessed_number=input("Guess the number:")
        attempts= check_answer(guessed_number, answer, attempts )
        if attempts==0:
            print("You are out of guesses.... You lose!")
            return
        elif guessed_number != answer:
            print("Guess again")
        else:
            print("game over ")
game()