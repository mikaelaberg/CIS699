# C-4.16 Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop.

def invertString(string, index = 0):
    """Invert the string
    example: pots&pans will become snap&stop
    """

    if index == len(string)-1:
        return [string[index]]
    else:
        answer = invertString(string, index + 1)
        answer.append(string[index])
        if index == 0: 
            answer = ''.join(answer)
            print(answer)
        return answer

userInput = input('Enter your string here:')
invertString(userInput)



