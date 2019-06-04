row: int = 5

for i in range(1, row + 1):
    print("*" * i)

for i in range(1, row + 1):
    for j in range(i):
        print("*", end="")
    print()

row: int = 1
while row < 6:
    print("*" * row)
    row += 1

