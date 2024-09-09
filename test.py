import unittest


def count_vowels(s):
    """Возвращает количество гласных в строке s."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# Тесты
def test_count_vowels():
    # Тест 1: строка, содержащая только гласные
    assert count_vowels("aeiou") == 5, "Ошибка: должно быть 5 гласных в 'aeiou'"

    # Тест 2: строка без гласных
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0, "Ошибка: должно быть 0 гласных в 'bcdfghjklmnpqrstvwxyz'"

    # Тест 3: смешанная строка
    assert count_vowels("Hello, World!") == 3, "Ошибка: должно быть 3 гласные в 'Hello, World!'"

    # Тест 4: строка с прописными и строчными буквами
    assert count_vowels("Python Programming") == 4, "Ошибка: должно быть 4 гласные в 'Python Programming'"

    # Тест 5: пустая строка
    assert count_vowels("") == 0, "Ошибка: должно быть 0 гласных в пустой строке"


# Запуск тестов
if __name__ == "__main__":
    test_count_vowels()
    print("Все тесты пройдены!")