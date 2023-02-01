# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?:"))
columns = int(input("How many columns?:"))
symbol = input("Enter a symbol: ")

for i in range(columns):
    for j in range(rows):
        print(symbol, end=" ")
    print()