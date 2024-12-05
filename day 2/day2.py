### --- Day 2: Red-Nosed Reports ---

def get_reports(file: str):
    """read input file and save each line as a report.
    """
    reports = []
    with open(file, 'r') as f:
        for line in f:
            reports.append(line.rstrip())

    return reports

def check_safety(reports):
    """reactor safety systems can only tolerate levels that are either
    gradually increasing or gradually decreasing. So, a report only counts
    as safe if both of the following are true:

    -- The levels are either all increasing or all decreasing.
    -- Any two adjacent levels differ by at least one and at most three.
    """

    num_safe_reports = 0;
    safe_reports = []
    unsafe_reports = []

    for report in reports:
        # get levels from report
        levels = report.split(" ")
        is_safe = True
        reason = ""

        # convert str to int
        for i in range(len(levels)):
            levels[i] = int(levels[i])
        
        # check if levels are increasing or decreasing
        if levels[0] > levels[1]:
            # decreasing
            for i in range(len(levels)-1):
                # check if all are decreasing
                if not levels[i] > levels[i+1]:
                    # not decreasing
                    is_safe = False
                    reason = "not decreasing"

                # check for unsafe difference
                diff = levels[i] - levels[i+1]
                if abs(diff) > 3:
                    # unsafe level difference
                    is_safe = False
                    reason = "unsafe level diff"

        elif levels[0] < levels[1]:
            # increasing
            for i in range(len(levels)-1):
                # check if all are increasing
                if not levels[i] < levels[i+1]:
                    # not increasing
                    is_safe = False
                    reason = "not increasing"

                # check for unsafe difference
                diff = levels[i] - levels[i+1]
                if abs(diff) > 3:
                    # unsafe level difference
                    is_safe = False
                    reason = "unsafe level diff"

        elif levels[0] == levels[1]:
            # same
            # report unsafe as not strictly increase or decrease
            is_safe = False
            reason = "not decrease or increase"

        if is_safe:
            num_safe_reports += 1
            safe_reports.append(levels)
        else:
            unsafe_reports.append(levels)

        #print(levels, is_safe, reason)

    return num_safe_reports, safe_reports, unsafe_reports


def check_safety_with_dampener(reports):
    """reactor safety systems can only tolerate levels that are either
    gradually increasing or gradually decreasing. So, a report only counts
    as safe if both of the following are true:

    -- The levels are either all increasing or all decreasing.
    -- Any two adjacent levels differ by at least one and at most three.
    -- if removing a single level from an unsafe report would make it safe,
       the report instead counts as safe
    """

    num_safe_reports = 0;

    for report in reports:
        # get levels from report
        levels = report

        # try removing each level and check
        for i in range(len(levels)):
            dampened_levels = levels.copy()
            dampened_levels.pop(i)

            is_safe = True
            reason = ""
        
            # check if levels are increasing or decreasing
            if dampened_levels[0] > dampened_levels[1]:
                # decreasing
                for i in range(len(dampened_levels)-1):
                    # check if all are decreasing
                    if not dampened_levels[i] > dampened_levels[i+1]:
                        # not decreasing
                        is_safe = False
                        reason = "not decreasing"

                    # check for unsafe difference
                    diff = dampened_levels[i] - dampened_levels[i+1]
                    if abs(diff) > 3:
                        # unsafe level difference
                        is_safe = False
                        reason = "unsafe level diff"

            elif dampened_levels[0] < dampened_levels[1]:
                # increasing
                for i in range(len(dampened_levels)-1):
                    # check if all are increasing
                    if not dampened_levels[i] < dampened_levels[i+1]:
                        # not increasing
                        is_safe = False
                        reason = "not increasing"

                    # check for unsafe difference
                    diff = dampened_levels[i] - dampened_levels[i+1]
                    if abs(diff) > 3:
                        # unsafe level difference
                        is_safe = False
                        reason = "unsafe level diff"

            elif dampened_levels[0] == dampened_levels[1]:
                # same
                # report unsafe as not strictly increase or decrease
                is_safe = False
                reason = "not decrease or increase"

            if is_safe:
                num_safe_reports += 1
                #print(dampened_levels, is_safe, reason)
                break

            #print(dampened_levels, is_safe, reason)

    return num_safe_reports


reports = get_reports("day 2/input.txt")
num_safe_reports, safe_reports, unsafe_reports = check_safety(reports)
print(num_safe_reports)

num_dampen_safe_reports = check_safety_with_dampener(unsafe_reports)
print(num_safe_reports + num_dampen_safe_reports)