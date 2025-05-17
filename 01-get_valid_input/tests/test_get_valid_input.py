from io import StringIO
import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from get_valid_input import get_valid_input


class TestGetValidInput(unittest.TestCase):

    def test_uses_prompt(self):
        with patch("builtins.input") as mock_input:
            test_prompt = "Go Jags!"
            mock_input.side_effect = ["a"]
            get_valid_input(test_prompt, ["a", "b"])
            try:
                mock_input.assert_called_once_with(test_prompt)
            except:
                self.fail(
                    f"""
get_valid_input does not appear to use the prompt passed in to it.
Did you call input(prompt)??"""
                )

    def _get_valid_input(self, valid_vals, inputs, exp_out, exp_val):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = inputs
            captured_output = StringIO()
            sys.stdout = captured_output
            act_val = get_valid_input("", valid_vals)
            sys.stdout = sys.__stdout__
            act_out = captured_output.getvalue().strip().splitlines()
            message = f'''
I called get_valid_input('A prompt:', {valid_vals}).
I typed in:
{'\n'.join(inputs)}
I expected to see:
{'\n'.join(exp_out)}
And to get back the value: {exp_val}
I saw:
{'\n'.join(act_out)}
and got back: {act_val}
'''
            self.assertEqual(exp_val, act_val, message)
            for i in range(len(exp_out)):
                if i < len(act_out):
                    exp = exp_out[i].lower()
                    act = act_out[i].lower()
                    self.assertIn(exp, act, message)

    def test_first_try_first_val_all_lower(self):
        self._get_valid_input(["beef", "pork", "chicken"], ["beef"], [], "beef")

    def test_first_try_first_val_all_lower_strips_input(self):
        self._get_valid_input(["beef", "pork", "chicken"], ["  beef  "], [], "beef")

    def test_first_try_first_val_uppder_input(self):
        self._get_valid_input(["beef", "pork", "chicken"], ["BEEF"], [], "beef")

    def test_first_try_first_val_uppder_choices(self):
        self._get_valid_input(["BEEF", "PORK", "CHICKEN"], ["beef"], [], "beef")

    def test_first_try_first_all_uppder_returns_lower(self):
        self._get_valid_input(["BEEF", "PORK", "CHICKEN"], ["BEEF"], [], "beef")

    def test_first_try_last_val_uppder_input(self):
        self._get_valid_input(["beef", "pork", "chicken"], ["CHICKEN"], [], "chicken")

    def test_first_try_first_all_uppder_returns_lower(self):
        self._get_valid_input(["BEEF", "PORK", "CHICKEN"], ["CHICKEN"], [], "chicken")

    def test_second_try_first_val_all_lower(self):
        self._get_valid_input(
            ["beef", "pork", "chicken"], ["tofu", "beef"], ["INVALID INPUT"], "beef"
        )

    def test_second_try_first_val_uppder_input(self):
        self._get_valid_input(
            ["beef", "pork", "chicken"], ["tofu", "BEEF"], ["INVALID INPUT"], "beef"
        )

    def test_third_try_last_val_all_lower(self):
        self._get_valid_input(
            ["beef", "pork", "chicken"],
            ["tofu", "tofurkey", "chicken"],
            ["INVALID INPUT", "INVALID INPUT"],
            "chicken",
        )


if __name__ == "__main__":
    unittest.main()
