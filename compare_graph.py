from cProfile import label
from posixpath import split
import matplotlib.pyplot as plt
b_t = []
b_m = []
p_s = []
e_t = []
e_m = []
with open("basic.txt", "r") as f:

    count = 0
    lines = f.readlines()
    for line in lines:
        splits = line.split(" ")
        if count == 0:
            for a in splits:
                b_t.append(a)
        elif count == 1:
            for a in splits:
                b_m.append(a)
        elif count == 2:
            for a in splits:
                p_s.append(a)
        count += 1
b_m = b_m[:-1]
b_t = b_t[:-1]
p_s = p_s[:-1]
with open("efficient.txt", "r") as f:

    count = 0
    lines = f.readlines()
    for line in lines:
        splits = line.split(" ")
        if count == 0:
            for a in splits:
                e_t.append(a)
        elif count == 1:
            for a in splits:
                e_m.append(a)

        count += 1
e_m = e_m[:-1]
e_t = e_t[:-1]
problem_size = [int(x) for x in p_s]

efficient_time = [float(x) for x in e_t]
efficient_mem = [int(x) for x in e_m]
basic_mem = [int(x) for x in b_m]
basic_time = [float(x) for x in b_t]
plt.plot(problem_size, basic_mem, label="basic")
plt.plot(problem_size, efficient_mem, label="efficient")
plt.xlabel("Problem_size (M + N)")
plt.ylabel("Memory_usage (KB)")
plt.title("Problem_Size vs Memory")

plt.legend()
plt.show()


plt.plot(problem_size, basic_time, label="basic")
plt.plot(problem_size, efficient_time, label="efficient")
plt.xlabel("Problem_size (M + N)")
plt.ylabel("Time (ms)")
plt.title("Problem_Size vs Time")

plt.legend()
plt.show()