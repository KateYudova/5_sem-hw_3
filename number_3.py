"""
process
"""
import os
import number_0
import time
from multiprocessing import Pool
import warnings
warnings.filterwarnings('ignore')
ls = []
number_0.srch(os.getcwd(), ls)
start = time.time()
if not len(ls):
    print ("No files in this directory")
    exit(0)
with Pool() as executor:  
    executor.map(number_0.get, ls)
print("Process: Finish in %s seconds" % (time.time() - start))
