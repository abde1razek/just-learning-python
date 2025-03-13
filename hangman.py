import random

# Greetings
print("Welcome to Hangman!")

# Word list
wordlist = ["hacker", "bounty", "random", "red", "hat", "love"]

# Start a new game
def newgame():
    global secretword, WordCounter, hearts
    secretword = random.choice(wordlist)
    WordCounter = ["_"] * len(secretword)
    hearts = 5
    print(WordCounter)
    print("You have 5 hearts.")

# Start the game
game_over = False
newgame()

while not game_over:
    guess = input("Guess a letter? ").lower()
    if guess in secretword:
        for position in range(len(secretword)):
            if secretword[position] == guess:
                WordCounter[position] = guess
        print(WordCounter)
    else:
        hearts -= 1
        print(f"You have {hearts} ♥ left")
        if hearts == 0:
            print("You have lost :(")
            print("Y: New game\nN: End game\nH: Reset heart counter to 5")
            try_again = input("Try Again? (Y/N/H) ").upper()
            if try_again == "Y":
                newgame()
            elif try_again == "H":
                hearts = 5
                print(f"You have {hearts} ♥ left")
                print(WordCounter)
            elif try_again == "N":
                print("See you soon")
                game_over = True
            else:
                print("Try Again? (Y/N/H)")

    if "_" not in WordCounter:
        print("You Win!")
        try_again = input("Play Again? (Y/N) ").upper()
        if try_again == "Y":
            newgame()
        else:
            print("See you soon")
            game_over = True
