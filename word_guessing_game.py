import random as r
name = (input('What is yor name?'))
print("Good luck!", name)

words = ('rainbow', 'king','queen', 'love' , 'hate', 'grief')
print("\nGuess a word from the below list:\n",words,)
word=r.choice(words)

guesses = ''
turns = 12

while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_",end=" ")
        failed += 1
    if failed == 0:
        print("\nCongratulations!! You got it right.\n")
        print("The word is", word)
        break

    print()
    guess = input("Please guess a letter:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("You are wrong")
        print("You have", turns,"chances left.")
        if turns==0:
            print("You loose.")