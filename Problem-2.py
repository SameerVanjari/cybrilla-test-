'''
Problem 2 
Write an Algorithm to find all unique triplets in the arrays which gives the sum of zero.
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0. Solution must not
contain duplicate triplets.

Sample:
Input:
[ -1, 0, 1, 2, -1, 4]
Output:
-1, 0, 1
-1, 2, -1


'''

def find_triplets(S):
    k=0
    for i in range(len(S)-2):
        for j in range(k+1, len(S)):
            for k in range (i+1, len(S)):
                a = S[i]
                b = S[j]
                c = S[k]
                if (a+b+c==0):
                    print(a , b , c)
       
       

if __name__ == "__main__":
    S = [ -1, 0, 1, 2, -1, 4]
    find_triplets(S)