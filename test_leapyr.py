import unittest
import leapyr

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyr.leapYear(2000), "2000 is a leap year")

    def test2(self):
        self.assertEqual(leapyr.leapYear(2100), "2100 is not a leap year")
    
    def test3(self):
        self.assertEqual(leapyr.leapYear(2003), "2003 is not a leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)