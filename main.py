import random

def process_guess(the_answer, the_guess):
  position = 0
  clue = ""
  for letter in the_guess:
    if letter == the_answer[position]:
      clue += "G"
    elif letter in the_answer:
      clue += "Y"
    else:
      clue += "-"
    position += 1
  print(clue)
  return clue == "GGGGG" 

word_list = []
word_file = open("wordle.txt")

for word in word_file:
  word_list.append(word.strip())

answer = random.choice(word_list)

number_of_guesses = 0
guessed_correctly = False

while number_of_guesses < 6 and not guessed_correctly:
  guess = input("Input a 5 letter word and press enter:")
  print("You have guessed", guess)
  number_of_guesses += 1
  
  guessed_correctly = process_guess(answer, guess)

if guessed_correctly:
  print("Congratulations! You guessed the word in ", number_of_guesses, "times.")
else:
  print("You have used up all of your guesses, the correct word was", answer)