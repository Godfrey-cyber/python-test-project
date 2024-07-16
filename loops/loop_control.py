# loop control statement - they change the flow of loops from their normal flow
# break = terminates the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothoong acts a s a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break
phone_number = '123-456-098'
for i in phone_number:
    if i == "-":
        continue
    print(i)