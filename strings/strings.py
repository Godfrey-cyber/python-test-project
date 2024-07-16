# Strings
name = "Godfrey Ndiritu"
print(len(name)) #lenght
print(name.find('r')) # position of r
print(name.upper()) #uppercase
print(name.lower()) # lowercase
print(name.capitalize()) # capitalize
print(name.isdigit()) #if is number
print(name.isalpha()) # contains only alpjhabets letters
print(name.count('o')) # counts all o
print(name.replace('o', 'a')) # replace o with a
print(name*3) #*3

# splicing [start:stop:step]
name = 'Godfrey Ndiritu'
first_name = name[0:7] # 1st index is inclusive the last one is not inclusive or [:7]
last_name = name[8:] # 1st index is inclusive the last one is not inclusive or [:7]
print(first_name)
print(last_name)

website = "https://google.com"
slice = slice(7, -4)
print(website[slice])

# index operator - gives sequence to the element
name = 'bro Code'
print(name[0]).isupper()
print(name[0:3]).upper()
