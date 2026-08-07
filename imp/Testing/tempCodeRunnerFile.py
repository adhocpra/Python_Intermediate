import unittest

def find_max(a,b):
    if a>b:
        return a
    return b

class testMax(unittest.TestCase):
    def test_max(self):
        self.assertGreater(find_max(6,3),3)

if "__name__"== "__main__":
    unittest.main()