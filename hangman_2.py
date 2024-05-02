import random

stages =['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
''',  '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========== 
''',  '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========== 
''',  '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========== 
''',  '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========== 
''',  '''
    +---+
    |   |
    O   |
        |
        |
        |
=========== 
''',  '''
    +---+
    |   |
        |
        |
        |
        |
=========== 
''']

word_list = ["ardvark", "baboon", "camel" ]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(f"Psst, the solution is {chosen_word}.")

display =[]
# for _ in range(len(chosen_word)):
for _ in range(word_length):
    display += "_"
# print(display)

while not end_of_game:
    guess = input("Guess a letter: ? ").lower()
    
    for position in range(word_length):
        # print(f"Position : {position}")
        letter = chosen_word[position]
        # print(f"Letter : {letter}")
        # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {guess}")
            # print(f"Display : {display}") 
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"Lives is : {lives}")
            end_of_game = True
            print(stages[lives])
            print("You lose.")
            break
    print(f"Lives is : {lives}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(stages[lives])  