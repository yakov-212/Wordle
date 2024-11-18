import os

clear = lambda: os.system("cls")

def greetings():
    print("Welcome to Wordle im sure you already know the rules but to just a quick recap\n"
    "Someone picks a five letter word and then you guess what the word is\n"
    "In this version if the letters in the right spot a G will appear if its in the wrong spot youll get a Y\n"
    "you have six trys Good Luck")

def dots():
    print("****"*20)

def prompt(prompt):
    while True:
        word = input(f"{prompt} a five letter word: ")
        if len(word) == 5:
            break
        print("only enter five letter words")
    return list(word)

def main():
    correct = ["X"]*5
    double = []
    round = 1
    clear()
    greetings()
    word = prompt("Enter")
    clear()
    while round <=6:
        guess = prompt("Guess")
        for i in range(5):
            if word[i] == guess[i]:
                correct = correct[0:i]+["G"]+correct[i+1:]
                double.append(guess[i])
            elif guess[i] in word:
                if word.count(guess[i]) >= guess.count(guess[i]):
                    correct = correct[0:i]+["Y"]+correct[i+1:]
                else:
                    if guess[i] not in double:
                        correct = correct[0:i]+["Y"]+correct[i+1:]
                        double.append(guess[i])
        print(guess)
        print(correct)
        dots()

        if correct == ["G"]*5:
            print("You win!!")
            print(f"Your score: {round}")
            break
        correct = ["X"]*5
        double = []
        round += 1

if __name__ == "__main__":
    main()
