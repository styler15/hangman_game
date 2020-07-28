# Write your code here
import random

#randomize
word_choices =[ 'python', 'java', 'kotlin', 'javascript']
shuffled_word = random.choice(word_choices)

# Game setup
dashes = '-'*(len(shuffled_word))
word = list('-'*(len(shuffled_word)))
h = 0
guessed_list = []
print("H A N G M A N\n")
while input('Type "play" to play the game, "exit" to quit:') != "play":
    continue


while h < 8:
    print()
    print(dashes)
    guess = input('Input a letter: ')
    #guessing multiple letters/uppercase/previously guessed
    if len(guess) != 1:
        print('You should input a single letter')
    elif not guess.islower():
        print('It is not an ASCII lowercase letter')
    elif guess in dashes or guess in guessed_list:
        print('You already typed this letter')
    elif guess in shuffled_word:
        for i in range(len(shuffled_word)):
            if guess == shuffled_word[i]:
                word[i] = guess
                dashes = ''.join(word)
                h += 0
    #letter not in word
    else:
        h += 1
        print('No such letter in the word')
        guessed_list.append(guess)

#Final result after guessing
if '-' not in dashes:
    print('You guessed the word!')
    print('You survived!\n')
else:
    print('You are hanged!\n')
