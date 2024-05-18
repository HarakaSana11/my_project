import unittest
from my_module.operations import do_add

class TestDoAdd(unittest.TestCase):
    
    def test_valid_input(self):
        self.assertEqual(do_add(None, '4 5'), 9)
        self.assertEqual(do_add(None, '10 20'), 30)
        self.assertEqual(do_add(None, '0 0'), 0)
        self.assertEqual(do_add(None, '-1 -2'), -3)

    def test_invalid_number_of_arguments(self):
        self.assertIsNone(do_add(None, '4'))
        self.assertIsNone(do_add(None, '4 5 6'))
        self.assertIsNone(do_add(None, ''))

    def test_non_numeric_input(self):
        self.assertIsNone(do_add(None, 'four five'))
        self.assertIsNone(do_add(None, '4 five'))
        self.assertIsNone(do_add(None, 'five 5'))

    def test_edge_cases(self):
        self.assertEqual(do_add(None, '2147483647 1'), 2147483648)
        self.assertEqual(do_add(None, '-2147483648 -1'), -2147483649)
        self.assertIsNone(do_add(None, '   '))

if __name__ == '__main__':
    unittest.main()