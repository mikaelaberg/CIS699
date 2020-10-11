# Write a short recursive Python function that determines if a string s is a 
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.

def display():
    """Display for user input and output of palindrome test."""

    inputString = input("Enter your string: ")
    if isPalindrome(inputString):
        print('Your string is a palindrome!')
    else: 
        print('Your string is not a palindrome.')


def isPalindrome(word):
    """Determining if a string is a palindrome or not."""

    if len(word) <= 1: 
        return True
    if word[0] == word[len(word) - 1]:
        return isPalindrome(word[1:len(word) - 1])
    else: 
        False
    
display()
