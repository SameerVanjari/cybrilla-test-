'''
problem 3 
Write a program to find if a string is a palindrome. Print true if the string is a palindrome and print false if it is
not.

'''

def palindrome(s):
    normal = s
    reverse = s[::-1]
    if normal == reverse:
        print("true")
    else: print("false")

if __name__== "__main__":
    s ='anna'
    palindrome(s)
