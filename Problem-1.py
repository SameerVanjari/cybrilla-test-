'''
Problem 1 
You are given an array A of N integers. You want to choose some integers from the array subject to the
condition that the number of distinct integers chosen should not exceed K. Your task is to maximize the sum
of chosen numbers.

Sample 1:
Input:
4 1
3 -1 2 5

Output:
5


'''
from typing import Mapping


def func1(K,A):
    A = A.sort()
    res = 0
    for i in range(K):
        res += int(A[::-1][i])

    return res 

if __name__ =="__main__":
    A = [3, -1,2, 5]
    K= 1
    