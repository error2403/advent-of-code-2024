from typing import List

###   --- Day 1: Historian Hysteria ---   ###

def parse_input_file(file: str) -> tuple[List[int], List[int]]:
    """Parse the input file and split into 2 lists
    a left and a right column."""

    left_column = []
    right_column = []

    with open(file, 'r') as input:
        for line in input:
            values = line.split("   ")
            left_column.append(values[0])
            right_column.append(values[1].rstrip())

        return left_column, right_column
    

def compute_distances(left_col: List[int], right_col: List[int]) -> int:
    """Sort the parsed lists from low to high. then find the difference
    between the values and sum differences."""

    # sort columns
    left_col.sort()
    right_col.sort()
    
    distance = 0
    for i in range(len(left_col)):
        left_val = left_col[i]
        right_val = right_col[i]

        distance += abs(int(left_val) - int(right_val))
    
    return distance

def compute_similarity(left_col: List[int], right_col: List[int]) -> int:
    """figure out exactly how often each number from the left list
    appears in the right list. Calculate a total similarity score by
    adding up each number in the left list after multiplying it by the
    number of times that number appears in the right list."""

    similarity = 0
    for value in left_col:
        similarity += int(value) * right_col.count(value)

    return similarity


# main code loop for part 1
left_col, right_col = parse_input_file("day 1/input.txt")
dist = compute_distances(left_col, right_col)
print(dist, "\n")

# main code loop for part 2
similarity = compute_similarity(left_col, right_col)
print(similarity)

