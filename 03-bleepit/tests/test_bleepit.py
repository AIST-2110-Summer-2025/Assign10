from io import StringIO
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bleepit import bleepit


sentence1 = "Some naughty folks say naughty words if they speak too fast to some people"
sentence2 = "An elephant named Bobo said hi Bob to his best buddy Robert the mouse"


class TestBleepit(unittest.TestCase):

    def _test(self, text, bleeps, exp_out, exp_val):
        captured_output = StringIO()
        sys.stdout = captured_output
        act_val = bleepit(text, bleeps)
        sys.stdout = sys.__stdout__
        act_out = captured_output.getvalue().strip()
        message = f"""
I called bleeper('{text}', {bleeps}).
I expected to see:
{exp_out}
And to get back the value: {exp_val}
I saw:
{act_out}
and got back: {act_val}
"""
        self.assertEqual(exp_val, act_val, message)
        self.assertEqual(exp_out, act_out, message)

    def test_one_bleep(self):
        self._test(
            sentence1,
            ["naughty"],
            "Some ******* folks say ******* words if they speak too fast to some people",
            2,
        )

    def test_no_bleeps(self):
        self._test(
            sentence1,
            [],
            "Some naughty folks say naughty words if they speak too fast to some people",
            0,
        )

    def test_two_bleeps(self):
        self._test(
            sentence1,
            ["naughty", "to"],
            "Some ******* folks say ******* words if they speak too fast ** some people",
            3,
        )

    def test_two_bleeps_caps(self):
        self._test(
            sentence1,
            ["naughty", "some"],
            "**** ******* folks say ******* words if they speak too fast to **** people",
            4,
        )

    def test_one_bleep_no_results(self):
        self._test(
            sentence2,
            ["bart"],
            "An elephant named Bobo said hi Bob to his best buddy Robert the mouse",
            0,
        )

    def test_four_bleep_no_results(self):
        self._test(
            sentence2,
            ["bart", "lisa", "homer", "marge"],
            "An elephant named Bobo said hi Bob to his best buddy Robert the mouse",
            0,
        )

    def test_four_bleep_one_results(self):
        self._test(
            sentence2,
            ["bart", "lisa", "homer", "buddy"],
            "An elephant named Bobo said hi Bob to his best ***** Robert the mouse",
            1,
        )

    def test_two_bleep_caps(self):
        self._test(
            sentence2,
            ["bob", "robert"],
            "An elephant named Bobo said hi *** to his best buddy ****** the mouse",
            2,
        )

    def test_bleep_last_word(self):
        self._test(
            sentence2,
            ["mouse"],
            "An elephant named Bobo said hi Bob to his best buddy Robert the *****",
            1,
        )


if __name__ == "__main__":
    unittest.main()
