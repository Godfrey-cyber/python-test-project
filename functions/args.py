from ast import arguments


# *args - a parameter that will pack all arguments into a tuple  useful so that a function can accept a varying amount on arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(3,4,5,6,7,8,9))