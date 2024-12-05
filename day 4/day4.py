# --- Day 4: Ceres Search ---

# read input data into 2d array
with open("day 4/input.txt", 'r') as f:
    # get number of lines
    num_lines = len(f.readlines())

    # get number of characters per line
    f.seek(0)
    num_chars = len(f.readline())-1

    # create blank 2d array
    # input_data = [num_lines][num_chars]
    input_data = [['.' for i in range(num_chars)] for j in range(num_lines)]
    
    # populate array
    f.seek(0)
    for line_num, line in enumerate(f.readlines()):
        chars = list(line.rstrip('\n'))

        for char_num, char in enumerate(chars):
            input_data[line_num][char_num] = char


## Part 1 - XMAS count

# find horizontal count of 'XMAS'
horizontal_count = 0
for row in input_data:
    # check for forward spelling
    for pos, char in enumerate(row):
        if char == 'X' and pos < num_chars-3:
            # found start, check for completion
            if (row[pos+1] == 'M'
            and row[pos+2] == 'A'
            and row[pos+3] == 'S'):
                horizontal_count += 1

        # check for backward spelling
        if char == 'X' and pos > 2:
            # found start, check for completion
            if (row[pos-1] == 'M'
            and row[pos-2] == 'A'
            and row[pos-3] == 'S'):
                horizontal_count += 1

print("horizontal:", horizontal_count)

# find vertical count of 'XMAS'
vertical_count = 0
for col in range(num_chars):
    for row in range(num_lines):
        # check for downward spelling
        if input_data[row][col] == 'X' and row < num_lines-3:
            # found start, check for completion
            if (input_data[row+1][col] == 'M'
            and input_data[row+2][col] == 'A'
            and input_data[row+3][col] == 'S'):
                vertical_count += 1

        # check for upward spelling
        if input_data[row][col] == 'X' and row > 2:
            # found start, check for completion
            if (input_data[row-1][col] == 'M'
            and input_data[row-2][col] == 'A'
            and input_data[row-3][col] == 'S'):
                vertical_count += 1

print("vertical:", vertical_count)

# find diagonal count of 'XMAS'
# diagonals: 
#   [+][+] --> right & up
#   [+][-] --> right & down
#   [-][+] --> left & up
#   [-][-] --> left & down
diagonal_count = 0
for row in range(num_lines):
    for col in range(num_chars):
        # check [+][+] diagonal
        if (input_data[row][col] == 'X'
        and col < num_chars-3
        and row > 2):
            # found start, check for completion
            if (input_data[row-1][col+1] == 'M'
            and input_data[row-2][col+2] == 'A'
            and input_data[row-3][col+3] == 'S'):
                diagonal_count += 1 

        # check [+][-] diagonal
        if (input_data[row][col] == 'X'
        and col < num_chars-3
        and row < num_lines-3):
            # found start, check for completion
            if (input_data[row+1][col+1] == 'M'
            and input_data[row+2][col+2] == 'A'
            and input_data[row+3][col+3] == 'S'):
                diagonal_count += 1

        # check [-][+] diagonal
        if (input_data[row][col] == 'X'
        and col > 2
        and row > 2):
            # found start, check for completion
            if (input_data[row-1][col-1] == 'M'
            and input_data[row-2][col-2] == 'A'
            and input_data[row-3][col-3] == 'S'):
                diagonal_count += 1

        # check [-][-] diagonal
        if (input_data[row][col] == 'X'
        and col > 2
        and row < num_lines-3):
            # found start, check for completion
            if (input_data[row+1][col-1] == 'M'
            and input_data[row+2][col-2] == 'A'
            and input_data[row+3][col-3] == 'S'):
                diagonal_count += 1

print("diagonal:", diagonal_count)
print("total:", horizontal_count+vertical_count+diagonal_count)

## Part 2 - X-MAS count (MAS in the shape of an x)
##                      eg: M . M
##                          . A .
##                          S . S

mas_count = 0
for row in range(num_lines):
    for col in range(num_chars):
        # find a valid 'A'
        if (input_data[row][col] == 'A'
        and row > 0 and row < num_lines-1
        and col > 0 and col < num_chars-1):
            
            # check M's on top
            if (input_data[row-1][col-1] == 'M'
            and input_data[row-1][col+1] == 'M'
            and input_data[row+1][col-1] == 'S'
            and input_data[row+1][col+1] == 'S'):
                mas_count += 1

            # check M's on right
            if (input_data[row-1][col-1] == 'S'
            and input_data[row-1][col+1] == 'M'
            and input_data[row+1][col-1] == 'S'
            and input_data[row+1][col+1] == 'M'):
                mas_count += 1

            # check M's on bottom
            if (input_data[row-1][col-1] == 'S'
            and input_data[row-1][col+1] == 'S'
            and input_data[row+1][col-1] == 'M'
            and input_data[row+1][col+1] == 'M'):
                mas_count += 1

            # check M's on left
            if (input_data[row-1][col-1] == 'M'
            and input_data[row-1][col+1] == 'S'
            and input_data[row+1][col-1] == 'M'
            and input_data[row+1][col+1] == 'S'):
                mas_count += 1

print("mas count:", mas_count)