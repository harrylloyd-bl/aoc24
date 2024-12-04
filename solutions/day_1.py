#  Clean data
with open("..\\data\\raw\\day_1.txt", "r") as f:
    raw_lines = f.readlines()

clean_str_list = [l.strip("\n").split("   ") for l in raw_lines]
list1, list2 = sorted([int(l[0]) for l in clean_str_list]), sorted([int(l[1]) for l in clean_str_list])

# Pt 1
dist = [abs(l1 - l2) for l1, l2 in zip(list1, list2)]
total_dist = sum(dist)
print(f"Part 1: Total distance = {total_dist}")

# Pt 2
common_locs = set(list1) & set(list2)
similarity_score = 0
for loc in common_locs:
    similarity_score += list2.count(loc) * loc
print(f"Part 2: Similarity score = {similarity_score}")