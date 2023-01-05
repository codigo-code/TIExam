import unittest

import datacapture


class TestDataCapture(unittest.TestCase):
    def setUp(self):
        self.capture = datacapture.DataCapture()
        self.capture.add(3)
        self.capture.add(9)
        self.capture.add(3)
        self.capture.add(4)
        self.capture.add(6)
        self.capture.add(5)
        self.capture.add(7)
        self.stats = self.capture.build_stats()
    
    def test_less(self):
        self.assertEqual(self.stats.less(3), 0)
        self.assertEqual(self.stats.less(5), 3)

    def test_greater(self):
        self.assertEqual(self.stats.higher(3), 5)
        self.assertEqual(self.stats.higher(7), 1)

    def test_between(self):
        self.assertEqual(self.stats.between(3, 6), 5)
        self.assertEqual(self.stats.between(6, 7), 2)


if __name__ == '__main__':
    unittest.main()