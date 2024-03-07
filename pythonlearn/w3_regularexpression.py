# author: Pongs

import re


# 1
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))


# 2
def text_match(text):
    pattern = "^a(b*)$"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(text_match("ac"))
print(text_match("abbbbbbbbbbbbb"))
print(text_match("abc"))


# 3
def text_match(text):
    pattern = "ab+?"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(text_match("ab"))
print(text_match("abbbbc"))
print(text_match("c"))


# 4
def string_match(text):
    pattern = "ab?"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(string_match("zb"))
print(string_match("ab"))


# 5
def text_match_2(text):
    pattern = "ab{3}"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(text_match_2("abbb"))


# 6
def text_match_3(text):
    pattern = "ab{2,3}"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(text_match_3("aaaabb"))
print(text_match_3("aaaaaabbbbbbb"))


# 7
def find_lower_underscore(text):
    pattern = "[a-z]+_[a-z]"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(find_lower_underscore("aab_cbbbc"))
print(find_lower_underscore("aab_Abbbc"))
print(find_lower_underscore("Aaab_abbbc"))
print(find_lower_underscore("aab_"))


# 8
def find_upper_lower(text):
    pattern = "[A-Z][a-z]"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(find_upper_lower("Ab"))
print(find_upper_lower("Abasdasd"))
print(find_upper_lower("abbbbbbbbbbbbbb"))


# 9
def match_a_end_b(text):
    pattern = "a.*b$"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(match_a_end_b("aabbbbd"))
print(match_a_end_b("aabAbbbc"))
print(match_a_end_b("accddbbjjjb"))


# 10
def match_begin(text):
    pattern = "^\w+"
    if re.search(pattern, text):
        return "Match!"
    else:
        return "Not Match!"


print(match_begin("The quick brown fox jumps over the lazy dog."))
print(match_begin(" The quick brown fox jumps over the lazy dog."))
