import unittest

def line_is_valid(line):
    l = list(line.split(' '))

    for word1 in l:
        for word2 in l:
            if word1 != word2 and sorted(word1) == sorted(word2):
                return False
    
    return True

def line_is_valid_duplicate(line):
    l = list(line.split(' '))
    return False if len(l) != len(set(l)) else True


def check(input):
    result = 0
    for line in input.split('\n'):
        if line_is_valid(line) and line_is_valid_duplicate(line):
            result += 1
            
    return result


class Test(unittest.TestCase):

    def test_should_be_valid1(self):
        self.assertTrue(line_is_valid('abcde fghij'))
    
    def test_should_be_valid2(self):
        self.assertTrue(line_is_valid('iiii oiii ooii oooi oooo'))
    
    def test_should_be_valid3(self):
        self.assertTrue(line_is_valid('a ab abc abd abf abj'))

    def test_should_not_be_valid(self):
        self.assertFalse(line_is_valid('oiii ioii iioi iiio'))

    def test_should_not_be_valid2(self):
        self.assertFalse(line_is_valid('abcde xyz ecdab'))

    def test_should_be_1(self):
        self.assertEquals(check('aa bb cc dd aaa'), 1)
    
    def test_should_be_2(self):
        self.assertEquals(check('aa bb cc dd aaa\naa bb cc'), 2)

if __name__ == '__main__':
    unittest.main()