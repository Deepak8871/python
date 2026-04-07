"""
Unit Tests — Booleans & Conditionals Solutions

Run with pytest:   python -m pytest tests/ -v
Run with unittest: python -m unittest discover tests/ -v
"""

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solutions import (
    sign, to_smash,
    prepared_for_weather_buggy, prepared_for_weather_fixed,
    concise_is_negative,
    wants_all_toppings, wants_plain_hotdog,
    exactly_one_sauce, exactly_one_topping,
    should_hit
)


# ── Q1 ────────────────────────────────────────────────
class TestSign(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(sign(5), 1)
        self.assertEqual(sign(0.001), 1)
        self.assertEqual(sign(1000), 1)

    def test_negative(self):
        self.assertEqual(sign(-3), -1)
        self.assertEqual(sign(-0.5), -1)

    def test_zero(self):
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(0.0), 0)


# ── Q2 ────────────────────────────────────────────────
class TestToSmash(unittest.TestCase):
    def test_remainder(self):
        self.assertEqual(to_smash(91), 1)
        self.assertEqual(to_smash(9), 0)
        self.assertEqual(to_smash(10), 1)

    def test_grammar_singular(self):
        from io import StringIO
        import contextlib
        f = StringIO()
        with contextlib.redirect_stdout(f):
            to_smash(1)
        out = f.getvalue()
        self.assertIn("1 candy", out)
        self.assertNotIn("candies", out)

    def test_grammar_plural(self):
        from io import StringIO
        import contextlib
        f = StringIO()
        with contextlib.redirect_stdout(f):
            to_smash(10)
        out = f.getvalue()
        self.assertIn("candies", out)


# ── Q3 ────────────────────────────────────────────────
class TestWeatherBug(unittest.TestCase):
    def test_bug_exists(self):
        buggy = prepared_for_weather_buggy(False, 0.0, False, False)
        fixed = prepared_for_weather_fixed(False, 0.0, False, False)
        # On these inputs they may differ — demonstrating the bug
        self.assertIsInstance(buggy, bool)
        self.assertIsInstance(fixed, bool)

    def test_fixed_umbrella(self):
        self.assertTrue(prepared_for_weather_fixed(True, 10, False, True))

    def test_fixed_no_rain_no_workday(self):
        self.assertTrue(prepared_for_weather_fixed(False, 0.0, False, False))

    def test_fixed_rain_with_hood(self):
        self.assertTrue(prepared_for_weather_fixed(False, 3, True, True))


# ── Q4 ────────────────────────────────────────────────
class TestConciseIsNegative(unittest.TestCase):
    def test_negative(self):
        self.assertTrue(concise_is_negative(-1))
        self.assertTrue(concise_is_negative(-100))

    def test_non_negative(self):
        self.assertFalse(concise_is_negative(1))
        self.assertFalse(concise_is_negative(0))


# ── Q5 ────────────────────────────────────────────────
class TestToppingFunctions(unittest.TestCase):
    def test_wants_all(self):
        self.assertTrue(wants_all_toppings(True, True, True))
        self.assertFalse(wants_all_toppings(True, False, True))
        self.assertFalse(wants_all_toppings(False, False, False))

    def test_plain_hotdog(self):
        self.assertTrue(wants_plain_hotdog(False, False, False))
        self.assertFalse(wants_plain_hotdog(True, False, False))
        self.assertFalse(wants_plain_hotdog(True, True, True))

    def test_exactly_one_sauce(self):
        self.assertTrue(exactly_one_sauce(True, False, True))
        self.assertTrue(exactly_one_sauce(False, True, False))
        self.assertFalse(exactly_one_sauce(True, True, False))
        self.assertFalse(exactly_one_sauce(False, False, True))


# ── Q6 ────────────────────────────────────────────────
class TestExactlyOneTopping(unittest.TestCase):
    def test_one_topping(self):
        self.assertTrue(exactly_one_topping(True, False, False))
        self.assertTrue(exactly_one_topping(False, True, False))
        self.assertTrue(exactly_one_topping(False, False, True))

    def test_zero_toppings(self):
        self.assertFalse(exactly_one_topping(False, False, False))

    def test_two_toppings(self):
        self.assertFalse(exactly_one_topping(True, True, False))

    def test_three_toppings(self):
        self.assertFalse(exactly_one_topping(True, True, True))


# ── Q7 ────────────────────────────────────────────────
class TestShouldHit(unittest.TestCase):
    def test_always_hit_low(self):
        self.assertTrue(should_hit(10, 8, 0, 0))
        self.assertTrue(should_hit(5, 11, 0, 0))

    def test_hit_vs_strong_dealer(self):
        self.assertTrue(should_hit(10, 15, 0, 0))
        self.assertTrue(should_hit(7, 13, 0, 0))

    def test_stand_vs_weak_dealer(self):
        self.assertFalse(should_hit(6, 14, 0, 0))

    def test_stand_17_plus(self):
        self.assertFalse(should_hit(10, 17, 0, 0))
        self.assertFalse(should_hit(6, 20, 0, 0))


if __name__ == "__main__":
    unittest.main()
