foods=["pizza","tacos","dim sum","sushi"]

print(foods[1])

print()

#for PLACEHOLDER in THE_LIST_WE_WANT_TO_LOOK_AT:
    #THIS IS A CODE BLOCK
    #THIS CODE BLOCK
    #WILL RUN EVERY ITEM IN THE LIST
    
# for food in foods:
#     print(f"I like to eat {food}")
#     print(type(food))
    
# print("loop is over")

for food in foods:
    if food == "pizza":
        continue
    print(f"I like {food} beacuse they are yummy")
    
for index in range(len(foods)):
    print(index)
    print(foods[index])
    
print(list(enumerate(foods)))

for index,food in enumerate(foods):
    print(f"my no {index +1} food is {food.title()}")
    
#loop of the index
print(list(range(len(foods))))
print(len(foods))





 


    
