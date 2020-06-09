import random

name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the guessing game!")
words = ["mumbai","delhi","laddakh","madras","newyork","kolkata","lucknow","greaternoida","chandigarh"]
# get a random word from this list
index = random.randint(0, len(words))
word = words[index]
indexes = random.sample(range(0, len(word)), 3)
guesses = "" #characters that the user has guessed so far
for i in indexes:
    guesses += word[i]
chances = 10
play = input("enter yes/no")
if play[0]=='y':
    game_on=True
else:
    game_on=False

def playagain():
    # this will help you understad scoping
    global play
    play = input("Do you want to play again? (yes/no): ")
    if play[0] == "y":
        global chances, word, guesses
        chances = 10
        index = random.randint(0, len(words))
        word = words[index]
        indexes = random.sample(range(0, len(word)), 3)
        guesses = "" 
        for i in indexes:
            guesses += word[i]

 #this play is global variable
while game_on:
    while chances > 0:
        won = True
        for ch in word:
            if ch in guesses: # the person has guessed
                print(ch, end=" ")
            else:
                print("_", end=" ")
                won = False

        if won:
            print("\nYou Won!")
            print(f"Your score is {chances * 10}")
            playagain()
            break

        # take a guess from the user
        guess = input("\nGuess a character: ")
        guesses += guess

        if guess not in word:
            chances -= 1
            print("\nWrong Answer!!")
            print(f"You have {chances} chances left!")

            if chances == 0:
                print("You Lose!!")
                playagain()
                break

print("Thanks for playing!")
