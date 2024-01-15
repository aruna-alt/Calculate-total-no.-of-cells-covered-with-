rows = 20
cols = 20
grid = [['*' for _ in range(cols)] for _ in range(rows)]

row_number = int(input("Enter the row number (0 to 19): "))
col_number = int(input("Enter the column number (0 to 19): "))

count_at_symbols = 0

grid[row_number][col_number] = '@'
count_at_symbols += 1

for i in range(row_number + 1, rows):
    if col_number - (i - row_number) >= 0:
        grid[i][col_number - (i - row_number)] = '@'
        count_at_symbols += 1
    if col_number + (i - row_number) < cols:
        grid[i][col_number + (i - row_number)] = '@'
        count_at_symbols += 1
       
        if col_number - (i - row_number) == 0:
            for j in range(i + 1, rows):
                grid[j][0] = '@'
                count_at_symbols += 1

        
        elif col_number + (i - row_number) == cols - 1:
            for j in range(i + 1, rows):
                grid[j][cols - 1] = '@'
                count_at_symbols += 1


for i in range(row_number + 1, rows):
    for j in range(cols):
        if j >= col_number - (i - row_number) and j <= col_number + (i - row_number):
            grid[i][j] = '@'
            count_at_symbols += 1

for row in grid:
    print(' '.join(row))
    
print(f'Total number of cells covered with "@" symbols: {count_at_symbols}')
