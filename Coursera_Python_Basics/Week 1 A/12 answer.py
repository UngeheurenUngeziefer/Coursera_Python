# Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# Программа получает на вход три числа: A, B, N — целые, неотрицательные, не превышают 10000.
A = int(input())
B = int(input())
N = int(input())

R = ((N * A) + ((N * B) // 100))
C = ((N * B) % 100)
print(str(R) + ' ' + str(C))
