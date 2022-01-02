#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    
    total = len(arr)
    
    for each in arr:
        if each > 0:
            plus += 1
        elif each < 0:
            minus += 1
        else:
            zero += 1
            
    print("{:.6f}".format(plus/total))
    print("{:.6f}".format(minus/total))
    print("{:.6f}".format(zero/total))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
