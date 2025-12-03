# importing random
import random
# creating list for words
words = ["apple","carrot","orange","cherry","tomato"]

correct_guesses = 6
# using random to choose from the list
choosen_word = random.choice(words)
print(choosen_word)

# creating an empty string called placeholder 
placeholder = ""
# getting the len of chosen_word
word_length = len(choosen_word)

# using for loop to iterate each letter from the choosen_word using range function
for position in range(word_length):
    # adding _ to placeholder
    placeholder += "_"
print(placeholder) # printing the placeholder as per the letters which are in chosen_word 
correct_letters = []  
gameOver = False # creating a gameover variable and keeping it ad False to loop the game after the user has guessed the letter

# logic of the game 
while not gameOver:
    print(f"{correct_guesses}/6 lives left")
    guessed = input("Enter the letter you gueessed: ")
    # checking if the user has already guessed the letter or not
    if  guessed in correct_letters:
        print(f"You've already guessed {guessed}, It wasn't on the word")
    display = ""
    # iterating through the chosen_word to see if the guessed letter is same as the iterable letter from the word list
    for letter in choosen_word:
        if letter == guessed:
            display += letter
            correct_letters.append(guessed)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # giving logic if the guessed letter is not in chosen word from the list
    if guessed not in choosen_word:
        correct_guesses -= 1
        print(f"You've guessed {guessed},That's not in the word.You lose a life")
        if correct_guesses == 0:
            gameOver = True
            print(f"The word was {choosen_word}. You lost the game")
    if "_" not in display:
        gameOver = True
        print("Congrats, You guessed correctly ,You WON!!!")