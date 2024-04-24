import random
from hangman_words import word
random_word = random.choice(word)
#print(random_word)
ranges = len(random_word) 
from hangman_art import logo
print(logo)
lives=7
#Create blanks
empty = []
for _ in range(ranges):
    empty += "_"
print(empty) 
end_of_game=False

while not end_of_game:
  Guess_letter = input("\nGuess a letter:").lower()
  if Guess_letter in empty:
    print(f"You have already guessed {Guess_letter}")
    #Check guessed letter
  for position in range(ranges):
        check = random_word[position]
        if Guess_letter in check:
            empty[position] = Guess_letter
            print(empty)
    #Check if user is wrong.
  if Guess_letter not in random_word: 
        print(f"You guessed {Guess_letter} that's not in the word.You lose a life. ")
        lives -=1
        if lives==0:
          end_of_game=True
          print("You lose")
        from hangman_art import stages
        print(stages[lives])
    #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(empty)}")

    #Check if user has got all letters.
  if "_" not in empty:
     end_of_game=True
     print("You win")