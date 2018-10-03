import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

no_of_boxes = n * m
no_of_quad_neighbours = no_of_boxes // 4

remainder = no_of_boxes % 4

if remainder < 3:
    if remainder != 0:
        additional_supplies = 1
    else:
        additional_supplies = 0
else:
    additional_supplies = 2

supplies_required = no_of_quad_neighbours + additional_supplies
print(supplies_required)
