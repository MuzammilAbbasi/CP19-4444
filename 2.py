s = input('Enter word : ')


def reverse(s): 
    return s[::-1]   
def isPalindrome(s):  
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False

ans = isPalindrome(s) 

if ans == 1: 
    print("The Sentence Is Palindrome") 
else: 
    print("The Sentence Is Not Palindrome")