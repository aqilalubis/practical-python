# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            try:
                total_cost = total_cost + (int(row[1]) * float(row[2]))
            except ValueError:
                print('Warning: Invalid data type found')
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total Cost: {cost:.2f}')
