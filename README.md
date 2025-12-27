# CS50 Problem Set 6 - Sentimental Cash

This repository contains my solution for the "Cash" problem from Harvard's CS50 course, reimplemented in Python. The program calculates the minimum number of coins required to give a user change.

## Files

`cash.py` : The main script that prompts the user for the amount of change owed and outputs the minimum number of coins.

## Description

The program implements a greedy algorithm to minimize the number of coins used. It behaves similarly to the C version of the problem but leverages Python's syntax and floating-point handling.

The program follows these steps:

- Input Validation: It prompts the user for the "Change owed". It utilizes a while loop to ensure the input is a non-negative floating-point number.
- Conversion: It converts the user's input (dollars) into cents (integers) to avoid floating-point imprecision errors during calculation.
- Greedy Algorithm: It sequentially subtracts the largest coin values possible from the total cents:

- - Quarters (25¢)
- - Dimes (10¢)
- - Nickels (5¢)
- - Pennies (1¢)

- Output: It prints the final count of coins used.

## Output Behavior

Input Handling: Re-prompts on negative numbers or non-numeric input.

Precision: Accurately handles converting float dollars to integer cents (e.g., $0.41 becomes 41 cents).

## Example Run

```bash
$ python cash.py
Change owed: 0.41
4
```

## How to Run

Ensure you have Python installed, then run the script directly:

```bash
python cash.py
```
