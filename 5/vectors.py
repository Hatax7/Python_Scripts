def add_vectors(vector1,vector2):
    result = []
    for index,value in enumerate(vector1):
        result.append(value + vector2[index])
    return result
print(add_vectors([1,1],[1,1]) == [2,2])
print(add_vectors([1,2],[1,4]) == [2,6])
print(add_vectors([1,2,1],[1,4,3]) == [2,6,4])

def add_vectors2(vector1,vector2):
    result=[]
    for i in range(len(vector1)):
        result.append(vector1[i] + vector2[i])
    return result
print(add_vectors2([1,1],[1,1]) == [2,2])
print(add_vectors2([1,2],[1,4]) == [2,6])
print(add_vectors2([1,2,1],[1,4,3]) == [2,6,4])
