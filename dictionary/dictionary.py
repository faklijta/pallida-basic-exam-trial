dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]
# Implement this method. It should add the given key-value pair to the
# list 'dictionary'
def add_word(hun_word, eng_word):
    dictionary.update({'hun_word':'eng_word'})

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'

def translate_to_hun(eng_word):
    for key, value in dictionary.items():
        print(value + "in english is" + key)


def translate_to_eng(hun_word):
    for key, value in dictionary.items():
        print(key + "in hungarian is" + value)

