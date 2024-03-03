# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename) as f:
        portfolio = parse_csv(f,select=['name','shares','price'],types=[str,int,float])
                
    return portfolio
    

def read_prices(filename):
    with open(filename) as f:
        prices = dict(parse_csv(f,types=[str,float],has_headers=False))
                
    return prices
        
            
def make_report(portfolio, prices):
    report = []
    
    for stock in portfolio:
        price = prices[stock['name']]
        change = price - stock['price']
        report.append((stock['name'], stock['shares'], '$' + str(price), change))
        
    return report


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' %headers)
    print(('-' * 10 + ' ') * len(headers))

    for row in report:
        print('%10s %10d %10s %10.2f' %row)          


def portfolio_report(filename1, filename2):
    portfolio = read_portfolio(filename1)
    prices = read_prices(filename2)
    print_report(make_report(portfolio, prices))
    
def main(argv):
    portfolio_report(argv[1], argv[2])
    

if __name__ == '__main__':
    import sys
    main(sys.argv)
