import random

words = ["python", "computer", "science", "internship", "programming"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts Left:", attempts)

    letter = input("Enter a letter: ").lower()

    if letter in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)