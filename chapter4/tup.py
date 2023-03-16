my_string=1,2
print(type(my_string))
my_string=(1,2)
print(type(my_string))
print(my_string)

#tuple cant change, immutable

print(my_string[1])

for num in my_string:
    print(num)
    
my_string = my_string + (3,4)
print(my_string)
