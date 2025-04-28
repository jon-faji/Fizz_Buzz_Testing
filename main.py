import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
    
    def test_divisible_by_3(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
    
    def test_divisible_by_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

if __name__ == '__main__':
    unittest.main(exit=False)

    
    try:
        n = int(input("Enter a number for FizzBuzz: "))
        print(fizzbuzz(n))
    except ValueError:
        print("Please enter a valid integer.")