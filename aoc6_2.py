import unittest

def redistribute(l):
    sel = max(l)
    sel_index = l.index(sel)
    l[sel_index] = 0

    while sel > 0:
        sel_index += 1
        l[sel_index % len(l)] = l[sel_index % len(l)] + 1
        sel -= 1

    return l


def run(l):
    result_one = loop(l)
    redistributed = result_one[0]
    result_two = loop(redistributed)

    return result_two[1]


def loop(l):
    cycles = 0
    prev_state = []
    redistributed = list(l)

    while redistributed not in prev_state:
        prev_state.append(list(redistributed))
        redistributed = redistribute(redistributed)
        cycles += 1

    return (redistributed, cycles)


def prep(s):
    return [int(s) for s in s.split('\t')]


class Test(unittest.TestCase):

    def test_redistribute(self):
        data = [0, 2, 7, 0]
        self.assertEquals(redistribute(data), [2, 4, 1, 2])

    def test_redistribute_iter(self):
        data = [0, 2, 7, 0]
        result = redistribute(data)
        self.assertEquals(result, [2, 4, 1, 2])
        result = redistribute(result)
        self.assertEquals(result, [3, 1, 2, 3])
        result = redistribute(result)
        self.assertEquals(result, [0, 2, 3, 4])
        result = redistribute(result)
        self.assertEquals(result, [1, 3, 4, 1])
        result = redistribute(result)
        self.assertEquals(result, [2, 4, 1, 2])

    def test_run_loop_size(self):
        data = [0, 2, 7, 0]
        self.assertEquals(run(data), 4)


if __name__ == '__main__':
    unittest.main()
