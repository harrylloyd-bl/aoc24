import re

# Clean data
with open("data\\raw\\day_4.txt", "r") as f:
    raw_lines = f.readlines()
    lines = [l.strip("\n") for l in raw_lines]

# Pt 1
h_lines = lines.copy()
v_lines = ["".join([l[i] for l in lines]) for i, _ in enumerate(lines)]

d_lines_rl_down = ["".join([l[::-1][i-j] for i, l in enumerate(lines) if i-j>=0]) for j in range(len(lines))]
d_lines_rl_up = ["".join([l[::-1][i+j] for i, l in enumerate(lines) if i+j<=139]) for j in range(1,len(lines))]
d_lines_rl = d_lines_rl_down + d_lines_rl_up

d_lines_lr_down = ["".join([l[i-j] for i, l in enumerate(lines) if i-j>=0]) for j in range(len(lines))]
d_lines_lr_up = ["".join([l[i+j] for i, l in enumerate(lines) if i+j<=139]) for j in range(1,len(lines))]
d_lines_lr = d_lines_lr_down + d_lines_lr_up

xmas_p = re.compile("XMAS")
samx_p = re.compile("SAMX")

line_sets = [h_lines, v_lines, d_lines_lr, d_lines_rl]
counts = [sum([sum([len(xmas_p.findall(l)), len(samx_p.findall(l))]) for l in lines]) for lines in line_sets]
print(f"Pt 1: Total XMAS = {sum(counts)}")

# Pt 2
numeric_lines = [l.replace("M", "1").replace("S", "2").replace("A", "5").replace("X", "7") for l in lines]

def extract_x_mas(r1, r2, r3):
    count = 0
    if len(r1) != len(r2) != len(r3):
        raise ValueError("Row lengths aren't the same")
    for i, letter in enumerate(r2[1:-1]):
        if letter == "5":
            trace_lr = sum([int(r1[i]), int(r3[i+2])])
            trace_rl = sum([int(r1[i+2]), int(r3[i])])
            count += (trace_lr == 3) and (trace_rl == 3)
    
    return count

x_mas_lines = [extract_x_mas(tr, mr, br) for tr, mr, br in zip(numeric_lines[:-2], numeric_lines[1:-1], numeric_lines[2:])]
print(f"Pt 2: Total XMAS = {sum(x_mas_lines)}")
