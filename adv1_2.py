
import unittest

def calc(captcha):
    inlist = list(str(captcha))
    result = 0
    match = len(inlist) / 2

    for i, c in enumerate(inlist):
        if (i + match) < len(inlist):
            if c == inlist[i + match]:
                result += int(c)
        else:
            overflow = (i + match) - len(inlist)
            if c == inlist[overflow]:
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
