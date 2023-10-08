# Імпортуємо бібліотеку для тестування
import unittest

class TestStringFunctions(unittest.TestCase):
    
    # Тест для функції strip()
    def test_strip(self):
        self.assertEqual("   Hello, World!   ".strip(), "Hello, World!")

    # Тест для функції capitalize()
    def test_capitalize(self):
        self.assertEqual("hello world".capitalize(), "Hello world")

    # Тест для функції title()
    def test_title(self):
        self.assertEqual("hello world".title(), "Hello World")

    # Тест для функції upper()
    def test_upper(self):
        self.assertEqual("hello world".upper(), "HELLO WORLD")

    # Тест для функції lower()
    def test_lower(self):
        self.assertEqual("Hello World".lower(), "hello world")

if __name__ == '__main__':
    unittest.main()
