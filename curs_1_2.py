print("Hello111")

name = "Ana"
print(name)

names = ["Ana", "Maria", "Ioana", "Elena", "Daniela", "Ana"]
keyword = "Elena"

if keyword not in names:
    print(f"{keyword} was not found")
else:
    print(f"{keyword} is found")

d1 = {1: "Salut"}
d2 = d1
print(d1 is d2)

d3 = {1: "Salut"}
d4 = d3
print(d3 is d4)

print(ord("a"))
print(chr(97))

# Strings are immutable
# name[0]="D"

print(names[-2:])
print(sorted(names))
# This function will update the list
# names.sort()
print(names)

unique_names = set(names)
print(unique_names)

# Set-urile nu sunt indexate
# print(unique_names[0])

person = {
    "first_name": "Ion",
    "last_name": "Popescu"
}

print(person.get('age', 0))
# In this case you will have an error
# print(person['age'])