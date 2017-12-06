
import unittest

def calc(captcha):
    inlist = list(str(captcha))
    result = 0
    offset = len(inlist) / 2

    for i, c in enumerate(inlist):
        if c == inlist[(i + offset) % len(inlist)]:
            result += int(c)
            
    return result


class Test(unittest.TestCase):

    def test_captcha_1212(self):
        self.assertEqual(calc(1212), 6)

    def test_captcha_1221(self):
        self.assertEqual(calc(1221), 0)

    def test_captcha_123425(self):
        self.assertEqual(calc(123425), 4)

    def test_captcha_123123(self):
        self.assertEqual(calc(123123), 12)

    def test_captcha_123123(self):
        self.assertEqual(calc(12131415), 4)

if __name__ == '__main__':
    unittest.main()

