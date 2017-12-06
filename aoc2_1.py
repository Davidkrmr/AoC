import unittest


def create_table(data):
    return [map(int, line.split()) for line in data.split('\n')]


def calc_diff(l):
    return max(l) - min(l)


def calc(data):
    result = 0
    table = create_table(data)

    return sum((calc_diff(t) for t in table))


class Test(unittest.TestCase):

    def test_create_table(self):
        table = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(create_table("5 1 9 5\n7 5 3\n2 4 6 8"), table)

    def test_calculate_diff(self):
        table = [5, 1, 9, 5]
        self.assertEqual(calc_diff(table), 8)

    def test_calculate(self):
        self.assertEqual(calc("5 1 9 5\n7 5 3\n2 4 6 8"), 18)


if __name__ == '__main__':
    unittest.main()
