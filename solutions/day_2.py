#  Clean data
with open("..\\data\\raw\\day_2.txt", "r") as f:
    raw_lines = f.readlines()

reports = [[int(r) for r in l.strip("\n").split(" ")] for l in raw_lines]

# Pt 1
def classify_report(report: list, problem_damper: bool=False) -> bool:
    if problem_damper:
        for i, _ in enumerate(report):
            copy = report.copy()
            copy.pop(i)
            if classify_report(copy, problem_damper=False):
                return True
        else:
            return False
        
    rate_of_change = [i - j for i,j in zip(report[:-1], report[1:])]
    mod_roc = [abs(r) for r in rate_of_change]

    if min(mod_roc) < 1 or max(mod_roc) > 3:
        return False
    elif sum(mod_roc) != abs(sum(rate_of_change)):
        return False
    else:
        return True
    
classified_reports = [classify_report(r) for r in reports]
print(f"Part 1: Number of safe reports = {sum(classified_reports)}")

# Pt 2
# Modified classify_report to have a problem_handler section
problem_damped_reports = [classify_report(r, problem_damper=True) for r in reports]
print(f"Part 2: Number of safe reports inc problem handling = {sum(problem_damped_reports)}")
