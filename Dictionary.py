person = {
    "name": "Aditi",
    "role": "Mentor"
}
print(person["name"])
print(person["role"])
person["city"] = "Chennai"
for key, value in person.items():
    print(key, ":", value)