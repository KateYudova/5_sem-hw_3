"""
process
"""
import os
import number_0
import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
import warnings
warnings.filterwarnings('ignore')
ls = []
number_0.srch(os.getcwd(), ls)
start = time.time()
if not len(ls):
    print ("No files in this directory")
    exit(0)
with ProcessPoolExecutor(max_workers=2) as pool:
    for item in ls:
        pool.submit(number_0.get, item)
print("Process: Finish in %s seconds" % (time.time() - start))
