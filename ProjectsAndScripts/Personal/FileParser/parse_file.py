#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import re #----------------------------#
from string import ascii_letters #-----#
from random import randint, choice #---#
from os.path import exists #-----------#
from collections import Counter, deque #


"""
@args@ ->   _file   : path_to_file,
            name    : name_of_variable
            in_place: open_current_file_to_parse or find_file
            _sort   : sort words
            beautify: symbols in one line

@input@
word_list.txt:
    A
    AA
    AAAA
    ~~~~~~~

@call_func@
convert file in place word_list.txt -> word_list.py:
    from parse_file import convert_to_list
    convert_to_list(__file__, 'list_of_words', in_place=True, _sort=False)
    '''
    A
    AA
    AAAA
    ~~~~~~~
    '''

@call_func@
find file and convert:
    convert_to_list(path_to_file, 'list_of_words', in_place=False, _sort=False)


@LIST output@
# len(list_of_words) -> ??
list_of_words = [
    A, AA, AAA, ~~~~~~~
]


@DICT output@
# len(dict_of_words) -> ??
dict_of_words = {
    'A': [
        'A', 'AA', 'AAA'
    ],
    '~~~~~~~': [
        ...
    ] 
}
"""


def generate_random_words(flag, in_place=False, wlen=50):
    # http://members.optusnet.com.au/charles57/Creative/Techniques/random_words.html
    """
    @args@ ->   flag    : list, dict
                in_place: generate python file with words
                wlen    : count of random words

    python3.6 : random.choices(list_of_words, k=random.randint(1, 9))
    """
    result = ""
    may_words = "\n"
    letters = list(ascii_letters)
    for _ in range(wlen):
        for _ in range(randint(5, 9)):
            may_words += choice(letters)
        result += may_words
        may_words = "\n"

    if in_place:
        _c = """convert_to_{0}(__file__, '{0}_of_words', in_place=True)\n'''""".format(flag)
        _i = "from parse_file import convert_to_{}\n".format(flag)
        result = "{}{}{}\n'''".format(_i, _c, result)
        _file = 'word_list.py'
    else:
        _file = 'word_list.txt'

    with open(_file, 'w') as random_f:
        random_f.write(result)


def convert_to_list(_file, name="list_of_words", in_place=False, _sort=True, beautify=100):
    if exists(_file):
        # i don't know what it calls, i'll call it @baeos: begin and end of string
        baeos = ["'''", '"""']
        source = ""
        with open(_file, 'r') as _f:
            in_file = _f.readlines()

        flag = False
        for get_line in in_file:
            if in_place:
                # remove python script
                get_flag = get_line.strip()
                if not flag:
                    if get_flag in baeos:
                        flag = True
                else:
                    if get_flag not in baeos:
                        source += get_line
            else:
                source += get_line

        result = ""
        # remove symbols
        word = re.compile(r'\w+')
        words = word.findall(source)
        wlen = len(words)

        # make limit words in line
        # len('word') \ (100 symbols|beautify)
        get_minimum = str(Counter([len(w) for w in words]).most_common(3))

        # [(6, 16), (5, 12), (4, 6)] -> '(6(5(4' -> 654
        lens_of_most_common = "".join(re.findall(r'\(\d', get_minimum))[1::2]

        # ignore words with len 1
        start, _, end = [int(lens) for lens in lens_of_most_common]
        leno = end if (end - start) > start else start

        # len(", ") == 2
        line = int(beautify / (leno * 2))
        if _sort:
            words.sort()

        # [['w1', 'w2', 'w3'], ['w4', 'w5', 'w6'], ... ]
        words = deque(words)
        lines = [
            ["'{}'".format(words.popleft()) for _ in range(line)] for _ in range(int(wlen/line))
        ]

        # create list with name
        tab = "\n    "
        result += "# len({0}) -> {1}\n{0} = [{2}".format(name, wlen, tab)

        for idx, lbl in enumerate(lines):
            result += ", ".join(lbl)
            if idx < (len(lines) - 1):
                result += tab

        # add tab if list not empty
        if words:
            result += tab
        result += ", ".join(["'{}'".format(wstr) for wstr in words])
        result += "\n]"

        # rewrite file
        with open(_file, 'w') as _f:
            _f.write(result)

        print("\n[+] Parsed, open file: {}\n".format(_file))
    else:
        # generate file of words
        # False: .txt file, True: .py file
        generate_random_words('list', False)
        print("\n[!] {0}: not exists! Generated file: {0}, try again\n".format(_file))


def convert_to_dict(_file, name="list_of_words", in_place=False, _sort=True, beautify=95):
    if exists(_file):
        baeos = ["'''", '"""']
        source = ""
        with open(_file, 'r') as _f:
            in_file = _f.readlines()

        flag = False
        for get_line in in_file:
            if in_place:
                get_flag = get_line.strip()
                if not flag:
                    if get_flag in baeos:
                        flag = True
                else:
                    if get_flag not in baeos:
                        source += get_line
            else:
                source += get_line

        result = ""
        word = re.compile(r'\w+')
        words = word.findall(source)
        wlen = len(words)

        get_minimum = str(Counter([len(w) for w in words]).most_common(3))
        lens_of_most_common = "".join(re.findall(r'\(\d', get_minimum))[1::2]

        start, _, end = [int(lens) for lens in lens_of_most_common]
        if (end - start) > start:
            leno = end
        else:
            leno = start

        line = int(beautify / (leno * 2))
        keys = list(set("".join([w[0] for w in words])))
        if _sort:
            keys.sort()

        lines = []
        for key in keys:
            nword = []
            delidx = []
            for idx, w in enumerate(words[:]):
                if w[0] == key:
                    nword.append('{}'.format(w))
                    delidx.append(idx)
            delidx.sort()
            for dx in reversed(delidx):
                del words[dx]
            lines.append(nword)
        del words

        tab = "\n    "
        result += "# len({0}) -> {1}\n{0} = %s{2}".format(name, wlen, tab) % '{'

        for idx, (k, lbl) in enumerate(zip(keys, lines)):
            result += "'{}': [{}".format(k, "%s    " % tab)
            in_line = 0
            llen = len(lbl)
            while in_line < llen:
                result += ", ".join(["'{}'".format(wstr) for wstr in lbl[in_line:in_line+line]])
                in_line += line
                if in_line < llen:
                    result += "%s    " % tab
            result += "{}],".format(tab)
            if idx < len(lines) - 1:
                result += tab
        result += "\n}"

        with open(_file, 'w') as _f:
            _f.write(result)

        print("\n[+] Parsed, open file: {}\n".format(_file))
    else:
        generate_random_words('dict', False)
        print("\n[!] {0}: not exists! Generated file: {0}, try again\n".format(_file))


if __name__ == "__main__":
    pass
    # generated file (you) importing funcs, and nah need to execute it

    # convert_to_dict('word_list.txt', 'girl_names', False, True)
    # convert_to_list('word_list.txt', 'girl_names', False, True)
