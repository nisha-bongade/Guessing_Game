import random 

def play_game():
    comp_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess the computer num: "))

        if user_num == comp_num:
            print("CONGRATULATIONS! You won. Game Over!!")
            break
        elif user_num < comp_num:
            print("Too Low")
        else: 
            print("Too High")

    print("Thank you for playing.")

play_game()
