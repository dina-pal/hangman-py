
import random

print()

words = [
    "Hello", "world", "Earth", "fortune", "test", "this", 'is'
]

# TODO: Choice a work from the wordlist and store in a variable call choice_word

choice_word = random.choice(words)

print(choice_word)

# TODO: Generate blank space as in choice_word

display = []

for letter in choice_word:
    display += "_"
print(display)


guess = input("Enter a letter: ").lower()

# Check if the letter exist or not

for letter in choice_word:
    if (letter == guess):
        print("right")
    else:
        print("Wrong!")
