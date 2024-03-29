# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def count_turn_over(coins: list) -> int:
    heads = 0
    for coin in coins:
        if coin == "head":
            heads += 1
    return heads if heads < len(coins) - heads else len(coins) - heads


if __name__ == '__main__':
    assert count_turn_over(["head", "head", "tail", "head", "tail", "head"]) == 2
    assert count_turn_over(["head", "head", "head", "head", "head", "head"]) == 0
    assert count_turn_over(["tail", "tail", "tail", "tail", "tail", "tail"]) == 0
