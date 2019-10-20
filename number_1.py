"""
consistently
"""
import os
import time
import number_0
import warnings
warnings.filterwarnings('ignore')
ls = []
k = 0
number_0.srch(os.getcwd(), ls)
start = time.time()
if len(ls) == 0:
    print("No files in this directory")
    exit(0)
print(ls)
for i in ls:
    number_0.get(i)
    print(k)
    k += 1
print("Finish in %s seconds" % (time.time() - start))
