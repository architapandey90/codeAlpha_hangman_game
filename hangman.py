import random

def hangman():
    #predefined small list of words
    words=["apple","banana","grape","orange","peach"]

    #randomly choose one word
    word=random.choice(words)
    guessed_word=["_"]*len(word)

    attempts_left=6
    guessed_letters=[]

    print(" 🤺 Welcome to Hangman!")
    print("you have 6 incorrect guesses. let's begin!\n")

    #game loop
    while attempts_left>0 and "_" in guessed_word:
        print("word:","  ".join(guessed_word))
        print(f"guessed letters:{','.join(guessed_letters)}")
        print(f"attempts left:{attempts_left}")

        guess=input("guess a letter:").lower()

        if len(guess)!=1 or not guess.isalpha():
            print("⚠️please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️you already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("correct guess!\n")
            for i ,letter in enumerate(word):
                if letter==guess:
                    guessed_word[i]=guess

        else:
            print("wrong guess!\n")
            attempts_left-=1

    #game results
    if"_"not in guessed_word:
        print("🎉congratulations!you guessed the words",word)
    else:
        print("💀out of attempts!the word was",word)


#run the game
hangman()

