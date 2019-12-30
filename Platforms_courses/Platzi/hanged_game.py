import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['lavadora', 'perro', 'gato', 'secadora', 'persona', 'petroleo', 'justicia', 'ahorcado', 'winner']

def get_random_word():
    random_index = random.randint(0, len(WORDS)-1)
    # return random.choice(WORDS) OTHER ALTERNATIVE 
    return WORDS[random_index]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print(f'{"=+=+=+=+="*10}')

def initialize_game():
    word = get_random_word()
    hidden_word = "-"*len(word)
    tries = 0
    play = True
    return [word, hidden_word, tries, play]



def verify_letter_in_word(word, letter, hidden_word):
    word = word.lower()
    letter = letter.lower()
    hidden_word  = list(hidden_word)
    its_found = False

    for index, letter_sub in enumerate(word):
        if letter_sub == letter: 
            hidden_word[index] = letter
            its_found = True

    return its_found, ''.join(hidden_word)


def game_over(word, is_winner = False):
    if is_winner: print(f'{"*-*"*10} GANASTE LA PALABRA ES: {word.upper()!r} {"*-*"*10}:')
    else: print(f'La palabra era: {word}')
    print('')
    return bool(int(input('Want play again? (0) Exit, (1) Again: ')))


def run():
    [word, hidden_word, tries, play ] = initialize_game()

    while play:
        display_board(hidden_word, tries)
        letter = input('Write a letter: ')
        its_found, hidden_word = verify_letter_in_word(letter = letter, word = word, hidden_word = hidden_word)
        if its_found:
            if word == hidden_word:
                play = game_over(word, True)
                if play: 
                    [word, hidden_word, tries, play ] = initialize_game()
        else:
            tries +=1
            if tries == len(WORDS)-1:
                play = game_over(word)
                if play: 
                    [word, hidden_word, tries, play ] = initialize_game()
            


if __name__ == '__main__':
    print(f'{"*"*10} Welcome to Hanged Game {"*"*10}')
    run()