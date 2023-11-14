def cross_product(vec1,vec2):
    ''' returns the cross product of 2 vectors of length 3 '''
    result = []
    result.append(vec1[1]*vec2[2]-vec1[2]*vec2[1])
    result.append(vec1[2]*vec2[0]-vec1[0]*vec2[2])
    result.append(vec1[0]*vec2[1]-vec1[1]*vec2[0])
    return result
print(cross_product([2,3,4],[5,6,7]) == [-3,6,-3])
