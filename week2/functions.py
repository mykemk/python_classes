'''
In this class we intend to cover functions:
- Inbuilt functions
- User defined functions
- Intro to functions --functions declared using def
- Parameters and arguments ---parameters are values passed to the functions
- Positional and keyword arguments -- 
- Declaring return values for functions 
- Basics of functions coding exercise
- Default arguments coding exercise ---default arguments have default values in python
- Function annotations
- Lambda functions --a function defined without a name
- Functions quiz
- Python arbitrary arguments ---they're denoted using an arterisk (*) before the parameter name
Arbitrary are useful when we don't know the number of arguments to expect in a function call
- Git repo: https://github.com/MichaelMurithi/python_classes
'''

list = [1,2,3,4,5,6,7,12]

nums_sum = sum(list) #sum is an inbuilt function
print(nums_sum)

def teach(student):
    print(f'The lecturer is teaching student')


def is_even(number):
    return number % 2 == 0

#Keyword arguments
def greet(visitor, language="english"):
    visitor = input("Who is the visitor?")
    greeting = "Hello"
    if language == 'slovak':
        greeting = "Ahoj"
    print(greeting,visitor)
    
greet("Cherono",language="slovak")

# print(is_even(10))
#Converting fareignheight to celsius
#Lambda functions


'''
- lambda function has the following syntax: lambda arguments: expression
- Lambda functions can have any number of arguments but only one expression
- Used when we require a nameless function for a short period of time
- Generally used as arguments to a high order function like filter(), map()
- 
'''

#lambda functions
addTen = lambda x : x+10
print(addTen(10))