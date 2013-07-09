import unittest

from bowling import PointsList


class TestBowling(unittest.TestCase):

    def test_blunder(self):
        pl = PointsList([0] * 20)
        count = pl.count_points()
        self.assertEqual(count, 0)

    def test_base_example(self):
        pl = PointsList([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7,
                         3, 10, 10, 10])
        count = pl.count_points()
        self.assertEqual(count, 193)

        pl = PointsList([9, 0, 3, 5, 6, 1, 3, 6, 8, 1, 5, 3, 2, 5,
                         8, 0, 7, 1, 8, 1])
        count = pl.count_points()
        self.assertEqual(count, 82)

        pl = PointsList([9, 0, 3, 7, 6, 1, 3, 7, 8, 1, 5, 5, 0, 10,
                         8, 0, 7, 3, 8, 2, 8])
        count = pl.count_points()
        self.assertEqual(count, 131)

if __name__ == '__main__':
    unittest.main()
