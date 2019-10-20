"""
threads
"""
import os
import time
import number_0
from concurrent.futures import ThreadPoolExecutor, as_completed
import warnings
warnings.filterwarnings('ignore')
ls = []
number_0.srch(os.getcwd(), ls)
start = time.time()
if not len(ls):
    print ("No files in this directory")
    exit(0)
with ThreadPoolExecutor(max_workers = 8) as pool:
    for item in ls:
        pool.submit(number_0.get, item)
print("Threads: Finish in %s seconds" % (time.time() - start))
