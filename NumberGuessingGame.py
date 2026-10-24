from random import randint
from sys import exit

def choose_difficulty():
    print("Type the number of the difficulty you want to play.")
    print("1) Easy")
    print("2) Medium")
    print("3) Difficult")
    difficulty = input()
    if "0" < difficulty <= "3":
        return difficulty
    else:
        print("Invalid difficulty")
        return choose_difficulty()
    
def play_again(difficulty):
    print("Do you want to keep playing:")
    print("1) Yes")
    print("2) Yes, but on a drifferent difficulty")
    print("3) No")
    play_again = input()
    if "0" < play_again <= "3":
        if play_again == "1":
            play(difficulty)
        elif play_again == "2":
            play(choose_difficulty())
        else:
            print("Thanks for playing!")
            exit()
    else:
        print("Invalid choice")
        play_again()


def play(difficulty):
    number_found = False
    if difficulty == "1":
        number = randint(1, 10)
    elif difficulty == "2":
        number = randint(1, 100)
    elif difficulty == "3":
        number = randint(1, 1000)
    
    while True:
        guess = int(input("Guess a number: "))
        if guess == number:
            print(f"Congrats, you guessed {number} correctly")
            break
        elif guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
    play_again(difficulty)

        

playing = True
print("Welcome to my number guessing game!")
difficulty = choose_difficulty()

while playing:
    play(difficulty)
    