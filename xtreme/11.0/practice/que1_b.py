#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

no_of_boxes = n * m
no_of_quad_neighbours = no_of_boxes // 4
remainder = no_of_boxes % 4
if remainder:
    no_of_duo_boxes = remainder // 2
    loner = remainder % 2
    if loner:
        additional_bases = no_of_duo_boxes + 1
    else:
        additional_bases = no_of_duo_boxes
else:
    additional_bases = 0
    
no_of_bases = no_of_quad_neighbours + additional_bases

print(no_of_bases)
