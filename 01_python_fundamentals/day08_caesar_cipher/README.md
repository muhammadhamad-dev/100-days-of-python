# Day 08 — Caesar Cipher

An encryption and decryption tool based on the Caesar Cipher algorithm.
Supports any shift value and handles non-alphabetic characters gracefully.

## Concepts Practiced
- Functions with parameters
- Modulo operator for alphabet wrap-around
- `while` loops for program restart
- Handling edge cases (numbers, spaces, symbols)

## Files
| File | Purpose |
|------|---------|
| `main.py` | Cipher logic and user interface |
| `art.py` | ASCII logo |

## How to Run
```bash
python main.py
```

## Example
```
Direction: encode
Message: hello world
Shift: 3
→ khoor zruog

Direction: decode
Message: khoor zruog
Shift: 3
→ hello world
```