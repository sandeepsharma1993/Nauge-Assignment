import unittest

from nau1 import driver,encode 


class TestEncode(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = 'Hello world!'
        result = encode(data)
        print(result)
        self.assertEqual(result, 'Svool dliow!')

if __name__ == '__main__':
    unittest.main()

