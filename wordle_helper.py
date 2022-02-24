file = open("wordlist.txt", "r") 
words = file.read().split()
file.close()

word_so_far = ['' for _ in range(5)]
good_letters = set()
bad_letters_by_pos = [set() for _ in range(5)]
bad_letters = set()

def is_word_good(word):
    for i, letter in enumerate(word):
        if letter in bad_letters:
            return False
        elif letter in bad_letters_by_pos[i] and (letter not in (word[:i] + word[i+1:])):
            return False
        elif word_so_far[i] and letter != word_so_far[i]:
            return False
    for letter in good_letters:
        if letter not in word:
            return False
    return True


while True:
    print('enter guess')
    guess = input()
    print('enter result')
    result = input()

    for letter, res, i in zip(guess, result, list(range(5))):
        if res == 'g':
            word_so_far[i] = letter
            good_letters.add(letter)
        elif res == 'y':
            good_letters.add(letter)
            bad_letters_by_pos[i].add(letter)

    for letter, res, i in zip(guess, result, list(range(5))):
        if res == 'b':
            if letter in good_letters:
                bad_letters_by_pos[i].add(letter)
            else:
                bad_letters.add(letter)
    words = list(filter(is_word_good, words))
    print(words)
    print()
