import capitalize
from nose.tools import eq_


'''
Any function with a name matching 'test' somewhere in its name will be run
To run it:
nosetests capitalize_tests_with_nose.py
'''


def test_one_word():
    text = 'duck'
    result = capitalize.just_do_it(text)
    eq_(result, 'Duck')

def test_multiple_words():
    text = 'a veritable flock of ducks'
    result = capitalize.just_do_it(text)
    eq_(result, 'A Veritable Flock Of Ducks')


def test_words_with_apostrophes():
    text = "I'm fresh out of ideas"
    result = capitalize.just_do_it(text)
    eq_(result,"I'm Fresh Out Of Ideas")


def test_words_with_quotes():
    text = "\"You're despicable,\" said Daffy Duck"
    result = capitalize.just_do_it(text)
    eq_(result,"\"You're Despicable,\" Said Daffy Duck")