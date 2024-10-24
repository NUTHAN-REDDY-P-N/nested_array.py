A code written with python which takes in a nested array and gives out the flatten array


result = []
def flattenarray(nestedarray):
    for item in nestedarray:
        if type(item) == list:
            flattenarray(item)
        else:
            result.append(item)
nestedarray= eval(input(('enter the nested array')))
flattenarray(nestedarray)
print(f'The nested array is {result}')
