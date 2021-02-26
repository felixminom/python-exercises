#About flow control

#if statement
#result:
#   less than zero

x = -12

if x < 0:
    print('less than zero')
elif x == 0:
    print('zero')
else:
    print('greater than zero')

#Surprisingly python does not have switch stataments
# you can simulate one

#The for loop

numbers = [1,2,3,4,5]

for number in numbers:
    print(number*2)

#From the official documentation:
#   "Code that modifies a collection while iterating over that same collection
#   can be tricky to get right. Instead, it is usually more straight-forward
#   to loop over a copy of the collection or to create a new collection."
#as we see oficial doc recommends inmutability :)


#Iterate#From the official documentation:
#   "Code that modifies a collection while iterating over that same collection
#   can be tricky to get right. Instead, it is usually more straight-forward
#   to loop over a copy of the collection or to create a new collection."
#as we see oficial doc recommends inmutability :)

users = [(0, 'inactive'), (1, 'active')]

# Strategy:  Iterate over a copy
# Result: [(1,'active)]
for user, status in users.copy():
    if status == 'inactive':
        del users[user]
print(users)

# Strategy:  Create a new collection
#result: {1: 'active'}
active_users = {}
for user, status in users:
    if status == 'active':
        active_users[user] = status

print(active_users)


#THE RANGE FUNCTION

#result: 0,1,2,3,4
#the given point is not part of the generated sequence
for i in range(5):
    print(i, end=', ')

#Actually this is a bad approach, but you can do like this
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#result: range(0,10)
# In many ways the object returned by range() behaves as if it is a list,
# but in fact it isn’t. It is an object which returns the successive items
# of the desired sequence when you iterate over it, but it doesn’t really make
# the list, thus saving space.

#this seems like lazy loading to me
print(range(10))

#result: [0,1,2,3]
l = list(range(4))


#Break and continue statements, and else clauses on Loops

# The break statement breaks out of the innermost enclosing for or while loop.
# A loop’s else clause runs when no break occurs

#find the prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#The continue statement, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


#THE PASS STATEMENT

#useful as a placeholder

class PassClass():
    pass

def pass_function():
    pass

