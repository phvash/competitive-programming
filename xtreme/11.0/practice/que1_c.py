#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

def twos_solution(n):
    return n // 2 + n % 2

def is_even(n):
    return True if n % 2 == 0 else False

if n > m:
    l = n
    s = m
else:
    l = m
    s = n

a1 = l // 2
if is_even(l):
    r1 = 0
else:
    r1 = 1

t1 = a1 + r1

if s < 2:
    t = t1
else:
    m = s // 2
    t1 = m * t1
    
    if is_even(s):
        t = t1
    else:
        w = 1 * l
        t2 = twos_solution(w)
        t = t1 + t2
        
print(t)
