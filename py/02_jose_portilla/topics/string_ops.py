"""
   String oeprations
"""
import string

print(string.ascii_lowercase)


def is_pangram(str1, alphabet=string.ascii_lowercase):
    """
    pangram is a sentence that contains all alphabets atleast once

    Returns:
        bool: return True is the string passed is pangram else False
    """
    alphaset = set(alphabet)
    str1 = str1.replace(' ', '')
    str1_set = set(str1.lower())

    return str1_set == alphaset  # compares by value


print(is_pangram("The quick brown fox jumps over the lazy dog"))
