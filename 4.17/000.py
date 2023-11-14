def double_stuff(values):
    new_list = []
    for value in values:
        new_elm = 2 * value
        new_list.append(new_elm)

    return new_list
v = [23, 55, 13]
print(double_stuff(v))

print(enumerate(v))
