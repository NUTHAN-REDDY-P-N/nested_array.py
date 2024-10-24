
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


