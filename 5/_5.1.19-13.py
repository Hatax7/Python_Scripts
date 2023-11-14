def remove_all(rem,string):
    #x = ''
    result = string
    #temp = ''
    if rem not in string:
        return string
    while rem in result:
        x = result.find(rem)
        z = x + len(rem)
        #temp = result
        result = result[:x] + result[z:]#temp[:x] + temp[z:]
    return result
    
