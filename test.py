import unittest

def sum(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(0, 0), 0)

if __name__ == '__main__':
    unittest.main()