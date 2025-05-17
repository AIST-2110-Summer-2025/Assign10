import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from size_finder import size_finder

sentence1 = "This is a sentence that has words that have a variety of sizes"
sentence2 = "This one has a lot of words with three letters and a few with one letter"


class TestSizeFinder(unittest.TestCase):

    def _test(self, paragraph, size, exp_res):
        act_res = size_finder(paragraph, size)
        message = f"""
I called size_finder('{paragraph}', {size}).
And to get back:
{exp_res}
Instead I got back:
{act_res}
"""
        self.assertEqual(exp_res, act_res, message)

    def _test_raises(self, paragraph, size):
        try:
            size_finder(paragraph, size)
        except ValueError:
            return
        except:
            pass
        paragraph = f"'{paragraph}'" if isinstance(paragraph, str) else paragraph
        self.fail(
            f"I expected a ValueError when I called: size_finder({paragraph}, size)"
        )

    def test_one_result(self):
        self._test(sentence1, 3, ["has"])

    def test_many_results_with_caps(self):
        self._test(sentence1, 4, ["This", "that", "that", "have"])

    def test_many_results_with_caps(self):
        self._test(sentence1, 10, [])

    def test_many_results_with_duplicates(self):
        self._test(sentence2, 3, ["one", "has", "lot", "and", "few", "one"])

    def test_raise_paragraph_is_int(self):
        self._test_raises(12345, 4)

    def test_raise_paragraph_is_bool(self):
        self._test_raises(False, 5)

    def test_raise_size_is_str(self):
        self._test_raises("valid paragraph", "FIVE")

    def test_raise_size_too_low(self):
        self._test_raises("valid paragraph", 0)

    def test_raise_size_too_high(self):
        self._test_raises("valid paragraph", 20)

    def test_empty_low_bound(self):
        self._test("Valid paragraph", 1, [])

    def test_empty_high_bound(self):
        self._test("Valid paragraph", 19, [])

    def test_results_at_low_bound(self):
        self._test("A fancy sentence with a couple of one-letter words", 1, ["A", "a"])

    def test_empty_high_bound(self):
        self._test("A sentence with a big_crazy_long_word", 19, ["big_crazy_long_word"])


if __name__ == "__main__":
    unittest.main()
