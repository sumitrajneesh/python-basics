# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# name = 'sumit'
# age = 24

#Concatenate
# print('Hello , my name is ' + name + 'and  i am ' + str(age))
# String Formatting
#Arguments by position 
# print('My name is {name} and I am  {age} '.format(name=name, age=age))

#F-Strings (3.6+)
# print(f'My name is {name} and I am  {age} ')
# String Methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower

print(s.lower())

#Replace
print(s.replace('world','everyone'))
#Swap case
print(s.swapcase())

#Count
sub = 'h'

print(s.count(sub))

#Start with
print(s.startswith('hello'))

#End with
print(s.endswith('d'))

#split into a list
print(s.split())

#Find position

print(s.find('r'))


#Is all alphanumeric
print(s.isalnum())

#Is all alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())

