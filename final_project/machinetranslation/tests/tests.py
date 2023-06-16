import unittest

import translator

class TestEnglish(unittest.TestCase):
    def test_English(self):
        self.assertEqual(translator.english_to_french("hello"), "bonjour")
        self.assertEqual(translator.english_to_french("say"), "dire")
        self.assertNotEqual(translator.english_to_french("Bye"), "Good-bye")

class TestFrench(unittest.TestCase):
    def test_French(self):
        self.assertEqual(translator.french_to_english("bonjour"), "hello")
        self.assertEqual(translator.french_to_english("dire"), "say")
        self.assertNotEqual(translator.french_to_english("Au revoir"), "Bonjour")

unittest.main()
