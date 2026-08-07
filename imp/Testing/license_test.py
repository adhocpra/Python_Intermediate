import unittest

def license_check(age):
    return age >=18

class TestLicense(unittest.TestCase):
    def test_license(self):
        self.assertTrue(license_check(18))

if __name__== "__main__":
    unittest.main()