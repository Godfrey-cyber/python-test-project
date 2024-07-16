import time
# for loops - a statement that executes ablock of code a limited amount of time unlike a while loops which executes unlimited amount of time
for i in range(10):
    print(i + 1)

for i in range(50, 100, 2): # the last number is not inclusive
    print(i + 1)

for j in "Godfrey":
    print(j)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new Year")

food = ['pizza', 'spaghetti', 'humburger', 'sushi']

for x in food:
    print(x)