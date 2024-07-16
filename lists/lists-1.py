#lists - store multiple items within a variable
food = ['pizza', 'spaghetti', 'humburger', 'sushi']
print(food)
print(food[0]) # pizza
# food[4] = 'pudding'
print(food)

for x in food:
    print(x)

cars = ['Bughatti', 'Tesla', 'Mercedes', 'Toyota', 'Nissan', 'Subaru', 'Ford', 'Scania']

for x in range(len(cars)):
    print(x)

for car in cars:
    print(car) # prints all the cars

cars.append('Range Rover') # adds
cars.remove('scania') # removes
cars.pop() # removes the last
cars.sort() # sorts
cars.clear() # clears everything