# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio

# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        port = Portfolio.from_csv(lines, **opts)
    return port
    

def read_prices(filename):
    with open(filename) as lines:
        prices = dict(parse_csv(lines,types=[str,float],has_headers=False))
                
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
    portfolio_report(*argv[1:])
    

if __name__ == '__main__':
    
    import sys
    main(sys.argv)
