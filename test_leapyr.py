import unittest
import leapyr

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyr.leapYear(2000), "2000 is a leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)