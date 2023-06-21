#Strings  <class 'str'>
#ejemplos de uso comillas
print("Hello world")
print('hello world')
print('''hello world''')
print("""hello world """)
#ejemplo type
print(type("hello world"))
#concadenacion
print("bye" + "world")
#Numbers
print(type(30))   #int
print(type(30.5))  #float
print(type(22))  #int
print(type(21.5))   #float

#boolean
print(type(True))
print(type(False))


#list
[10, 20, 30, 55]
['hello', 'bye', 'adios']
[10, 'hello', True, 10.1]
[]  #vacia
print(type([10, 'hello', True, 10.1]))

#tuples

print(type((10, 20, 30, 55)))
() #vacia

#dictorionies, importante poner comas al final y los puntos
{   
    "name":"ryan",
    "lastname":"castro",
    "nickname":"guty" 
}
{
    "lat": 1214554,
    "long": 1541415
}
#<class 'dict'>
print(type({   
    "name":"ryan",
    "lastname":"castro",
    "nickname":"guty" 
}))


print(type(None)) 