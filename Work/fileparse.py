# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(rows, select=[], types=[], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse an iterable object into a list of records
    '''
    
    if type(rows) == str:
        raise TypeError('Iterator must be given, not file name')
    rows = [row.strip().split(delimiter) for row in rows if row.strip()]
    if has_headers:
        headers = rows[0]
        rows = rows[1:]
        
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
        
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
        
    records = []
    for i, row in enumerate(rows, 1):
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val.strip('"')) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f'Row {i}: Couldn\'t convert {row}')
                    log.debug(f'Row {i}: Reason {e}')
                continue
                
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
            
    return records
    