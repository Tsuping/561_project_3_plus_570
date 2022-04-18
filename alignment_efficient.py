


f = open("case.txt","r")
lines = f.readlines()


def find_string(lines):
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
    return S1, S2

def generate_string(X):
    if len(X[0]) == 0:
        print("Please give a valid string")
    current_string = X[0]
    for i in range(1, len(X)):
        temp = current_string
        current_string = current_string[0:X[i] + 1] + temp + current_string[X[i] + 1:]
    return current_string

x, y = find_string(lines)
x_string = generate_string(x)
y_string = generate_string(y)
print(x_string)