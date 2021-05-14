# Instructions
# 1. Write down Python code in say() method
#    - This method might have one parameter `number` which possibly 1-99
#    - This method need to return an English word for provided number e.g. If the number is 3, should return "three"
# 2. More examples on test data (numbers and words) are in the "Test Data Example" section
# 3. How to run this file through unit tests
#    - Open the terminal
#    - Run this command "python <path/to/file.py>" e.g. python PyConUS2021Challenge.py
#    - If the tests are failed, it will display "FAILED (failures=16)" for example, on the terminal
#    - If the tests are pass, it will display "Ran 16 tests in 0.001s OK"


import unittest


class PyConUS2021Challenge():
    def say(self, number):
        # Remove `pass` and implement your own here below            
        pass


# ==================== Test Data Examples =====================
numbers_and_words = [
    (1, 'one'), 
    (2, 'two'), 
    (10, 'ten'), 
    (11, 'eleven'), 
    (12, 'twelve'),
    (13, 'thirteen'), 
    (14, 'fourteen'), 
    (15, 'fifteen'), 
    (18, 'eighteen'),
    (20, 'twenty'), 
    (21, 'twenty one'), 
    (25, 'twenty five'), 
    (30, 'thirteen'), 
    (50, 'fifty'), 
    (70, 'seventy'), 
    (99, 'ninety nine') 
]

class TestPyConUS2021Challenge(unittest.TestCase):
    pass


def test_generator(number, expected):
    def test(self):
        actual = PyConUS2021Challenge().say(number)
        self.assertEqual(actual, expected)
    return test


if __name__ == '__main__':
    for number, word in numbers_and_words:
        expected = word.replace(" ", "_")
        test_name = f'test_number_{number}_should_return_{expected}'
        test_case = test_generator(number, word)
        setattr(TestPyConUS2021Challenge, test_name, test_case)

    unittest.main()