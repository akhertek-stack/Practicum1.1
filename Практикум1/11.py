import math

r_inner = float(input())
r_outer = float(input())

area = math.pi * (r_outer**2 - r_inner**2)

print(area)