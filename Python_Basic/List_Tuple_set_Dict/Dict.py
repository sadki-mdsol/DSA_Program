data = {'1':'One',2:'Two'}

print(data.get('1'))

print(data.get('xyz'))

print(data['1'])

print(data.get('xyz','DEfault if key not exist'))

keys = ['Sneha','Vijay']
values = ['C++','Python']

name_lng = dict(zip(keys,values))

print(name_lng)

name_lng['Navin'] = 'Java'
print(name_lng)


del name_lng['Navin']
print(name_lng)


prog = {
    'JS':'Atom',
    'Python':['Sublime','Pycharm'],
    'Java':{
        'J2SE':['VS','Atom'],
        'J2EE':'Eclipse'
    }
}

print(prog)
print(prog['JS'])
print(prog['Python'])
print(prog['Java']['J2SE'])
print(prog['Java']['J2SE'][0])