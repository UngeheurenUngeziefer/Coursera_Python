# Дано действительное положительное число a и целое неотрицательное число n. Вычислите aⁿ,
# не используя циклы и стандартную функцию pow, но используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).

a = float(input())
n = float(input())

r = a * (a ** (n - 1))


def power(a, n):
    print(r)


power(a, n)