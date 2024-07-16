# nested loops - the inner loop will finish all its iteration before finishing one interation of the outer loop

rows = int(input("Rows: "))
cols = int(input("Cols: "))

symbol = "%" #input("Enter symbol: ")

for i in range(rows):
    for j in range(cols):
        print(symbol)
    print("")