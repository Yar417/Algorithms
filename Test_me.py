x, y = 1000, 1000
A = [x, y]
steps = 1


def move(arg):
    arg[1] += 1
    return arg


def count_coord(arg):
    x = arg[0]
    y = arg[1]
    max = 0
    for i in str(x):
        max += int(i)
    for j in str(y):
        max += int(j)
    return max <= 25


while A[0] <= 1023:
    if count_coord(move(A)):
        steps += 1
    else:
        A[0] += 1
        A[1] = 1000
print(steps)
