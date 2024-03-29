# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def get_indexes(array: list, min_a: float, max_a: float) -> list:
    indexes = []

    for i in range(len(array)):
        if min_a < array[i] < max_a:
            indexes.append(i)

    return indexes


if __name__ == '__main__':
    a = [-56, 6, 12, -45.45, 12, 34.58, -10]
    print(get_indexes(a, -3., 60.))
