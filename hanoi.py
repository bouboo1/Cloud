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

# n = eval(input("请输入递归层数:"))
n = 3
movement_count = move(n, 'A', 'B', 'C')
# print("总移动次数为:", movement_count)
print(movement_count)
