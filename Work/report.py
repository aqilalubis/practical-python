# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        portfolio = parse_csv(f,select=['name','shares','price'],types=[str,int,float])
    portfolio = [Stock(p['name'], p['shares'], p['price']) for p in portfolio]
    return Portfolio(portfolio)
    

def read_prices(filename):
    with open(filename) as f:
        prices = dict(parse_csv(f,types=[str,float],has_headers=False))
                
    return prices
        
            
def make_report_data(portfolio, prices):
    report = []
    
    for stock in portfolio:
        price = prices[stock.name]
        change = price - stock.price
        report.append((stock.name, stock.shares, price, change))
        
    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)         


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

    
    
def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])
    

if __name__ == '__main__':
    import sys
    main(sys.argv)
