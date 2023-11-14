def find(word, letter, startat):
    index = startat
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count_letter(string,letter):
    startat = 0
    count = 0
    while True:#startat < len(string):
        new_index = find(string,letter,startat)
        if new_index == -1:
            return count
        count += 1
        startat = new_index + 1
    #return count

print(count_letter('banana',' '))
