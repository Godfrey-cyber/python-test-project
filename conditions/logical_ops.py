#logical operators
temp = input("What is the temperature?: ")

if temp >= 0 and temp <= 30:
    print("The temperature is good today")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")