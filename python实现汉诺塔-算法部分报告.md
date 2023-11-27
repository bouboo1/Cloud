# python实现汉诺塔-算法部分

## 代码

```py
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
n = eval(input())
movement_count = move(n, 'A', 'B', 'C')
# print("总移动次数为:", movement_count)
print(movement_count)
```

## 输入样例

> 请输入递归层数:4

## 输出样例

**这里是原始输出，由于测试需要最终只输出移动次数**

> A -> B
> A -> C
> B -> C
> A -> B
> C -> A
> C -> B
> A -> B
> A -> C
> B -> C
> B -> A
> C -> A
> B -> C
> A -> B
> A -> C
> B -> C
> 总移动次数为: 15

## 实现思路

- 定义一个递归函数`move`用于移动汉诺塔的盘子

- 函数的输入参数包括：n（表示盘子的数量），A、B、C（表示三个塔的名称），count（记录移动次数，默认值为0）。

- 当只剩下一个盘子时（即n=1），直接将盘子从A塔移动到C塔，count加1，打印移动步数

- 当n大于1时，调用函数自身move(n-1, A, C, B, count)，将n-1个盘子从A塔通过C塔移动到B塔。

- 递归地将n-1个盘子从A塔移动到B塔，返回最终count

- 将最大的盘子从A塔移动到C塔，count加1，打印移动步数

- 再次调用函数自身move(n-1, B, A, C, count)，将n-1个盘子从B塔通过A塔移动到C塔。

- 递归地将n-1个盘子从B塔移动到C塔，返回最终count

