#!/usr/bin/python3
"""Define a text
indentation function
"""


def text_indentation(text):
    """Receives a text and then
    it prints separated text
    """
    if not isinstance(text, str):
        raise TypeError("text mmust be a string")
    no_space = 0
    for i in text:
        if no_space == 0:
            if i == " ":
                continue
            else:
                no_space = 1
        if no_space == 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                no_space = 0
            else:
                print(i, end="")
