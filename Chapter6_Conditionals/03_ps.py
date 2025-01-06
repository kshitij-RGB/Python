list = ["Kshitij", "Riya", "Rishabh", "Suraj"]

name = input("Enter your name: ")

if(name in list):
    print("Already present..")
else:
    list.append(name)
    print("Name updated in list \n", list)