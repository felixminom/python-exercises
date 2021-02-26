#String with single quotes
#result: single quoted string
s1 = 'single quoted string'

#Escaped character with \
#result: it does\'nt escape by default
s2 = 'it does\'nt escape by default'

#Escaped by double quotes
#result: it does\'nt escape by default
s3 = "it doesn't escape by default"

#Raw string
#result: C:\testing\raw
s4 = r'C:\testing\raw'

#Multiline string
#result:
#Using this as an example
#    of multiline strings.
#
s5 = """
Using this as an example
    of multiline strings.
"""

#Multiline string (escaping end of line)
#result: This is a string with no end of lines
s6 = """\
This is a string\
with no end of lines\
"""

#Concatenated strings with +
#result: First string Second String
s7 = 'First string' + ' ' + 'Second string'

#Concatenated strings (automatically)
#result: unodos
s8 = 'uno' 'dos'

#result: This is useful when working with really long strings
s9 = ('This is useful when working '
      'with really long strings')


#A character is a string of size one
#type('hola'[0]) = <class 'str'>
#a string can be indexed 
s10 = 'hola mundo'

for char in s10:
    print(char)

#Also negative indexes are valid
#result: o (last character)
print(s10[-1])

#We can slice strings
#result: mundo
#position 5 (included) 10 (excluded)
print(s10[5:10])

#A larger index than the length of the array
#will generate an error
try:
    s10[25]
except:
    print('I failed, index out of scope')

#Strings are 'inmutable' 
#assigning to an indexed position is not valid
try:
    s10[0:1] = 'ne'
except:
    print('Assignation is not valid') 


#Some other methods
s11 = 'Hello world'

#Result: hello world
s11_2 = s11.casefold()

#result = 1 (case sensitive)
number_of_hellos = s11.count('Hello')

#the format method
#using **args
#result: the sum of 1 and 2 is 3
s12 = "the sum of 1 and 2 is {0}".format(1+2)
print(s12)

#using **kwargs
#result: the sum of 1 and 2 is 3
s13 = "the sum of 1 and 2 is {result}".format(result= 1+2)
print(s13)

#Stripping strings
s14 = '    spacious   '

#result: 'spacious   '
print('lstrip:', s14.lstrip())

#result: '   spacious'
print('rstrip:', s14.rstrip())

#split
#result: [1,2,3]
list_of_strings = '1,2,3'.split(',')
print(list_of_strings)


#UNICODE VS BYTESTRING
#definitions
#   character: A character is the smallest possible component of a text
#   code point: A code point is an integer value, usually denoted in base 16.
#   glyph: A character is represented on a screen or on paper by a set of graphical elements that’s called a glyph

#some of this info was took from 
#https://betterprogramming.pub/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686

#when trying to encode something out of ASCII limits an exception will be thrown 
try: 
    "αά".encode('ascii')
except UnicodeEncodeError:
    print("Can't handle this encoding")


#UTF-8 (Unicode Transformation Format, 8-bit numbers are used) 
#result: b'\xce\xb1\xce\xac' type will be bytes
bytes_of_string = "αά".encode('utf-8')

#result: 'αά' type will be str
string_of_bytes = bytes_of_string.decode('utf-8')

#The default type for strings was str, but it was stored as bytes. 
#if you needed to save Unicode strings in Python 2, 
#you had to use a different type called unicode, usually prepending 
#a u to the string itself upon creation.

#1. Now in python3 all strings are unicode
#2. We can create bytes prepeding the b

byte_example = b'\xce\xb1' #byte for α

string_of_byte = byte_example.decode('utf-8')

#It is important to understand that Python does not try to guess the encoding. 
#Rather it uses the encoding returned from locale.getpreferredencoding().

import locale

#result: 'utf-8' (in windows seems to be ASCII)
l = locale.getdefaultlocale()