# timethis.py

import time
  
def timethis(func):
    def timed_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end - start}')
    return timed_func
    