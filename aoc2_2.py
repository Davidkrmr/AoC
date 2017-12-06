import unittest


def create_table(data):
    table = []
    for line in data.split('\n'):
        l = map(int, line.split())
        table.append(l)
    return table


def calc_div(l):
    for first in l:
        for second in l:
            if first % second == 0 and first != second:
                return first / second


def calc(data):
    result = 0
    table = create_table(data)

    for t in table:
        result += calc_div(t)

    return result


class Test(unittest.TestCase):

    def test_create_table(self):
        table = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(create_table("5 1 9 5\n7 5 3\n2 4 6 8"), table)

    def test_calc_div(self):
        table = [5, 9, 2, 8]
        self.assertEqual(calc_div(table), 4)


if __name__ == '__main__':
    unittest.main()
