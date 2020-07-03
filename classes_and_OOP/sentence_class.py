import string


class Sentence(object):
    def __init__(self, input_sentence=""):
        self.input_str = input_sentence

    def get_first_word(self):
        a = string.punctuation
        if a in self.input_str:
            for values in self.input_str:
                if values in a:
                    sentence_w = self.input_str.replace(values, "")
                    sentence_list = sentence_w.split()
                    return (sentence_list[0])
        else:
            return self.input_str.split()[0]

    def get_all_word(self):
        return self.input_str

    def replace(self, number, new_word):
        sentence_list = self.input_str.split()
        sentence_list.remove(sentence_list[number])
        sentence_list.insert(number, new_word)
        return " ".join(sentence_list)

    def __str__(self):
        return f"{self.input_str}"


word = Sentence("hello dear lady of the federation")
print(word.get_first_word())
print(word.replace(2, "President"))
