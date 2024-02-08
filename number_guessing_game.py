import random

play_again = 1

while play_again == 1:
    num = random.randint(1, 100)

    guess = 0
    user = 0
    bottom = 1
    top = 100

    while user != num:
        guess = guess + 1
        print("Guess a number between", bottom, "and", top)
        user = input()
        user = int(user)

        if user > num:
            print("Too high")
            top = user
        elif user < num:
            print("Too low")
            bottom = user
        else:
            print("You got it!")
            print("You guessed", guess, "times")
    
    play_again = input("Do you want to play again? Type 1 for yes and 2 for no: ")
    play_again = int(play_again)
            
    if play_again == 2:
        print("Goodbye.")
        break
    else:
        continue