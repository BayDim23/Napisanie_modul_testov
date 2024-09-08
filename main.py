def remainder(dividend, divisor):
    """Возвращает остаток от деления dividend на divisor.

    Если divisor равен 0, выбрасывает исключение ValueError.
    """
    if divisor == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return dividend % divisor


# Тесты
def test_remainder():
    # Тест 1: обычное деление
    assert remainder(10, 3) == 1, "Ошибка: 10 % 3 должно быть 1"

    # Тест 2: деление с отрицательным делителем
    assert remainder(10, -3) == 1, "Ошибка: 10 % -3 должно быть 1"

    # Тест 3: деление с отрицательным делимым
    assert remainder(-10, 3) == 2, "Ошибка: -10 % 3 должно быть 2"

    # Тест 4: оба числа отрицательные
    assert remainder(-10, -3) == -1, "Ошибка: -10 % -3 должно быть -1"

    # Тест 5: деление на 1
    assert remainder(10, 1) == 0, "Ошибка: 10 % 1 должно быть 0"

    # Тест 6: деление на -1
    assert remainder(10, -1) == 0, "Ошибка: 10 % -1 должно быть 0"

    # Тест 7: деление на 0
    try:
        remainder(10, 0)
        assert False, "Ошибка: ожидалось исключение ValueError при делении на 0"
    except ValueError:
        pass  # Ожидаем, что исключение будет выброшено

    print("Все тесты пройдены!")


# Запуск тестов
test_remainder()