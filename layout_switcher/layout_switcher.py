# -*- coding: utf-8 -*-

cyrillic_layout = """
            йцукенгшщзхъ\
            фывапролджэ
            ячсмитьбю.
            ЙЦУКЕНГШЩЗХЪ/
            ФЫВАПРОЛДЖЭ
            ЯЧСМИТЬБЮ,
            Ё!"№;%:?*()_+
            ё1234567890-=
            """

latin_layout = """
            qwertyuiop[]\
            asdfghjkl;'
            zxcvbnm,./
            QWERTYUIOP{}|
            ASDFGHJKL:"
            ZXCVBNM<>?
            ~!@#$%^&*()_+
            `1234567890-=
            """

cyrillic_to_latin = dict(zip(cyrillic_layout, latin_layout))
latin_to_cyrillic = dict(zip(latin_layout, cyrillic_layout))


def translate_layout(s, dictionary):
    result = ''
    for char in s:
        try:
            translated_char = dictionary[char]
        except KeyError:
            translated_char = char
        result += translated_char
    return result


def translate_to_cyrillic(s):
    return translate_layout(s, latin_to_cyrillic)


def translate_to_latin(s):
    return translate_layout(s, cyrillic_to_latin)
