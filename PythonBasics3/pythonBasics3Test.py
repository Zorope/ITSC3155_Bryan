import unittest
import pythonBasics3


class TestPythonBasicsOne(unittest.TestCase):

#Test case for starts_with_non_number
    def test_starts_with_non_number(self):

        self.assertEqual(pythonBasics3.starts_with_non_number("Once upon a time, I was 18"), True)

        self.assertEqual(pythonBasics3.starts_with_non_number("5 weekdays each week"), False)

        self.assertEqual(pythonBasics3.starts_with_non_number("-5 is what I got on my quiz"), True)

        self.assertEqual(pythonBasics3.starts_with_non_number(" 1 more meal left in the fridge"), True)

        self.assertEqual(pythonBasics3.starts_with_non_number("# is used to comment a line in Python"), True)

        # Please add three more test cases following the order above

#Test case for multiple_words
    def test_multiple_words(self):

        self.assertEqual(pythonBasics3.multiple_words("That's 10/10"), True)

        self.assertEqual(pythonBasics3.multiple_words(" "), False)

        self.assertEqual(pythonBasics3.multiple_words("Different\\twhitespace"), False)

        self.assertEqual(pythonBasics3.multiple_words("It's-all-one-word"), False)

        self.assertEqual(pythonBasics3.multiple_words(" one-sided? "), False)

        # Please add three more test cases following the order above


#Test case for reserved_us_tld
    def test_reserved_us_tld(self):

        self.assertEqual(pythonBasics3.reserved_us_tld("http://www.whitehouse.gov"), False)

        self.assertEqual(pythonBasics3.reserved_us_tld("https://www.charlotte.edu"), True)

        self.assertEqual(pythonBasics3.reserved_us_tld("https://uncc.instructure.com"), False)

        self.assertEqual(pythonBasics3.reserved_us_tld("https://www.education.com"), False)

        self.assertEqual(pythonBasics3.reserved_us_tld("https://www.norad.mil"), True)

        self.assertEqual(pythonBasics3.reserved_us_tld("https://www.congress.gov"), True)

        # This does match the description (https and .edu) but it includes extra stuff. Feel free to implement this functionality.
        self.assertEqual(pythonBasics3.reserved_us_tld("https://selfservice.uncc.edu/pls/BANPROD/twbkwbis.P_GenMenu?name=homepage"), False)



if __name__ == '__main__':

  unittest.main(verbosity=1)
