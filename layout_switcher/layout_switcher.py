# -*- coding: utf-8 -*-

cyrillic_layout = "йцукенгшщзхъ" + \
                  "фывапролджэ" + \
                  "ячсмитьбю." + \
                  "!\"№;%:?*()_+" + \
                  "ЙЦУКЕНГШЩЗХЪ" + \
                  "ФЫВАПРОЛДЖЭ" + \
                  "ЯЧСМИТЬБЮ, " + \
                  "1234567890-="

latin_layout = "qwertyuiop[]" + \
               "asdfghjkl;'" + \
               "zxcvbnm,./" + \
               "!@#$%^&*()_+" + \
               "QWERTYUIOP{}" + \
               "ASDFGHJKL:\"" + \
               "ZXCVBNM<>? " + \
               "1234567890-="

cyrillic_to_latin = dict(zip(cyrillic_layout, latin_layout))
latin_to_cyrillic = dict(zip(latin_layout, cyrillic_layout))

x = input()
y = []

for ch in x:
    y.append(cyrillic_to_latin[ch])

print(''.join(y))
