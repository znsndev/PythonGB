# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def get_same_numbers(N: list, M: list):
    return set(N) & set(M)


def input_nums(amount: int) -> list:
    a = []
    for i in range(amount):
        a.append(int(input(f"Enter {i+1} item value: ")))
    return a


if __name__ == '__main__':
    n = input_nums(int(input("Enter amount of elements for N: ")))
    m = input_nums(int(input("Enter amount of elements for M: ")))

    print(get_same_numbers(n, m))

