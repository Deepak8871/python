"""
Kaggle Python Course — Exercise 3: Booleans & Conditionals
Solutions by: [Your Name]

Topics covered:
- Boolean logic (and, or, not)
- Conditional expressions (if/elif/else)
- Python operator precedence
- Ternary / one-liner expressions
- int() and bool() type conversions
"""


# ─────────────────────────────────────────────
# Q1. Sign Function
# ─────────────────────────────────────────────

def sign(number):
    """
    Returns the sign of a number:
      -1 if negative, 1 if positive, 0 if zero.

    Examples:
        >>> sign(-5)
        -1
        >>> sign(0)
        0
        >>> sign(3.7)
        1
    """
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


# ─────────────────────────────────────────────
# Q2. Grammar-Aware Candy Smasher
# ─────────────────────────────────────────────

def to_smash(total_candies):
    """
    Returns the number of leftover candies after distributing
    evenly among 3 friends. Also prints a grammatically correct
    message (candy vs candies).

    Examples:
        >>> to_smash(91)
        Splitting 91 candies
        1
        >>> to_smash(1)
        Splitting 1 candy
        1
    """
    word = "candy" if total_candies == 1 else "candies"
    print(f"Splitting {total_candies} {word}")
    return total_candies % 3


# ─────────────────────────────────────────────
# Q3. Buggy Weather Checker (Bug Demonstrated)
# ─────────────────────────────────────────────

def prepared_for_weather_buggy(have_umbrella, rain_level, have_hood, is_workday):
    """
    BUGGY version — has operator precedence issue.
    'not' only applies to 'rain_level > 0', not the whole last condition.

    Bug demo: have_umbrella=False, rain_level=0.0, have_hood=False, is_workday=True
    Expected: False (not raining, not a workday issue)
    Returns:  True  (incorrectly, because 'not rain_level > 0' = True, then 'and is_workday' = True)
    """
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday


def prepared_for_weather_fixed(have_umbrella, rain_level, have_hood, is_workday):
    """
    FIXED version — uses explicit parentheses for clarity.

    Logic:
      - Safe if I have an umbrella, OR
      - Rain isn't heavy AND I have a hood, OR
      - It's NOT (raining AND a workday)
    """
    return have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)


# ─────────────────────────────────────────────
# Q4. Concise is_negative
# ─────────────────────────────────────────────

def is_negative(number):
    """Verbose version (original)."""
    if number < 0:
        return True
    else:
        return False


def concise_is_negative(number):
    """
    One-liner version — returns the boolean comparison directly.

    Examples:
        >>> concise_is_negative(-3)
        True
        >>> concise_is_negative(5)
        False
    """
    return number < 0


# ─────────────────────────────────────────────
# Q5. Hot Dog Topping Functions
# ─────────────────────────────────────────────

def onionless(ketchup, mustard, onion):
    """Returns True if customer does NOT want onion."""
    return not onion


def wants_all_toppings(ketchup, mustard, onion):
    """
    Returns True if customer wants ALL three toppings.

    Examples:
        >>> wants_all_toppings(True, True, True)
        True
        >>> wants_all_toppings(True, False, True)
        False
    """
    return ketchup and mustard and onion


def wants_plain_hotdog(ketchup, mustard, onion):
    """
    Returns True if customer wants NO toppings.

    Examples:
        >>> wants_plain_hotdog(False, False, False)
        True
        >>> wants_plain_hotdog(True, False, False)
        False
    """
    return not ketchup and not mustard and not onion


def exactly_one_sauce(ketchup, mustard, onion):
    """
    Returns True if customer wants ketchup XOR mustard (but not both).
    'onion' is irrelevant to this check.

    Examples:
        >>> exactly_one_sauce(True, False, True)
        True
        >>> exactly_one_sauce(True, True, False)
        False
    """
    return (ketchup or mustard) and not (ketchup and mustard)


# ─────────────────────────────────────────────
# Q6. Exactly One Topping (int + bool trick)
# ─────────────────────────────────────────────

def exactly_one_topping(ketchup, mustard, onion):
    """
    Returns True if customer wants exactly ONE of the three toppings.

    Trick: bool → int conversion: True=1, False=0
    So we can sum them and check if total == 1.

    Examples:
        >>> exactly_one_topping(True, False, False)
        True
        >>> exactly_one_topping(True, True, False)
        False
        >>> exactly_one_topping(False, False, False)
        False
    """
    return int(ketchup) + int(mustard) + int(onion) == 1


# ─────────────────────────────────────────────
# Q7. Blackjack — Smart should_hit Strategy
# ─────────────────────────────────────────────

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """
    Returns True if the player should hit (take another card).

    Strategy (simplified Basic Strategy):
    - Always hit if player_total < 12 (no bust risk)
    - Hit if player_total is 12–16 AND dealer shows 7+ (dealer is strong)
    - Stand otherwise (17+ always stand)

    Args:
        dealer_total      : Dealer's visible card total
        player_total      : Player's current best total (≤21)
        player_low_aces   : Number of aces counted as 1
        player_high_aces  : Number of aces counted as 11

    Returns:
        bool: True = Hit, False = Stand
    """
    if player_total < 12:
        return True
    if 12 <= player_total <= 16 and dealer_total >= 7:
        return True
    return False
