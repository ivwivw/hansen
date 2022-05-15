import unittest
import programmingtask


class TestType(unittest.TestCase):

    def setUp(self):
        self.letters = "STS"
        self.numbers = [3, 2]
        self.args = 3

    def test_check_number_of_args(self):
        """Assert of arguments passed is at least 3 take into account filename.py is 0 in argv"""
        self.assertFalse(programmingtask.valid_number_of_args(0))
        self.assertFalse(programmingtask.valid_number_of_args(1))
        self.assertFalse(programmingtask.valid_number_of_args(2))
        self.assertTrue(programmingtask.valid_number_of_args(3))

    def test_end_part(self):
        """test End part combinations """
        self.assertEqual(programmingtask.end_part('S', 'T'), "Soft and Tough.")
        self.assertEqual(programmingtask.end_part('S', 'S'), "Soft and Soft.")
        self.assertEqual(programmingtask.end_part('T', 'T'), "Tough and Tough.")
        self.assertEqual(programmingtask.end_part('T', 'S'), "Tough and Soft.")

    def test_parse_letter_arg(self):
        self.assertEqual(programmingtask.parse_letters_args('STTS'), ['S', 'T', 'T', 'S'])

    def test_validate_number_arg(self):
        with self.assertRaises(ValueError):
            programmingtask.validate_number_args(['33', 'a', '3'])

    # def test_start_part(self):
    #     self.assertEqual(programmingtask.start_part(1, "SST", [3, 2]), "Soft, Soft, Tough,")
