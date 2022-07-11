
import math


def combinatoria(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def calculate(n_dados, y_min, k_lados=20):
    sum = 0.0
    for i in range(1, n_dados + 1):
        sum += (((k_lados - y_min) / k_lados) ** i) * ((y_min / k_lados) ** (n_dados - i)) * combinatoria(n_dados, i)
    return sum

if __name__ == '__main__':
    n_dados = int(input("insera numero de dados"))
    y_min = int(input("insera numero minimo"))
    k_lados = int(input("insera numero de lados"))
    print(calculate(n_dados,y_min,k_lados))
