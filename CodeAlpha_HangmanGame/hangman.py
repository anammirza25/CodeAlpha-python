import random
words = ["python", "apple", "computer", "flower", "school"]
word = random.choice(words)
guessed_letters = []
attempts = 6
print("_ " * len(word))
while True:
    guess = input("Enter a letter: ")
    if guess in word:
        if guess in guessed_letters:
            print("You already guessed this letter")
        else:
            guessed_letters.append(guess)
            print("Correct guess!")
            display = ""
            for letter in word:
                if letter in guessed_letters:
                    display = display + letter 
                else: 
                    display = display + "_ "
            print(display)
            if "_" not in display:
                print("You Win!")
                break
    else:
        print("Wrong guess!")
        attempts -= 1
        print("Remaining Attempts:", attempts)
        if attempts == 0:
            print("Game over!")
            print("The word was", word)
            break