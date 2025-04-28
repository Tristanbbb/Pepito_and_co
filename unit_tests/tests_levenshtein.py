
# Documentation : https://rapidfuzz.github.io/Levenshtein/

import Levenshtein
import unittest

class LevenshteinTest(unittest.TestCase):

    def setUp(self):
        self.base_word = "Pepito"

    def test_simple(self):
        word_to_compare = "Papito"
        res = Levenshtein.distance(self.base_word,word_to_compare)
        self.assertEqual(1,res)

    # "Pepito" and "pepito" are considered as having a Levenshtein distance of 1. We should user lower() before comparing the strings to avoid false positives.
    def test_uppercase(self):
        word_to_compare = "pepito"
        res = Levenshtein.distance(self.base_word, word_to_compare)
        self.assertEqual(1, res)




