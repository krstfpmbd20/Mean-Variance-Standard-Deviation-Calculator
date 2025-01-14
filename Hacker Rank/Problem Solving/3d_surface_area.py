#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def _count_cube(A, i, j):
    count=2
    count+=max(A[i][j]- (A[i-1][j] if i>0 else 0), 0)
    count+=max(A[i][j]- (A[i][j-1] if j>0 else 0), 0)
    count+=max(A[i][j]- (A[i+1][j] if i<len(A)-1 else 0), 0)
    count+=max(A[i][j]- (A[i][j+1] if j<len(A[i])-1 else 0), 0)
    
    return count
    

def surfaceArea(A):
    count=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            count+=_count_cube(A, i, j)
    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
