# pcost.py
#
# Exercise 1.27

import csv
import sys
from .report import read_portfolio


def portfolio_cost(filename='Data/portfolio.csv'):
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(argv):
    print(f'Total cost {portfolio_cost(argv[1])}')
    

if __name__ == '__main__':
    import sys
    main(sys.argv)
    