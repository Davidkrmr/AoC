
import unittest

def calc(captcha):
    inlist = list(str(captcha))
    result = 0

    for i, c in enumerate(inlist):
        if c == inlist[(i + 1) % len(inlist)]:
            result += int(c)

    return result

class Test(unittest.TestCase):

    def setUp(self):
        pass

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
