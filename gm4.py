import random
from time import sleep

words=('apple','banana','dates','imli','diya')

HANGMAN=(
    
"""
|--------|
|        0
|
|
|
|
|

""",
    
"""
|--------|
|        0
|        |
|       -+-
|
|
|

""",
    
"""
|--------|
|        0
|      /-+-
|   
|
|
|

""",
    
"""
|--------|
|        0
|      /-+-\
|        |
|
|
|

""",
    
"""
|--------|
|        0
|      /-+-\
|        |
|        |
|      |
|      |

""",
    
"""
|--------|  
|        0
|      /-+-\
|        |
|        |
|      |   |
|      |   |
|
|

""")

word=random.choice(words)
MAX=len(HANGMAN)-1
spaces=("-")*len(word)
positivesaying=('Dips','Bhau','Maau')
used=[]
wrong=0

print(" Hello....WELCOME")
print()
input(" Press ENTER to start ")

while wrong < MAX and spaces!=word:
    print()
    print(HANGMAN[wrong])
    print(" Spaces ",spaces)
    print(" Used ", used)

    guess=input(" Guess a letter ").lower
    sleep(1)
    print()

    while guess in used:
        print("Hey... U already guessed this letter ")
        guess=input(" Guess a letter ").lower
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(positivesaying)," Updating ")

        new= ""
        for i in range(len(word)):
            if guess==word(i):
                new+=guess

            else:
                new +=spaces[i]
        spaces = new

    else:
        print("INCORRECT! Try again!")
        wrong += 1

print("Calculating result...")
sleep(1)
if wrong == MAX:
    print("UNLUCKY! Better luck next time!")

else:
    print("WINNER! Congratulations!")

print()
print()
input("Press Enter to Leave: ")

