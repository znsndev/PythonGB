# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

def print_powers_of_two(N: int):
    k = 1
    while 2 ** k < N:
        print(f"k = {k}\n2^k = {2 ** k}\n")
        k += 1


if __name__ == '__main__':
    print_powers_of_two(int(input("Enter N value: ")))
