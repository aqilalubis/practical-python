# bounce.py
#
# Exercise 1.5

n = 0
height = 100  # meters
while n < 10:
    n = n + 1
    height = 0.6 * height
    print(n, round(height, 4))
    
