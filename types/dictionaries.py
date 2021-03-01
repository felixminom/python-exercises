#Unlike sequences, which are indexed by a range of numbers,
# dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys.

#It is best to think of a dictionary as a set of key: value pairs,
# with the requirement that the keys are unique (within one dictionary).

MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

#result: Rockies
MLB_team['Colorado']

#delete element
del MLB_team['Seattle']

#add key, val pair
MLB_team['Quito'] = 'Nacho'

#result: ['Colorado', 'Boston', 'Minnesota', 'Milwaukee', 'Quito']
list(MLB_team)

#result: ['Boston', 'Colorado', 'Milwaukee', 'Minnesota', 'Quito']
sorted(MLB_team)

#result: False
'Guayaquil' in MLB_team

#result: True
'Boston' in MLB_team

#Bulding a dictionarie incrementally
person = {}

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

#result: Joe
person['fname']

#result: 51
person['age']

#result: ['Ralph', 'Betty', 'Joey']
person['children']

#result: Joey
person['children'][-1]

#Sox
person['pets']['cat']


#When looping through dictionaries, the key and corresponding value
#can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


#keys() returns a list of all keys in the dictionary
d = {'a': 10, 'b': 20, 'c': 30}

for k in d.keys():
    print(k)

#values() returns a list of all values in the dictionary
for v in d.values():
    print(v)