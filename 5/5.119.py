def my_find(haystack, needle):
    for index, letter in enumerate(haystack):
        if letter == needle:
            return index
    return -1

haystack = 'Bananarama!'
print(haystack.find('a'))
print(my_find(haystack,'a'))

def my_find2(haystack, needle, start=0):
    for index, letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return -1

import string

def remove_punctuation(phrase):
    phrase_sans_punct = ''
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct
