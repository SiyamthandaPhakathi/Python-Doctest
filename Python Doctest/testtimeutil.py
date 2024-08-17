"""
doctest script to test timeutil.py
Siyamthanda Phakathi
PHKSIY006
11 April 2024
"""
def main():
    """"
    >>> import timeutil
    >>> timeutil.validate(":00 a.m.")
    False
    >>> timeutil.validate("hh:00 a.m.")
    False
    >>> timeutil.validate("08:00 a.m.")
    False
    >>> timeutil.validate("1:00 z.k.")
    False
    >>> timeutil.validate("10:kk a.m.")
    False
    >>> timeutil.validate("10:40 a.m.")
    True

    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()