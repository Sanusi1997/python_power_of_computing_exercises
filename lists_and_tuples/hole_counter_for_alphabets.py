import string


def topological_letter_counter(word_list):
    topological_letters = 'abdgeopABDGOP'
    alphabets = string.ascii_lowercase + string.ascii_uppercase
    letter_with_holes = 0
    letter_without_holes = 0
    for letters in alphabets:
        if letters in topological_letters:
            alphabets = alphabets.replace(letters, '')

    count = 0
    while  len(word_list) > count:
        for letter in word_list[count]:
            if letter in topological_letters:
                letter_with_holes += 1
                print(letter_with_holes)
                if letter_with_holes > 2:
                    print(word_list[count])
            elif letter in alphabets:
                letter_without_holes += 1
        count+=1


word_list = ['hameed', 'dog', 'misst','meagre', 'mood', 'alaxity']
topological_letter_counter(word_list)

"""def letter_with_holes_in_list(sentence):
    topological_letters = 'abdgeopABDGOP'
    alphabets = string.ascii_lowercase + string.ascii_uppercase
    letter_with_holes = 0
    letter_without_holes = 0
    for letters in alphabets:
        if letters in topological_letters :
            alphabets = alphabets.replace(letters,'')
    for letter in sentence:
        if letter in topological_letters:
            letter_with_holes += 1
        elif letter in alphabets:
            letter_without_holes += 1
    print(f"Number of letters with hole is {letter_with_holes}")
    print(f"Number of letters without hole is {letter_without_holes}")

sentence = "My name is hamEed"
topological_letter_counter(sentence)"""
