import unittest
from testing import legend

class TestLegend(unittest.TestCase):

    def test_normal(self):
        #Нормальные данные
        self.assertAlmostEqual(legend(2, 4, 6), 1.0)

    def test_zero_division(self):
        #Деление на ноль
        with self.assertRaises(ZeroDivisionError):
            legend(3, 3, 10)

    def test_negative_log(self):
        #Ошибка логарифма
        with self.assertRaises(ValueError):
            legend(5, 2, 4)

    def test_string_input(self):
        # Проверка на ValueError, если попытаться дать строку вместо числа
        with self.assertRaises(TypeError):
            legend("буквы", 4, 6)

if __name__ == '__main__':
    unittest.main()
