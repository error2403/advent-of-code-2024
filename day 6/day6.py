import copy
# --- Day 6: Guard Gallivant ---

def get_map(file: str) -> list[list[str]]:
    """create a 2d array of the guard map given by file"""
    # read input data into 2d array
    with open(file, 'r') as f:
        # get number of lines (rows)
        num_rows = len(f.readlines())

        # get number of characters per line (columns)
        f.seek(0)
        num_cols = len(f.readline())-1

        # create blank 2d array
        # input_map = [num_rows][num_cols]
        input_map = [['.' for i in range(num_cols)] for j in range(num_rows)]

        # populate array
        f.seek(0)
        for line_num, line in enumerate(f.readlines()):
            chars = list(line.rstrip('\n'))

            for char_num, char in enumerate(chars):
                input_map[line_num][char_num] = char

        return input_map
    
def patrol_map(input_map: list[list[str]], log_map: bool = False, step_count: int = -1):
    """advance the guard through the map until they leave 
    and mark locations the guard visited with an 'X'.
    
    args:
        log_map: prints output map to text file for viewing
        iter_count: number of steps the guard takes"""
    guard_map = copy.deepcopy(input_map)
    steps = 1
    # find initial guard position
    guard_pose = [0,0] # (row, col)
    guard_heading = '^'
    for i, row in enumerate(guard_map):
        if row.count('^') > 0:
            guard_pose = [i, row.index('^')]
            break

    # start patrolling map
    has_left = False
    while not has_left:
        try:
            match guard_heading:
                case '^':   # guard facing north
                    # check for obstacle
                    if guard_map[guard_pose[0]-1][guard_pose[1]] == '#':
                        # guard turns 90 degrees right
                        guard_map[guard_pose[0]][guard_pose[1]] = '>'
                        guard_heading = '>'
                    else:
                        # guard advances forward
                        guard_map[guard_pose[0]][guard_pose[1]] = 'X'
                        guard_pose[0] -= 1
                        steps += 1
                        # check for negative looping
                        if guard_pose[0] < 0 or guard_pose[1] < 0:
                            has_left = True
                        else:
                            guard_map[guard_pose[0]][guard_pose[1]] = '^'

                case '>':   # guard facing east
                    # check for obstacle
                    if guard_map[guard_pose[0]][guard_pose[1]+1] == '#':
                        # guard turns 90 degrees right
                        guard_map[guard_pose[0]][guard_pose[1]] = 'V'
                        guard_heading = 'V'
                    else:
                        # guard advances forward
                        guard_map[guard_pose[0]][guard_pose[1]] = 'X'
                        guard_map[guard_pose[0]][guard_pose[1]+1] = '>'
                        guard_pose[1] += 1
                        steps += 1

                case 'V':   # guard facing south
                    # check for obstacle
                    if guard_map[guard_pose[0]+1][guard_pose[1]] == '#':
                        # guard turns 90 degrees right
                        guard_map[guard_pose[0]][guard_pose[1]] = '<'
                        guard_heading = '<'
                    else:
                        # guard advances forward
                        guard_map[guard_pose[0]][guard_pose[1]] = 'X'
                        guard_map[guard_pose[0]+1][guard_pose[1]] = 'V'
                        guard_pose[0] += 1
                        steps += 1

                case '<':   # guard facing west
                    # check for obstacle
                    if guard_map[guard_pose[0]][guard_pose[1]-1] == '#':
                        # guard turns 90 degrees right
                        guard_map[guard_pose[0]][guard_pose[1]] = '^'
                        guard_heading = '^'
                    else:
                        # guard advances forward
                        guard_map[guard_pose[0]][guard_pose[1]] = 'X'
                        guard_pose[1] -= 1
                        steps += 1
                        # check for negative looping
                        if guard_pose[0] < 0 or guard_pose[1] < 0:
                            has_left = True
                        else:
                            guard_map[guard_pose[0]][guard_pose[1]] = '<'

            if (steps > step_count
            and not step_count <= 0):
                has_left = True

        except:
            # guard has left the map
            guard_map[guard_pose[0]][guard_pose[1]] = 'X'
            has_left = True

    if log_map:
        with open("temp.txt", 'w') as file:
            for row in guard_map:
                for char in row:
                    file.write(char)
                file.write('\n')

    return guard_map, steps

def count_distinct_guard_positions(input_map: list[list[str]]):
    """count the number of 'X' chars that are in the map."""
    distinct_pos = 0
    for row in input_map:
        distinct_pos += row.count('X')

    return distinct_pos

def find_infinite_loops(input_map: list[list[str]]):
    """place 1 new obstacle and check if it created an infinite loop."""
    # determine size of grid for max iterations
    # in theory can't take more steps than spaces available
    loop_map = copy.deepcopy(input_map)
    size = len(input_map) * len(input_map[0])

    starting_pose = []
    for i, row in enumerate(loop_map):
        for j, char in enumerate(row):
            if char == '^':
                starting_pose = [i,j]

    loop_count = 0
    for i, row in enumerate(loop_map):
        for j, char in enumerate(row):
            # only run for new placeable obstacles
            if not (char == '#' or char == '^'
                    or (i == starting_pose[0]-1 and j == starting_pose[1])):
                temp = char
                loop_map[i][j] = '#'
                _, steps = patrol_map(loop_map, step_count=size)
                loop_map[i][j] = temp

                if steps > size:
                    loop_count += 1

    return loop_count

input_map = get_map("day 6/input.txt")
pt1_map, _ = patrol_map(input_map, log_map=True)
pos_count = count_distinct_guard_positions(pt1_map)
print("distinct positions visited:", pos_count)

# part 2
loops_found = find_infinite_loops(input_map)
print("loops found:", loops_found)