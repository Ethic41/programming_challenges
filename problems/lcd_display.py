# Author: Dahir Muhammad Dahir
# Date: 24th-05-2019 01:57 AM
# About: some note here


eight = {"a1": " ", 'a2': "-", 'a3': " ", 'b1': "|", 'b2': " ", 'b3': "|", 'c1': " ", 'c2': "-", 'c3': " ", 'd1': "|",
         'd2': " ", 'd3': "|", 'e1': " ", 'e2': "-", 'e3': " "}

num = "88"

n = 2
a_list = ""
b_list = ""
c_list = ""
d_list = ""
e_list = ""

num_mapping = {"8": eight}

for digit in num:
    d = num_mapping[digit]
    print(d["a1"] + (d["a2"] * n) + d["a3"], end="")
print("\n", end="")
for digit in num:
    d = num_mapping[digit]
    print(d["b1"] + d["b2"]*n + d["b3"], end="")
print("\n", end="")
for digit in num:
    d = num_mapping[digit]
    print(d["c1"] + d["c2"]*n + d["c3"], end="")
"""
    print(a_list)
    for i in range(n):
        b_list += d["b1"] + d["b2"]*n + d["b3"] + "\n"
    print(b_list)
    c_list += d["c1"] + d["c2"]*n + d["c3"]
    print(c_list)
    for i in range(n):
        d_list += d["d1"] + d["d2"]*n + d["d3"] + "\n"
    print(d_list)
    e_list += d["e1"] + d["e2"]*n + d["e3"]
    print(e_list)
"""