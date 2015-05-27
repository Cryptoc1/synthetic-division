# Synthetic Division
This python script evaluates an expression and returns its zeros by using synthetic division.

# Why?
I was struggling with the concept in my Algebra class, and programming always seems to help me understand mathematical procedures.

# Screens
![screenshot](screens/screenshot.png)

# Usage
I whipped this up pretty fast, so it's not super fancy. When entering the expression, terms should be separated by spaces, unless they are being subtracted, in which case, the subtraction sign should precede the term. By doing so, the term will be registered as a negative number. Exponents should be formatted as if they were being executed as a python expression, using the double asterisk notation, `x**2`. “Blank” variables should be preceded by the “invisible 1” (e.g `1x**2 + 2x`, **NOT** `x**2 + 2x`).
Example Input:

    1x**2 -2x -63 
