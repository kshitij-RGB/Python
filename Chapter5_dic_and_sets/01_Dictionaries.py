dd = {} #empty dictionary
a = {
    "name":"kshitij",
    "lname":"saxena",
    "age":18,
    "list":[10,True,"Happy"]
}
# print(a)
# print(a.items())
# print(a.keys())
# print(a.values())
# a.update({"age": 21})
# print(a["age"])

# print(a.get("name")) #if key does not exist it prints None
# print(a["name"])  #if key does not exist it prints an error
print(a.pop("list"))
print(a.popitem())
print(a.popitem())

