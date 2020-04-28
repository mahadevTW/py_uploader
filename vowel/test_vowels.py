from unittest import TestCase

from vowel.vowels import is_vowel_line, print_file_vowels


class Test(TestCase):
    def test_is_vowel_line_false_for_some_char_vowels_and_some_consonants(self):
        line = "hi, i am mahadev"
        assert is_vowel_line(line) == False

    def test_is_vowel_line_false_empty_line(self):
        line = ""
        assert is_vowel_line(line) == False

    def test_is_vowel_line_false_null_line(self):
        line = None
        assert is_vowel_line(line) == False

    def test_is_vowel_line_true_for_all_vowels_present_in_line(self):
        line = "brown fix attempt undone"
        assert is_vowel_line(line) == True

    def test_print_file_vowels_throws_exception_if_file_not_found(self):
        self.assertRaises(Exception, print_file_vowels, "blah.txt")

    def test_print_file_vowels(self):
        from unittest.mock import patch
        from io import StringIO
        expected_output = "brown fix attempt undone\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_file_vowels("test_data/demo.txt")
            self.assertEqual(fake_out.getvalue(), expected_output)
