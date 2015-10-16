#!/usr/bin/env python

import re, sys

def main():
    exp = get_expression()
    degree = determine_degree(exp)
    n = build_nums(exp)
    zeros = []
    for c in range(-100, 100):
        t = [0]
        d = []
        for i in range(0, len(n)):
            d.append(n[i] + t[i])
            t.append(d[i] * c)
        if len(d) > 0:
            if d[len(d)-1] == 0:
                zeros.append(c)

    print "\nFound " + str(len(zeros)) + " zero(s):"
    print zeros
    if len(zeros) < degree:
        print "However, The Fundamental Theorem of Algebra states there should be " + str(degree) + " zeros."
        print "This means that at least " + str(degree - len(zeros)) + " must be complex or floating points, possibly irrational."

def build_nums(exp):
    exp = re.sub("([x\^]..)", " ", exp)
    exp = exp.split()
    for i in exp:
        if i == "+":
            exp.remove(i)
        if i == "-":
            exp[exp.index(i)+1] = str("-" + exp[exp.index(i)+1])
            exp.remove(i)
    for n,i in enumerate(exp):
        exp[n] = int(i)

    return exp

def determine_degree(exp):
    exp = exp.split()
    exponents = []
    for i in exp:
        if i == "+" or i == "-":
            exp.remove(i)
    for i in exp:
        if "x" not in i:
            exp.remove(i)
    for i in exp:
        i = re.sub(".*([x\^])", "", i)
        i = i.replace("^", "")
        if i != "":
            exponents.append(int(i))
    exponents.sort(reverse=True)
    return exponents[0]

def get_expression():
    return raw_input("What is the expression?\n> ")

if __name__ == "__main__":
    main()
