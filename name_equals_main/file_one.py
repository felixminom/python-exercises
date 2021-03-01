# Python module to execute
#The variable __name__ will always be __main__
#for the module that is run. But the __name__
#variable for all other modules that are being
#imported will be set to their module's name

import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")