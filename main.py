import random
from hangman_step import logo, steps, tagline
from hangman_words import words
# Logo
print(logo)
print(tagline)


# pick any word of the list
choice_word = random.choice(words)


# Generate Blank Space as the length of choice_word
display = []

for letter in range(len(choice_word)):
    display.append("_")

# Display the blank space
print(" ".join(display))


# Number of lives remain
lives = len(choice_word)


# while end_of_game is not true give user to choose word
end_of_game = False
while not end_of_game:
    # Ask user to guess the letter
    guess = input("Enter the word! ").lower()

    #  if guess word are in choice_word lets add the letter on blank space
    for position in range(len(choice_word)):
        letter = choice_word[position]
        if (letter == guess):
            display[position] = letter
    print(f"{' '.join(display)}")

    # check if the word are already exist or not

    # Check if guess word are not in choice_word
    if (guess not in choice_word):
        lives -= 1
        print(steps[lives - 1])
    # if user have no lives remain over the game and make user lose
    if lives == 0:
        end_of_game = True
        print('You lose this time. try again')

    # if all blank are filled. win the user
    if "_" not in display:
        end_of_game = True
        print('🤷‍♀️ Congratulations! You Win')
