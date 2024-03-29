# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


def arithmetic_progression(a_first: float, n: int, d: float) -> list:
    a = [a_first]
    for i in range(2, n + 1, 1):
        a.append(a_first + (i - 1) * d)

    return a


if __name__ == '__main__':
    progression = arithmetic_progression(float(input("Enter the 1st element value: ")),
                                         int(input("Enter amount of elements: ")),
                                         float(input("Enter the d value: ")))
    print(progression)
