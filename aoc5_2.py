import unittest


def num_instructions(s):
    l = prep(s)
    return jump(l)


def jump(l):
    index = 0
    num_steps = 0

    while index < len(l):
        instruction = l[index]

        if instruction >= 3:
            l[index] = instruction - 1
        else:
            l[index] = instruction + 1

        index = index + instruction
        num_steps += 1

    return num_steps


def prep(s):
    return [int(s) for s in s.split('\n')]


class Test(unittest.TestCase):

    def test_prep(self):
        data = "0\n3\n0\n1\n-3"

        self.assertEquals(prep(data), [0, 3, 0, 1, -3])

    def test_num_instructions(self):
        data = "0\n3\n0\n1\n-3"
        self.assertEquals(num_instructions(data), 10)


if __name__ == '__main__':
    unittest.main()
