import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 8]), 10)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -8]), -5)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 5, -8]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.6, 3.7]), 3.7)
        self.assertEqual(max_integer([-1.5, -2.6, -3.7]), -1.5)
        self.assertEqual(max_integer([-1.5, 2.6, -3.7]), 2.6)

    def test_strings(self):
        self.assertEqual(max_integer(['apple', 'banana', 'orange']), 'orange')
        self.assertEqual(max_integer(['cat', 'dog', 'elephant']), 'elephant')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'apple', 3, 4])


if __name__ == '__main__':
    unittest.main()
