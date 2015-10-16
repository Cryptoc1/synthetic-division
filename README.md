# Synthetic Division
This python script evaluates an expression and returns its zeros by using synthetic division.

Note that this program doesn't completely replace Rational Root Theorem. This is because it's only capable of identifying the **rational** zeros of a given expression.

Aslo note that due to the manner of which floating point calculations are preformed, the script only returns integers.

## Why?
I was struggling with the concept in my Algebra class, and programming always seems to help me understand mathematical procedures.

## Screens
![screenshot](screens/screenshot.png)

## Usage
I whipped this up pretty fast, so it's not super fancy. When entering the expression, terms should be separated by spaces, unless they are being subtracted, in which case, the subtraction sign should precede the term. By doing so, the term will be registered as a negative number. Exponents should be formatted as if they were being executed as a python expression, using the double asterisk notation, `x**2`. “Blank” variables should be preceded by the “invisible 1” (e.g `1x**2 + 2x`, **NOT** `x**2 + 2x`).
Example Input:

    1x**2 -2x -63 

## TODO
- [ ] Update the parser for better equation inputting options
    * Repalce `**` with `^` to denote exponents
    * Refactor logic so that "invisible" 1's and 0's don't have to be manually entered
- [ ] Print a Syntetic Division Table
- [ ] Print if some zeros are complex (Use Fundamental Law of Algebra)
- [ ] Some sort of Graph?
