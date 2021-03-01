#Errors detected during execution are called exceptions

#BaseException: The base class for all built-in exceptions.
#It is not meant to be directly inherited by user-defined
#classes (for that, use Exception).

#NameError: Raised when a local or global name is not found.
#This applies only to unqualified names. The associated value
#is an error message that includes the name that could not be found.
#result: name 'a' is not defined
try:
    print(a)
except NameError as error:
    print(error)

#AttributeError: can be defined as an error that is raised
#when an attribute reference or assignment fails.
#result: 'int' object has no attribute 'append'

X = 10

try:
    X.append(6)
except AttributeError as error:
    print(error)

#ImportError: Raised when the import statement has troubles trying
#to load a module. Also raised when the “from list” in from ... import
#has a name that cannot be found.
#result: No module named 'fibonnaci'
try:
    import fibonnaci
except ImportError as error:
    print(error)



#EAFP vs LBYL

#Let's see an example of this with a dictionary.

#KeyError: Raised when a mapping (dictionary) key is not
#found in the set of existing keys.

weather_by_city = {
    'Quito': 18,
    'Guayaquil': 27,
    'Cuenca': 20
}

#EAFP
#EAFP means that you should just do what you expect to work
#and if an exception might be thrown from the operation then
#catch it and deal with that fact.

try:
    weather_by_city['Ambato']
except KeyError as error:
    print(error)

#LBYL
#LBYL is when you first check whether something will succeed
#and only proceed if you know it will work.

if 'Ambato' in weather_by_city:
    print('I have this city')


#Raising exceptions
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')


#Finally clause
#The try statement has another optional clause which is
#intended to define clean-up actions that must be executed
#under all circumstances. This is the finally clause

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except Exception as error:
        #To catch all cases
        print(error)
    else:
        print("result is", result)
    finally:
        #This will execute even if a exception is raised
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")
