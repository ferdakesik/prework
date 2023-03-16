print("hello")
2+2
numbers=[2,4,5,3,2]
print(numbers)
print(type(numbers))
print(numbers[1])
print(type(numbers[1]))
print([1,2,3,4,5][0])
print(6)
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

foods=["pizza","tacos","dim sum","sushi"]
print(type(foods))
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x=12
y=15.5
z="Z"
random_list=[x,y,z]
print(random_list)
print(random_list[0])
print(type(random_list[0]))
print(random_list[1])
print(type(random_list[1]))
print(random_list[2])
print(type(random_list[2]))

foods.append("cheeseburger") #end of the list-in place
print(foods)

#not to do
#foods=foods.append("cheeseburger") it returns none

foods.insert(0,"pho")
print(foods)

foods.remove("pho")
print(foods)

#foods.remove("burrito")

foods.append("pizza")
print(foods)
foods.remove("pizza") #removed first
print(foods)

foods=["pizza","tacos","dum sum","sushi"]
print(foods)
del foods[1]
print(foods)


foods=["pizza","tacos","dum sum","sushi"]
print(foods.pop())
print(foods)

#method of the list class called .sort
#built in function called sorted()

#sort in place
foods=["pizza","tacos","dum sum","sushi"]
print(foods.sort()) # alpahetic
print(foods)
print(foods.sort(reverse=True))
print(foods)

#sorted out of place
foods=["pizza","tacos","dum sum","sushi"]
print(sorted(foods))
print(foods)
foods=sorted(foods)
print(foods)
foods=sorted(foods,reverse=True)
print(foods)

foods=["pizza","tacos","dum sum","sushi"]
foods.reverse()
print(foods)

foods=["pizza","tacos","dum sum","sushi"]

print(foods[2])






