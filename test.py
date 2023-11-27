import unittest
from hanoi import move

class HanoiTestCase(unittest.TestCase):
    def test_hanoi(self):
        self.assertEqual(move(1, 'A', 'B', 'C'), 1)
        self.assertEqual(move(2, 'A', 'B', 'C'), 3)
        self.assertEqual(move(3, 'A', 'B', 'C'), 7)

if __name__ == '__main__':
    unittest.main()