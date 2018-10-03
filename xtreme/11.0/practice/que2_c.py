#!/bin/python3

import sys

def main(a, b, x):
    ab = pow(a, b)
    if x == 0:
        return 0
    
    if ab % x == 0:
        return ab
    m1 = 0
    m2 = (ab // x) * x
    m3 = m2 + x
    d1 = abs(ab - m1)
    d2 = abs(ab - m2)
    d3 = abs(ab - m3)

    min_d = min(d1, d2, d3)
    if d1 == d2 and d2 == d3:
        return m1
    
    elif d1 == d2:
        if d1 < d3:
            return m1
        else:
            return m3
        
    elif d2 == d3:
        if d2 < d1:
            return m2
        else:
            return m3
    
    elif d1 == d3:
        if d1 < d2:
            return d1
        else:
            return d2
    else:
        if min_d == d1:
            return m1
        elif min_d == d2:
            return m2
        elif min_d2 == d3:
            return m3

    
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b, x = list(map(int, input().strip().split(' ')))
        print(main(a, b, x))
