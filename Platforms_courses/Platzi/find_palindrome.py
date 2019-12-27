
def is_palindrome(word):
    reverse_word = ''.join(word[::-1].lower().split())
    word = ''.join(word.lower().split())
    print(word)
    print(reverse_word)
    
    if word.lower() == reverse_word.lower(): return 'is palindrome'
    return 'isn\'t palindrome'


if __name__ == '__main__':
    is_running = True
    while is_running:
        word = input('Write a word, we verify if it\'s palindrome or not: ')
        print(f'{"="*10} The word {word!r} {is_palindrome(word)} {"="*10}')
        is_running = bool(int(input('Do you want to keep trying? zero (0) to stop, one (1) to continue: ')))