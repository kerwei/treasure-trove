def is_palindrome(text):
    """
    Checks if a given string is a palindrome. Returns a boolean
    """
    n = len(text)

    if n % 2 == 0:
        return text[:(n//2)] == text[n-1:(n//2)-1:-1]
    else:
        return text[:n//2] == text[n-1:(n//2):-1]

def longpal(text):
    """
    Looks for the longest available palindrome in a string
    """
    for i in range(len(text)):
        for j in range(i+1):
            if is_palindrome(text[j:len(text)-i]):
                return text[j:len(text)-i]

    return None


if __name__ == '__main__':
    text = 'bbaaaabb'
    print(longpal(text))