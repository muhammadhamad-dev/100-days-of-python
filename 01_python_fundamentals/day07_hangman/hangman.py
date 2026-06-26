import random
import hangman_words
import hangman_art

lives = 6
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Build initial placeholder display
display = ["_"] * word_length
print("Word to guess: " + " ".join(display))

game_over = False
guessed_letters = []

while not game_over:
    print(f"\n**********  {lives}/6 LIVES LEFT  **********")
    guess = input("Guess a letter: ").lower()

    # Warn if letter already guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
    else:
        guessed_letters.append(guess)

    # Update display with correct guesses
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    print("Word to guess: " + " ".join(display))

    # Handle wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\n**** YOU LOSE! The word was '{chosen_word}' ****")

    # Check win condition
    if "_" not in display:
        game_over = True
        print("\n**** YOU WIN! ****")

    print(hangman_art.stages[lives])