# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers = [1,2,3,4,5]

fruits = ['apple', 'Oranges', 'Grapes', 'Pears']

#Use a constructor
#number2 = list((1,2,3,4,5))

#Get a value
print(fruits[1])

#Get length

print(len(fruits))

#Append to list
fruits.append('Mangos')

#Remove from list
fruits.remove('Grapes')


#Change value

fruits[0] = 'Blueberries'

#Remove with pop
fruits.pop(2)

#Reverse list
fruits.reverse()


#Reverse list
fruits.reverse()

#sort list

fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

print(fruits)
