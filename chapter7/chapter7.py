#the while loop
#while Boolean or Boolen exp:
#code block
#to run while
#condition is True


#you must be over 5 feet to ride my ride

# height=55
# while height<60:
#     height +=1
#     if height<58:
#         continue
#     print(f"you are {height} inches tall \n and too short to ride")
#     print("did my magic portion")
#     if height ==58:
#         break
   
# print("thank for coming")  


while True:
    response=input("what do you want to do? say hi [h], say goodbye [g], or quit?[q]")
    if response.lower()=="h":
        print("hello")
    elif response.lower()=="g":
        print("goodbye")
    elif response.lower()=="q":
        break
    else:
        print("invalide")
        
    