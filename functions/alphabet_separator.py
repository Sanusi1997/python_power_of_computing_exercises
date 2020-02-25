import string

def vowel_and_consonant_printer():
    """This function takes in user input and displays the number of vowels and consonants"""
    vowels = "aeiou"

    unwanted_char = list(string.punctuation)
    unwanted_char.remove("'")
    unwanted_char.append('\n')

    user_sentence = input("Please type your sentence: ")

    for chars in unwanted_char:
        user_sentence = user_sentence.replace(chars, "")

    number_of_consonants = 0
    number_of_vowels = 0
    for letters in user_sentence.lower():
        if letters in vowels:
            number_of_vowels += 1
        else:
            number_of_consonants += 1

    print(f"The number of vowels in your sentence is: {number_of_vowels}")
    print(f"The number of consonants in your sentence is: {number_of_consonants}")


vowel_and_consonant_printer()

