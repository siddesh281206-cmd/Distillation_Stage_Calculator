# Distillation Column Stage Calculator

## Aim
To estimate the number of theoretical stages required in a distillation column using relative volatility and component compositions.

## Objective
This program calculates the approximate number of theoretical stages required for separation in a binary distillation process.

## Theory
Distillation is a separation process used in chemical engineering to separate components based on differences in volatility.

The number of theoretical stages can be estimated using the equation:

N = ln(xD / xB) / ln(α)

Where:

- N = Number of theoretical stages
- xD = Mole fraction of component in the distillate
- xB = Mole fraction of component in the bottom product
- α = Relative volatility

Relative volatility indicates how easily two components can be separated by distillation.

## Requirements

Python 3.x
No external libraries are required.

## How to Run

1. Clone the repository
2. Run the program

## Test Values

Inputs : 

- Distillate composition (xD) = 0.95
- Bottom composition (xB) = 0.05
- Relative volatility (alpha) = 2.5

Meaning :

- xD = 0.95 → distillate is 95% pure
- xB = 0.05 → bottom has 5% light component
- α = 2.5 → reasonable separation factor

Expected Output :

- Estimated theoretical stages ≈ 3.23