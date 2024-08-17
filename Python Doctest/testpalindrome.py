"""
doctest script to test palindrome.py
Siyamthanda Phakathi
PHKSIY006
11 April 2024
"""
def main():
    """"
    >>> import palindrome
    >>> palindrome.is_palindrome("")
    True
    >>> palindrome.is_palindrome("A")
    True
    >>> palindrome.is_palindrome("Dog")
    False
    >>> palindrome.is_palindrome("hannah")
    True
    >>> palindrome.is_palindrome("skies")
    False

    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()