#I'll use Fibonacci's serie as example

def FibonacciSeries(limit):
    #multi assigment
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b, a+b

#result: 0,1,1,2,3,5,8
print(FibonacciSeries(10))