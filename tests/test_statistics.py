import unittest

from xlfunctions import xl, statistics


class StatisticsModuleTest(unittest.TestCase):

    def test_AVERAGE(self):
        self.assertEqual(
            statistics.AVERAGE(xl.RangeData([[1, 2],[3, 4]])), 2.5)

    def test_AVERAGE_numbers(self):
        self.assertEqual(
            statistics.AVERAGE(1, 2.0, 3, 4.0), 2.5)

    def test_AVERAGE_mixed(self):
        self.assertEqual(
            statistics.AVERAGE(xl.RangeData([[1, 2],[3, 4]]), 1, 2, 3, 4), 2.5)

    def test_COUNT(self):
        range0 = xl.RangeData([[1, 2],[3, 4]])
        range1 = xl.RangeData([[1, 2],[3, 'SPAM']])
        self.assertEqual(statistics.COUNT(range0), 4)
        self.assertEqual(statistics.COUNT(range1), 3)
        self.assertEqual(statistics.COUNT(range0, range1), 7)
        self.assertEqual(statistics.COUNT(range0, range1, 1), 8)
        self.assertEqual(statistics.COUNT(range0, range1, 1, 'SPAM'), 8)

    def test_COUNTA(self):
        range0 = xl.RangeData([[1, 2],[3, 4]])
        range1 = xl.RangeData([[2, 1],[3, '']])
        self.assertEqual(statistics.COUNTA(range0), 4)
        self.assertEqual(statistics.COUNTA(range1), 3)

    def test_COUNTA_with_bad_arg(self):
        self.assertIsInstance(statistics.COUNTA(None), xl.ValueExcelError)

    def test_MAX(self):
        self.assertEqual(statistics.MAX(xl.RangeData([[1, 2],[3, 4]])), 4)

    def test_MIN(self):
        self.assertEqual(statistics.MIN(xl.RangeData([[1, 2],[3, 4]])), 1)
