#def NAME_OF_FUNCTION(PARAMETERS):
    #THESE LINE
    #BELONG
    #TO THE CODE BLOCK
    #FOR THE FUNCTION
    
# def hello():
#     #print("hello")
#     return "hello"
    
# print(hello().upper())

# def hello(name,age):
#     print(f"hello {name} you are {age} years old")
    
# # hello(name="ferda",age=202)
# hello("kevin",23)


def say_hello(name,age):
    print(f"hello {name} you are {age} years old")

def say_goodbye():
    print("Goodbye")
    
def greet_back(feeling):
    if feeling=="good":
        print("awesome. i am good too")
    elif feeling=="bad":
        print("i am so sorry")
    elif feeling=="stressed":
        print("coding can be hard to learn")
    else:
        print("well, have a good day")
        
#driver code
while True:
    response= input("what do you want to do? say hello [H] say goodbye [G] talk to me [T], quit [Q]")
    if response.lower()=='q':
        break
    elif response.lower()=='h':
        name=input("what is your name?")
        age=input("what is your age?")
        say_hello(name,age)
    elif response.lower()=='g':
        say_goodbye()
    elif response.lower()=='t':
        feeling==input("how are you today?")
        greet_back(feeling)
    else:
        print("invalid input")
        
        

    