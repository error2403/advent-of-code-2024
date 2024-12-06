# --- Day 5: Print Queue ---

def parse_rules(rules: list[str]) -> dict:
    """read input file rules section and make dictionary of before/after pages."""
    rules_dict = {}
    for rule in rules:
        rule.rstrip('\n')
        # break into before and after pages
        pages = rule.split('|')
        
        # if rule is not in dict then add it, else append
        if rules_dict.get(pages[0]) == None:
            rules_dict[pages[0]] = [pages[1].rstrip('\n')]
        else:
            temp = rules_dict.get(pages[0])
            temp.append(pages[1].rstrip('\n'))

    return rules_dict

def parse_input(file: str) -> tuple[dict, list[str]]:
    """read input file to collect rules & updates."""

    with open(file, 'r') as f:
        # read file
        data = f.readlines()

        # split data into rules and updates
        break_line = data.index('\n')
        input_rules = data[:break_line]
        updates = data[break_line+1:]

        rules = parse_rules(input_rules)

        # remove trailing \n from updates
        for i in range(len(updates)):
            updates[i] = updates[i].rstrip('\n')

        return rules, updates
    
def check_update_order(updates: list[str], rules: dict) -> tuple[list, list]:
    """compare the update page order to the rules."""
    correct = []
    incorrect = []
    for update in updates:
        passed = True
        pages = update.split(',')
        for i, current_page in enumerate(pages):
            # check if it follows rules
            # no dict value can come before key
            if rules.get(current_page) == None:
                # page doesnt have any rules to follow
                pass
            else:
                page_rules = rules.get(current_page)
                for temp_page in pages[:i]:
                    if page_rules.count(temp_page) > 0:
                        passed = False
                        break

        if passed:
            correct.append(update)
        else:
            incorrect.append(update)
    
    return correct, incorrect

def sum_middle_pages(updates: list[str]) -> int:
    """sum the middle pages of updates"""
    page_sum = 0
    for update in updates:
        pages = update.split(',')
        page_sum += int(pages.pop(int(len(pages)/2)))

    return page_sum

def fix_incorrect_updates(updates: list[str], rules: dict):
    """re-order the pages of the incorrect updates to obey rules"""
    corrected_updates = []
    for update in updates:
        pages = update.split(',')
        temp_update = []
        for current_page in pages:
            # check if it follows rules
            # no dict value can come before key
            if rules.get(current_page) == None:
                # page doesnt have any rules to follow, add to end
                temp_update.append(current_page)
                
            else:
                page_rules = rules.get(current_page)

                rule_broken = False
                for i, temp_page in enumerate(temp_update):
                    if page_rules.count(temp_page) > 0:
                        # broke rule, place 1 spot before
                        temp_update.insert(i, current_page)
                        rule_broken = True
                        break

                if not rule_broken:
                    temp_update.append(current_page)
            
        # covert back into string
        update_str = ""
        for page in temp_update:
            update_str += page + ','
        corrected_updates.append(update_str.rstrip(','))

    return corrected_updates


rules, updates = parse_input("day 5/input.txt")
correct_updates, incorrect_updates = check_update_order(updates, rules)
part1_answer = sum_middle_pages(correct_updates)
print("part 1", part1_answer)

corrected_updates = fix_incorrect_updates(incorrect_updates, rules)
part2_answer = sum_middle_pages(corrected_updates)
print("part 2", part2_answer)