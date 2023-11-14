_file = open('alice.txt',encoding='utf8').read()

symbols = ''',."?”!:;()_'''
file = ''

for letter in _file:
    if letter not in symbols:
        file += letter

l_file = file.split()

longest_word = ''
length = 0
for word in l_file:
    if len(word) > length:
        length = len(word)
        longest_word = word
print("The longest word is '"+longest_word+"' and it's length is: " + str(length))
