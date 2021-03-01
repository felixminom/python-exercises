#Truthy and Falsy values are not truth values themselves,
#but they evaluate to either True or False.

#Falsy values:
#Empty lists []
#Empty tuples ()
#Empty dics {}
#Empty sets set()
#Empty strings ""
#Empty ranges range(0)
#Numbers: 0, 0.0, 0j
#None
#False

if []:
    print('Not here')
else:
    print('But here')

if None:
    print('Not here 2')
else:
    print('But here 2')


if 5:
    print('Don\'t need an else clause')


#result: True
bool([1,2,3])

#result: False
bool('')

#result: True
bool((1,2))

class CustomFalseBool():
    val = 0
    def __init__(self, num):
        self.value = num
    def __bool__(self):
        return False

#This should be True. But the __bool__ method is overwriten
#so the result is False
a = CustomFalseBool(15)
print(bool(a))


#result: False
b = CustomFalseBool(0)
print(bool(b))
