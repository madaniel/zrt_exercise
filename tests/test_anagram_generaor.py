import pytest

from src.anagram_generator.anagram_generator_module import AnagramGenerator


@pytest.fixture(scope='module')
def anagram_generator():
    anagram_generator = AnagramGenerator(None)
    yield anagram_generator
    print("done")


def test_anagram_generator_default_config(anagram_generator):
    print("anagram generator init successfully")


def test_anagram_get_all_permutations(anagram_generator):
    actual = anagram_generator._get_all_permutations('abc')
    expected = ['abc', 'bac', 'cab', 'acb', 'bca', 'cba']
    assert set(actual).intersection(set(expected)) == set(actual)
    print("All items in the actual exist on the expected")


def test_anagram_get_all_anagrams(anagram_generator):
    actual = anagram_generator._get_all_anagrams('ace')
    expected = ['ace', 'eca', 'aec', 'cae', 'cea', 'eac']
    assert set(actual).intersection(set(expected)) == set(actual)
    print("All items in the actual exist on the expected")


def test_anagram_get_all_language_words(anagram_generator):
    actual = anagram_generator._get_all_language_words('care')
    expected = ['care', 'race', 'acre']
    assert set(actual).intersection(set(expected)) == set(actual)
    print("All items in the actual exist on the expected")





