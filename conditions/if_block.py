age = input("Hpw old are you: ")
print(age)
min_age = 18
if age == 100:
    print("You are essentially old")
elif age >= min_age:
    print("You are an adult")
elif age <= 0:
    print("You canno be 0 years old")
else:
    print("You are a minor")