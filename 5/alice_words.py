_words = open('alice.txt',encoding='utf8').read()#.split()
words = ''
symbols = ''',."?”!:;()_/'''

#eliminates unwanted sysmbols
for letter in _words:
    if letter not in symbols:
        words += letter

words = words.split()

d_words = {}

#creates fills a dictionary with word's and their count
for word in words:
    if word.lower() >= 'a' and word.lower() <= 'z' :
       d_words[word.lower()] = d_words.get(word.lower(),0) + 1

l_words = list(d_words.items())

l_words.sort()

string = '{0:<20}{1}\n=========================\n'.format('Word','Count')
for word,number in l_words:
    string +='{0:<20}{1}\n'.format(word,number)

new_words = open('new_alice.txt','x')
new_words.write(string)


