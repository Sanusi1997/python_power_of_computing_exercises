def reverse_input(word):
    n = 1
    reversed_word = ''
    for char in word:
        reversed_word += word[len(word) - n]
        n += 1
        if n > len(word):
            print("The reverse of \"{}\" is \"{}\" ".format(word, reversed_word))
            break
reverse_input('What')


