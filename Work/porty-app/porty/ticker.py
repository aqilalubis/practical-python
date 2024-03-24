# ticker.py
from .follow import follow
import csv
from . import report
from . import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield (row[index] for index in indices)


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
        
def parse_stock_data(lines, names):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = (row for row in rows if row['name'] in names)
    return rows


def ticker(portfile, logfile, fmt):
    portfolio =  report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile), portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        formatter.row(row.values())
        