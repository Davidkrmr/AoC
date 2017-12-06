import unittest


def create_table(data):
    return [map(int, line.split()) for line in data.split('\n')]


def calc_div(l):
    result = 0
    for first in l:
        for second in l:
            if first % second == 0 and first != second:
                result = first / second
                break

    return result


def calc(data):
    result = 0
    table = create_table(data)

    return sum((calc_div(t) for t in table))


class Test(unittest.TestCase):

    def test_create_table(self):
        table = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(create_table("5 1 9 5 \n 7 5 3 \n 2 4 6 8"), table)

    def test_calc_div(self):
        table = [5, 9, 2, 8]
        self.assertEqual(calc_div(table), 4)

    def test_calc(self):
        self.assertEqual(calc("5 1 9 5 \n7 5 3 \n2 4 6 8"), 9)


if __name__ == '__main__':
    unittest.main()
