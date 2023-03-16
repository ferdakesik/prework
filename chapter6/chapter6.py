# my_dic={}
# my_dict=dict()
# my_dic={
#     "key":"value"
# }

# my_dic=dict(key="value")

#collection of pair value

steve={
    "name" : "Steve",
    "weight" : 155.5,
    "height" : 70,
    "foods" : ["country fried steak", "fried chicken","collards"],
    "ice_cream":{
        "vanilla":False,
        "choclate":True,
        "coffee":False
    },
    10:"this has an integer key"
}

print(type(steve))
#name of the dictionary [KEY]
print(steve["name"])
print(type(steve["name"].upper()))
print(steve["name"])
print(type(steve["weight"]))
print(type(steve["height"]))
print((steve["height"]))
print(type(steve["foods"]))
print((steve["foods"]))
print((steve["foods"][2]))
print((steve["ice_cream"]["vanilla"]))

print(steve.get("candies")) #none
print(steve.get("candies","no candy list"))

#chnage value of key
steve["name"]="joe"
print(steve)
my_list=[1,2,3]
my_list[1]="WOW"
print(my_list)

steve.update({
    "candies":["snickers","mars","m&m"]
})
print(steve)
del steve["candies"]
print(steve)


for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

for key in steve.values():  
    print(steve.values())
    
for value in steve.values():
    print(value)
    print(type(value))
    
    
for key,value in steve.items():
    # print(key)
    # print(value)
    if isinstance(value,list):
        print(f"The list is at {key}")
        
    
    
    
