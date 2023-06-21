myStr = "hello world"

#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello", "bye").upper())
print(myStr.replace("hello", "bye").lower())

print(myStr.count(" "))

print(myStr.startswith("hello"))
print(myStr.endswith("hello"))

print(myStr.split('o'))
print(myStr.find('o'))
print(myStr.find(' '))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])