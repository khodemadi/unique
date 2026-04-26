import random


#تعریف تابع wlecome

def welcome():
    print("welcome to this funny game")
    print("I will guess a number between 1 100 and")
    print("you have to guess it...")
    print("go go go go")
    print()

#تعریف تابع finish

def finish(number, count):
    print("good game")
    print(f"my numbers was {number} and you found it in {count}")
    print()
    answer = input("do you want to play again (Y/N) ")
    if answer.upper() == 'Y':
        return True
    else:
        return False

#تعریف تابع win

def win(computer_namber, guess):
    return computer_namber == guess

#تعریف تابع answer

def answer(computer, user):
    if computer > user:
        return "my numbar is larger"
    if computer < user:
        return "oh.. you went so large! mine is smaller"

    return "wow you won! good guess!"

#تعریف تابع get_a_guess

def get_a_guess():
    ans = input("what is your guess? ")
    return int(ans)


#از اینجا به بعد از تابع ها در کد استفاده میکنم استفاده میکنیم

welcome()
continue_playing = True
while (continue_playing):
    # computer numbre between 1 to 100
    computer_namber = random.randint(1, 100)

    # start with a wrong guess
    guess = 0

    count = 0

    while (not win(computer_namber, guess)):
        guess = get_a_guess()
        count += 1
        print(answer(computer_namber, guess))

    continue_playing = finish(computer_namber, count)
    
