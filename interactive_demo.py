"""
Interactive Demo — Booleans & Conditionals
Run this file to explore all solutions interactively.

Usage:
    python interactive_demo.py
"""

from solutions import (
    sign, to_smash,
    prepared_for_weather_buggy, prepared_for_weather_fixed,
    concise_is_negative,
    wants_all_toppings, wants_plain_hotdog,
    exactly_one_sauce, exactly_one_topping,
    should_hit
)

DIVIDER = "─" * 50


def section(title):
    print(f"\n{'═' * 50}")
    print(f"  {title}")
    print(f"{'═' * 50}")


def show(label, value):
    print(f"  {label:<45} → {value}")


def main():
    print("\n🐍 Kaggle Python — Booleans & Conditionals Demo")

    # ── Q1: sign ──────────────────────────────────────
    section("Q1 · sign(number)")
    for n in [-10, -0.5, 0, 3, 100]:
        show(f"sign({n})", sign(n))

    # ── Q2: to_smash ──────────────────────────────────
    section("Q2 · to_smash(total_candies)")
    for n in [1, 10, 91]:
        result = to_smash(n)
        print(f"  → Leftover: {result}")

    # ── Q3: Bug Demo ──────────────────────────────────
    section("Q3 · prepared_for_weather — Bug Demo")
    print("  Inputs: have_umbrella=False, rain_level=0, have_hood=False, is_workday=True")
    buggy  = prepared_for_weather_buggy(False, 0.0, False, True)
    fixed  = prepared_for_weather_fixed(False, 0.0, False, True)
    show("Buggy result (operator precedence bug)", buggy)
    show("Fixed result (parentheses added)      ", fixed)
    print(f"\n  Bug Explanation:")
    print("  Original:  not rain_level > 0 and is_workday")
    print("  Parsed as: (not rain_level > 0) and is_workday  ← 'not' grabs too little!")
    print("  Fixed:     not (rain_level > 0 and is_workday)  ← whole condition negated")

    # ── Q4: concise_is_negative ───────────────────────
    section("Q4 · concise_is_negative(number)")
    for n in [-7, 0, 4.2]:
        show(f"concise_is_negative({n})", concise_is_negative(n))

    # ── Q5: Hot Dog Toppings ───────────────────────────
    section("Q5 · Hot Dog Topping Functions")
    tests = [
        (True,  True,  True),
        (True,  False, True),
        (False, False, False),
        (True,  False, False),
    ]
    print(f"  {'Ketchup':<10} {'Mustard':<10} {'Onion':<10} │ All  │ Plain │ OneS.")
    print(f"  {DIVIDER}")
    for k, m, o in tests:
        all_t  = wants_all_toppings(k, m, o)
        plain  = wants_plain_hotdog(k, m, o)
        one_s  = exactly_one_sauce(k, m, o)
        print(f"  {str(k):<10} {str(m):<10} {str(o):<10} │ {str(all_t):<5}│ {str(plain):<6}│ {one_s}")

    # ── Q6: exactly_one_topping ───────────────────────
    section("Q6 · exactly_one_topping  [int(bool) trick]")
    print("  bool→int: True=1, False=0  →  sum them, check == 1")
    for k, m, o in tests:
        show(f"exactly_one_topping({k}, {m}, {o})", exactly_one_topping(k, m, o))

    # ── Q7: Blackjack ────────────────────────────────
    section("Q7 · Blackjack — should_hit Strategy")
    print(f"  {'Player':<10} {'Dealer':<10} {'Hit?'}")
    print(f"  {DIVIDER}")
    scenarios = [
        (10, 8,  0, 0),   # player 10, dealer 8 → hit
        (16, 10, 0, 0),   # player 16, dealer 10 → hit (dealer strong)
        (17, 5,  0, 0),   # player 17, dealer 5 → stand
        (12, 6,  0, 0),   # player 12, dealer 6 → stand (dealer weak)
        (11, 9,  0, 0),   # player 11, always hit
    ]
    for dt, pt, pla, pha in scenarios:
        result = should_hit(dt, pt, pla, pha)
        action = "HIT 🃏" if result else "STAND ✋"
        print(f"  Player={pt:<5}  Dealer={dt:<5}  → {action}")

    print(f"\n{'═' * 50}")
    print("  ✅  All demos complete!")
    print(f"{'═' * 50}\n")


if __name__ == "__main__":
    main()
