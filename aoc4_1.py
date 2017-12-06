import unittest


def line_is_valid(line):
    l = list(line.split(' '))
    return False if len(l) != len(set(l)) else True


def check(data):
    result = 0
    for line in data.split('\n'):
        if line_is_valid(line):
            result += 1

    return result


class Test(unittest.TestCase):

    def test_should_be_valid1(self):
        self.assertTrue(line_is_valid('aa bb cc dd ee'))

    def test_should_be_valid2(self):
        self.assertFalse(line_is_valid('aa bb cc dd aa'))

    def test_should_be_valid3(self):
        self.assertTrue(line_is_valid('aa bb cc dd aaa'))

    def test_should_be_1(self):
        self.assertEquals(check('aa bb cc dd aaa'), 1)

    def test_should_be_2(self):
        self.assertEquals(check('aa bb cc dd aaa\naa bb cc'), 2)


if __name__ == '__main__':
    unittest.main()
