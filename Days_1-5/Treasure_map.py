
row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map = [row1, row2, row3]

position = "33"
row = position[0:1]
column = position[1:2]


map[int(row) - 1][int(column) -1] = "X"
print(f"{row1}\n{row2}\n{row3}")

