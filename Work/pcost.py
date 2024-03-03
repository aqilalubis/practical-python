# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio


def portfolio_cost(filename='Data/portfolio.csv'):
    total_cost = 0
    portfolio = read_portfolio(filename)
    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']
    return total_cost


def main(argv):
    print(f'Total cost {portfolio_cost(argv[1])}')
    

if __name__ == '__main__':
    import sys
    main(sys.argv)
    