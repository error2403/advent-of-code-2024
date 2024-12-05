import re

# --- Day 3: Mull It Over ---

# define regexs needed
mul_regex = re.compile('mul\\(\\d+,\\d+\\)')
digit_regex = re.compile('\\d+')
do_regex = re.compile('do\\(\\)')
dont_regex = re.compile('don\'t\\(\\)')

def mul_instruction(instr: str) -> int:
    """take mul instruction and compute multiplcation result.
    """
    # extract digits
    digits = digit_regex.findall(instr)
    
    return int(digits[0]) * int(digits[1])

# read input text
input_text = ""
with open("day 3/input.txt", 'r') as f:
    input_text = f.read()


### part 1 find all mul instructions ###

# find all occurances of mul instruction
muls = mul_regex.findall(input_text)

# execute mul instructions
result = 0
for mul in muls:
    result += mul_instruction(mul)
print(result)

### part 2 include do() and don't() instructions ###
# remove disabled muls
while(True):
    # search for an instance of don't()
    dont_pos = dont_regex.search(input_text)

    if dont_pos == None:
        # no more don't() instructions
        print("no more occurances")
        break
    else:
        # check if do() instruction follows
        do_pos = do_regex.search(input_text, dont_pos.start())

        if do_pos == None:
            # no more do() instructions, disable end text and break
            input_text = input_text[:dont_pos.start()]
            break
        else:
            # remove disabled subsection
            input_text = input_text[:dont_pos.start()] + input_text[do_pos.start()+1:]

print(input_text)

# find all occurances of mul instruction
muls = mul_regex.findall(input_text)

# execute mul instructions
result = 0
for mul in muls:
    result += mul_instruction(mul)
print(result)