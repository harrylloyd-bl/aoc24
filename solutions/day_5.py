# Clean data
with open("data\\raw\\day_5.txt", "r") as f:
    raw_lines = f.readlines()
    lines = [l.strip("\n") for l in raw_lines]

# Pt 1
rules = [l for l in lines if "|" in l]
rule_lists = [r.split("|") for r in rules]
rule_sets = [{r[0],r[1]} for r in rule_lists]

updates = [l for l in lines if "," in l]
update_lists = [u.split(",") for u in updates]

update_rules = [[ul, [rl for rs, rl in zip(rule_sets, rule_lists) if rs <= set(ul)]] for i, ul in enumerate(update_lists)]

def validate_rules(update, rules):
    for r in rules:
        if update.index(r[0]) > update.index(r[1]):
            return False
        else:
            continue
    return True

validation = [validate_rules(*ur) for ur in update_rules]
middle_values = [int(ur[0][int((len(ur[0])-1)/2)]) for ur, v in zip(update_rules, validation) if v]
print(f"Pt 1: Sum of middle values = {sum(middle_values)}")

# Pt 2
# Only previously incorrect updates
incorrect_updates = [ur for ur, v in zip(update_rules, validation) if not v] 

def create_update(rules):
    first_page = {}
    second_page = {}
    for (r0, r1) in rules:
        if r0 not in first_page:
            first_page[r0] = 1
        else:
            first_page[r0] += 1

        if r1 not in second_page:
            second_page[r1] = 1
        else:
            second_page[r1] += 1
    
    sort_fp = [[v, k] for k,v in first_page.items()]
    sort_fp.sort(key=lambda x: x[0])
    sort_sp = [[v, k] for k,v in second_page.items()]
    sort_sp.sort(key=lambda x: x[0])

    update = [x[1] for x in sort_fp[::-1]]
    update.append(sort_sp[-1][1])
    return update

corrected_updates = [create_update(iu[1]) for iu in incorrect_updates]
corrected_middle_values = [int(cu[int((len(cu)-1)/2)]) for cu in corrected_updates]
print(f"Pt 1: Sum of middle values = {sum(corrected_middle_values)}")
