import sys
import time
import psutil

f = open("case5.txt","r")
lines = f.readlines()
input = []
S1 = []
S2 = []


for line in lines:
    if line.isupper():
        input.append(line.replace("\n", ""))
    else:
        line_int = int(line)
        input.append(line_int)
pointer1 = 0
pointer2 = 0

for i, item in enumerate(input):
    if type(item) is str:
        pointer2 = i
for i in range(pointer2):
    S1.append(input[i])

for i in range(pointer2, len(input)):
    S2.append(input[i])
print(S1)
print(S2)

def generate_string(X):
    if len(X[0]) == 0:
        print("Please give a valid string")
    current_string = X[0]   
    for i in range(1, len(X)):
        temp = current_string
        current_string = current_string[0:X[i] + 1] + temp + current_string[X[i] + 1:]
    return current_string

s1 = generate_string(S1)
s2 = generate_string(S2)
print(len(s2))

def Alignment_algo(x, y):
    alpha = {('A', 'A'): 0, 
         ('A', 'C'): 110, 
         ('A', 'G'): 48, 
         ('A', 'T'): 94, 
         ('C', 'A'): 110, 
         ('C', 'C'): 0, 
         ('C', 'G'): 118, 
         ('C', 'T'): 48, 
         ('G', 'A'): 48, 
         ('G', 'C'): 118, 
         ('G', 'G'): 0, 
         ('G', 'T'): 110, 
         ('T', 'A'): 94, 
         ('T', 'C'): 48, 
         ('T', 'G'): 110, 
         ('T', 'T'): 0}
    beta = 30
    m = len(x)
    n = len(y)
    array = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(m + 1):
        array[0][i] = i*beta
    for j in range(n + 1):
        array[j][0] = j*beta
    for j in range(n + 1)[1:]:
        for i in range(m + 1)[1:]:

            array[j][i] = min(alpha[(x[i - 1], y[j - 1])] + array[j - 1][i - 1], 
                         beta + array[j][i - 1], 
                         beta + array[j - 1][i])
    return array[n][m], array

def finding_pass(array, x, y):
    delta = 30
    alpha = {('A', 'A'): 0, 
         ('A', 'C'): 110, 
         ('A', 'G'): 48, 
         ('A', 'T'): 94, 
         ('C', 'A'): 110, 
         ('C', 'C'): 0, 
         ('C', 'G'): 118, 
         ('C', 'T'): 48, 
         ('G', 'A'): 48, 
         ('G', 'C'): 118, 
         ('G', 'G'): 0, 
         ('G', 'T'): 110, 
         ('T', 'A'): 94, 
         ('T', 'C'): 48, 
         ('T', 'G'): 110, 
         ('T', 'T'): 0}
    update_x = ''
    update_y = ''
    i = len(x)
    j = len(y)

    while (i, j) != (0,0):
        back_track = []
        if i == 0 or j == 0:
            back_track.append((float("inf"), "Paired"))
        else:
            different = alpha[(x[i - 1], y[j - 1])]
            pair_value = different + array[j-1][i-1]
            back_track.append((pair_value, "Paired"))
        
        if i == 0:
            back_track.append((float('inf'), "j_gap"))
        else:
            j_gap = delta + array[j][i-1]
            back_track.append((j_gap, "j_gap"))

        if j == 0:
            back_track.append((float('inf'), "i_gap"))
        else:
            i_gap = delta + array[j-1][i]
            back_track.append((i_gap, "i_gap"))
        back_track.sort()

        previous_step = back_track[0]

        if previous_step[1] == "Paired":
            update_x = x[i-1] + update_x
            update_y = y[j-1] + update_y
            i = i - 1
            j = j - 1
        elif previous_step[1] == "j_gap":
            update_x = x[i-1] + update_x
            update_y = "_" + update_y
            i = i - 1

        elif previous_step[1] == "i_gap":
            update_x = "_" + update_x
            update_y = y[j-1] + update_y
            j = j - 1

    return update_x, update_y

def output(durations, x_string, y_string, cost, memory):
    output_file = open("output.txt", "w")
    output_file.write(str(cost))
    output_file.write("\n")
    output_file.write(x_string)
    output_file.write("\n")
    output_file.write(y_string)
    output_file.write("\n")
    output_file.write(str(durations))
    output_file.write("\n")
    output_file.write(str(memory))


    output_file.close()

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

start_time = time.time()
min_cost, array = Alignment_algo(s1,s2)
x_string, y_string = finding_pass(array, s1, s2)
end_time = time.time()
duration = (end_time - start_time)*1000
memory = process_memory()

output(duration, x_string, y_string, min_cost, memory)
