import unittest
import leapyr

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyr, "2000 is not a leap year")


if __name__ == '__main__':
    unittest.main(verbosity=2)