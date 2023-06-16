'''This module is for the final IBM Python project 
   It contains two methods that translate english to french and viseversa
'''
from deep_translator import MyMemoryTranslator as mmt


def english_to_french(english_text):
    '''Takes in an English string. Returns a French string.'''
    french_text = mmt(source="en", target="fr").translate(english_text)

    return french_text


def french_to_english(french_text):
    '''Takes in a French string. Retrurns an English string.'''
    english_text = mmt(source="fr", target="en").translate(french_text)

    return english_text
