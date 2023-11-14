def dot_product(vec1,vec2):
    '''returns the sum of products of the corresponding elements of each list'''
    #result = []
    result = 0
    for i in range(len(vec1)):
        #result.append(vec1[i]*vec2[i])
        result += vec1[i] * vec2[i]
    return result#sum(result)
print(dot_product([1,1],[1,1]) == 2)
print(dot_product([1,2],[1,4]) == 9)
print(dot_product([1,2,1],[1,4,3]) == 12)
print()

def dot_product2(vec1,vec2):
    '''returns the sum of products of the corresponding elements of each list'''
    #result = []
    result = 0
    for i,x in enumerate(vec1):
        #result.append(x*vec2[i])
        result += x * vec2[i]
    return result#sum(result)
print(dot_product2([1,1],[1,1]) == 2)
print(dot_product2([1,2],[1,4]) == 9)
print(dot_product2([1,2,1],[1,4,3]) == 12)
print()

#def dot_product3(vec1.vec2):
   # result = []
   # for x1 in vec1:
        
