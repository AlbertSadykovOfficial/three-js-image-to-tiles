def halve_n_times(value, n):
    """
    Уменьшает значение value вдвое n раз.

    :param value: Исходное число
    :param n: Количество раз, на которое нужно уменьшить значение вдвое
    :return: Результат после n делений на 2
    """
    for _ in range(n):
        value /= 2
    return value

if __name__ == '__main__':
    # Пример использования
    result = halve_n_times(100, 3)  # 100 -> 50 -> 25 -> 12.5
    print(result)