fullname = "Kshitij Saxena"
#string slicing
firstname = fullname[0:7]
print(firstname)

#negative string slicing
lastname = fullname[-6:]
print(lastname)
# Or we can convert negative slicing into postive slicing by (length +(-ve index))
last_name=fullname[8:14]
print(last_name)


#skipping slicing
a="0123456789"
print(a[2:10:2])
