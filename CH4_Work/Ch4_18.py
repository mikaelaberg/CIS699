# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.

vowel = {'a', 'e', 'i', 'o', 'u'}

def vowelCounter(string, index = 0):
    """Counter to determine if the string provided has more vowels than consonants"""

    a = -1 if string[index] in vowel else 1
    if index == len(string) -1:
        return a
    else:
        return (a + vowelCounter(string, index + 1))

def vowelTester(string):
    """Testing the string for vowels and constants"""

    ans = vowelCounter(string)
    if ans > 0:
        return (f"Your string has more consonants by {ans}")
    elif ans < 0: 
        return (f"Your string has more vowels by {ans}")
    else:
        (f"Your string has equal number of vowels and consonants by {ans}")


stringList = [(input('Enter your string here: '))]
for string in stringList:
    print(vowelTester(string), string)
