"""
doctest script to test numberutil.py
Siyamthanda Phakathi
PHKSIY006
11 April 2024
"""
""""
paths:
    hundreds > 0 no remainder *
    hundred < 0 and 0 < remainder < 21 *
    hundreds > 0 and 0 > remainder > 21*
    hundreds > 0 and remainder > 21 and units > 0 *
    hundreds > 0 and remainder > 21 and units = 0 *
    hundreds < 0 and remainder > 21
    hundreds = 0 and remainder = 0*
    
"""
def main():
    """"
    >>> import numberutil
    >>> numberutil.aswords(200)
    'two hundred'
    >>> numberutil.aswords(17)
    'seventeen'
    >>> numberutil.aswords(201)
    'two hundred and one'
    >>> numberutil.aswords(0)
    'zero'
    >>> numberutil.aswords(224)
    'two hundred and twenty four'
    >>> numberutil.aswords(330)
    'three hundred and thirty'
    >>> numberutil.aswords(30)
    'thirty'
    >>> numberutil.aswords(31)
    'thirty one'

    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()