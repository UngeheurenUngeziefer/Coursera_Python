# По данному целому числу N распечатайте все квадраты натуральных чисел,не превосходящие N,
# в порядке возрастания.

N = int(input())
X = 0

while X**2 <= N - X:
    X = X + 1
    print(X**2, end=' ')
