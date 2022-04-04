import random
import hangman_art
import hangman_words

end_of_game = False
#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#Set 'lives' to equal 6.
lives = 6
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(word_length):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if lives == 0:
        print("You Lose.")
        print(f"The word was {chosen_word}")
        break

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])