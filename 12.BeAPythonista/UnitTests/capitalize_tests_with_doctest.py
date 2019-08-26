'''
With doctest, we can write tests in a shorter way
We actually kind of embed it in the src file...

Execute it with "-v" option:
python3 capitalize_tests_with_doctest.py -v
'''


def just_do_it(text):
    """
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_do_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """

    from string import capwords
    return capwords(text)


if __name__ == "__main__":
    import doctest
    doctest.testmod()