import copy
# --- Day 7: Bridge Repair ---

def get_equations(file: str) -> list[tuple[int, list[int]]]:
    """read file and extract equations."""
    equations = []
    with open(file, 'r') as f:
        for line in f.readlines():
            equation = line.split(': ')
            test_value = int(equation[0])
            str_remaining_nums = equation[1].rstrip('\n').split(' ')

            # convert from string to int
            remaining_nums = []
            for str_int in str_remaining_nums:
                remaining_nums.append(int(str_int))

            equations.append((test_value, remaining_nums))

    return equations


def eval_equation(expected:int, current:int, operator:str, rem_nums: list[int], is_part2: bool = False):
    """temp"""
    copy_list = copy.deepcopy(rem_nums)
    #print(current, operator, copy_list)
    if len(copy_list) == 0:
        return expected == current
    
    # if overshoot, give up
    if current > expected:
        return False
    
    if operator == '+':
        current += copy_list.pop(0)
    elif operator == '*':
        current *= copy_list.pop(0)
    elif operator == '||':
        current = int(str(current)+str(copy_list.pop(0)))
    else:
        pass

    if is_part2:
        return (eval_equation(expected, current, '+', copy_list, is_part2)
            or eval_equation(expected, current, '*', copy_list, is_part2)
            or eval_equation(expected, current, '||', copy_list, is_part2))
    else:
        return (eval_equation(expected, current, '+', copy_list)
            or eval_equation(expected, current, '*', copy_list))     


def test_equations(equations: list[tuple[int, list[int]]], is_part2: bool = False) -> int:
    """temp"""
    calibration_result = 0
    for equation in equations:
        rem_nums = equation[1]
        is_valid = eval_equation(equation[0], 0, '+', rem_nums, is_part2)

        if is_valid:
            calibration_result += equation[0]

    return calibration_result    

equations = get_equations("day 7/input.txt")
cal_result = test_equations(equations, is_part2=False)
print("part 1:",cal_result)
cal_result = test_equations(equations, is_part2=True)
print("part 2:",cal_result)