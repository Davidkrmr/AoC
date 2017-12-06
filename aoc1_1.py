
import unittest


def calc(captcha):
    inlist = list(str(captcha))
    result = 0

    for i, num in enumerate(inlist):
        if num == inlist[(i + 1) % len(inlist)]:
            result += int(num)

    return result


class Test(unittest.TestCase):

    def test_captcha_1122(self):
        self.assertEqual(calc(1122), 3)

    def test_captcha_1111(self):
        self.assertEqual(calc(1111), 4)

    def test_captcha_1234(self):
        self.assertEqual(calc(1234), 0)

    def test_captcha_91212129(self):
        self.assertEqual(calc(91212129), 9)


if __name__ == '__main__':
    unittest.main()
