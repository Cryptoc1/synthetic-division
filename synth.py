#!/usr/bin/env python

import os, sys, re, math

def main():
    exp = get_expression()
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
                
    print "\nThe following numbers are the zeros of this function:"
    print zeros
    
def build_nums(exp):
    exp = re.sub("([x\*].)", " ", exp)
    exp = exp.split()
    for i in exp:
        if i == "+":
            exp.remove(i)
    for n,i in enumerate(exp):
        exp[n] = int(i)

    return exp

def get_expression():
    return raw_input("What is the expression?\n> ")

if __name__ == "__main__":
    main()
