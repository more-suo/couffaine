cyrillic_layout = "йцукенгшщзхъ" + \
                  "фывапролджэ" + \
                  "ячсмитьбю." + \
                  "!\"№;%:?*()_+" + \
                  "ЙЦУКЕНГШЩЗХЪ" + \
                  "ФЫВАПРОЛДЖЭ" + \
                  "ЯЧСМИТЬБЮ,"

latin_layout = "qwertyuiop[]" + \
               "asdfghjkl;'" + \
               "zxcvbnm,./" + \
               "!@#$%^&*()_+" + \
               "QWERTYUIOP{}" + \
               "ASDFGHJKL:\"" + \
               "ZXCVBNM<>?"

cyrillic_to_latin = dict(zip(cyrillic_layout, latin_layout))
latin_to_cyrillic = dict(zip(latin_layout, cyrillic_layout))

print(cyrillic_to_latin)
print(latin_to_cyrillic)