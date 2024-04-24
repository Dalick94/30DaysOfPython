### DICTIONARIES ###

dog = {}
dog = {"name":"ronaldo", "color":"white", "breed":"dogo", "legs":4, "age":4}
student = {
        "first_name":"Guillermo",
        "last_name":"Vivancos",
        "gender":"male",
        "age":29,
        "marital_status":"single", 
        "skills":"hardworking",
        "country":"Spain",
        "city":"Murcia",
        "address":"Cartagena"}

print(len(student))

print(student["skills"])
print(type(student["skills"]))

student["skills"] = "Hardworking", "Torero", "Bailaor"
print(student)


print(dog.keys())
print(dog.values())

print(dog.items())

dog = {"name":"ronaldo", "color":"white", "breed":"dogo", "legs":4, "age":4}
del dog ["name"]
print(dog)

del dog