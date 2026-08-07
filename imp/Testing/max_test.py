import unittest

def find_max(a,b):
    if a>b:
        return a
    else:
         return b

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertGreater(find_max(6,3),3)

if __name__ == "__main__":
    unittest.main()