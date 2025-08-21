import random


def hangman(word):
    wrong = 0
    stages = ["",
              "______       ",
              "|            ",
              "|      |     ",
              "|      O     ",
              "|     /|\\    ",
              "|     / \\    ",
              "|            "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print('Welcome to the gallows!')
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter letter: "
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print('You won! This word was hidden: ')
            print(" ".join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You loose! This word was hidden: {}.'.format(word))


words = ['cat', 'dog', 'bat']
hangman(random.choice(words))