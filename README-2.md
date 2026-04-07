# 🐍 Python Booleans & Conditionals — Kaggle Exercise Solutions

> Solutions, explanations, and an interactive demo for the **Kaggle Python Course — Exercise 3: Booleans and Conditionals**.

---

## 📁 Project Structure

```
python-booleans-conditionals/
├── solutions.py          # All 7 solved functions with docstrings
├── interactive_demo.py   # CLI demo — run to see all outputs
├── tests/
│   └── test_solutions.py # 23 unit tests (unittest)
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/python-booleans-conditionals.git
cd python-booleans-conditionals

# Run the interactive demo
python interactive_demo.py

# Run all tests
python -m unittest discover tests/ -v
```

---

## 📝 Questions & Solutions

### Q1 — `sign(number)`
Implements the mathematical sign function without any built-in.

```python
def sign(number):
    if number > 0:   return 1
    elif number < 0: return -1
    else:            return 0
```

---

### Q2 — `to_smash(total_candies)` — Grammar Fix
Prints **"candy"** for 1, **"candies"** for anything else.

```python
word = "candy" if total_candies == 1 else "candies"
print(f"Splitting {total_candies} {word}")
```

---

### Q3 — Operator Precedence Bug 🐛
The original function had a subtle Python operator precedence bug.

```python
# BUGGY — 'not' only applies to 'rain_level > 0'
return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# FIXED — explicit parentheses clarify intent
return have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)
```

**Rule:** In Python, operator precedence is: `not` > `and` > `or`. Always use parentheses for clarity in complex boolean expressions.

---

### Q4 — `concise_is_negative` — One-liner
```python
def concise_is_negative(number):
    return number < 0   # comparison already returns bool!
```

---

### Q5 — Hot Dog Topping Functions

| Function | Logic |
|---|---|
| `wants_all_toppings` | `ketchup and mustard and onion` |
| `wants_plain_hotdog` | `not ketchup and not mustard and not onion` |
| `exactly_one_sauce` | XOR: `(k or m) and not (k and m)` |

---

### Q6 — `exactly_one_topping` — bool→int Trick
```python
def exactly_one_topping(ketchup, mustard, onion):
    return int(ketchup) + int(mustard) + int(onion) == 1
```
**Trick:** `bool` is a subclass of `int` in Python → `True == 1`, `False == 0`.

---

### Q7 — Blackjack `should_hit` — Basic Strategy
```python
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_total < 12:                          return True   # no bust risk
    if 12 <= player_total <= 16 and dealer_total >= 7: return True   # dealer is strong
    return False                                               # stand
```

---

## ✅ Test Results

```
Ran 23 tests in 0.002s — OK
```

All 23 unit tests pass covering edge cases for every function.

---

## 💡 Key Concepts Covered

- Boolean operators: `and`, `or`, `not`
- Operator precedence and why parentheses matter
- Ternary expressions: `x if condition else y`
- Python's `bool` ↔ `int` conversion
- Writing concise, readable boolean functions
- Basic Blackjack strategy implementation

---

## 📚 Reference

- [Kaggle Python Course](https://www.kaggle.com/learn/python)
- [Python Docs — Boolean Operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)

---

## 📄 License

MIT License — free to use for learning purposes.
