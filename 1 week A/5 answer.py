# N школьников поделили K яблок поровну, не делящийся остаток остался в корзинке.
# Сколько яблок осталось в корзинке?
# Программа получает на вход числа N и K — натуральные, не превышают 10000.
N = input()
K = input()
print((int(K) % int(N)))
