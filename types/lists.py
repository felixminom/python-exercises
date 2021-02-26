#Lists and something more

squares = [1,4,9,16]

#as strings, lists can be indexed and sliced

#result: 1
print(squares[0])

#index out of scope
try:
    squares[10]
except:
    print('index not found')


#slicing
#result: [1,4,9]
print(squares[:3])

#concatenation
squares = squares + [25, 36, 49, 64]

#lists are mutable
cubes = [1, 8, 27, 65, 125]

cubes[3] = 64

cubes.append(216)

#List can handle different types
random_list = ['a', 1, 2, ['b', 'c'], (3,4)]
