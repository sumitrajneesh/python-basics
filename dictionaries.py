# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


#Create a dictionay

person = {
    'first_name':'sumit',
    'last_name':'choudhary',
    'age':23
}

#Use constructor
#person2 = dict(first_name = 'Sara' , last_name = "Ali khan")

#Get value
print(person['first_name'])
print(person.get('last_name'))


#Add key/value

person['phone'] = '555-555-5555'

#Get dict keys

print(person.keys())

#Get dict items

print(person.items())

#Copy dict
person2 = person.copy()

person2['city']  = 'Bangalore'

#Remove item
del(person['age'])

person.pop('phone')

#Clear
person.clear()

#Get length
print(len(person2))

# print(person)

#list of dict
people = [
    {'name':'sumit', 'age': 30},
    {'name':'Amit', 'age':32}
]

# print(people)
print(people[1]['name'])