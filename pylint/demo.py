#!/usr/bin/env python
import string

shift = 3
choice = "encode"
word = "Hello"
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded=encoded + letters[x]
print encoded
