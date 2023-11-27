import random
def move(n, A, B, C, count=0):
    if n == 1:
        count += 1
        # print(A, "->", C)
    else:
        count = move(n - 1, A, C, B, count)
        count += 1
        # print(A, "->", C)
        count = move(n - 1, B, A, C, count)
    return count


