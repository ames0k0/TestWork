#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

import sys
import fileinput
from re import findall
from os import isatty


# sources:
# https://stackoverflow.com/questions/
#     11109859/pipe-output-from-shell-command-to-a-python-script/11109920
#     4429966/how-to-make-a-python-script-pipeable-in-bash
#     30686701/python-get-size-of-string-in-bytes
#     35247817/is-there-a-way-for-a-python-script-to-know-if-it-is-being-piped-to
# http://www.gnu.org/software/cflow/manual/html_node/Source-of-wc-command.html
# https://docs.python.org/3/library/exceptions.html#OSError


class WordCounter:
    """
    1. -l считает количество строк
    $ cat /etc/passwd| wc  -l
    46
    2. -w считает количество слов
    $ cat /etc/passwd| wc -w
    62
    3. -c считает количество байт
    $ cat /etc/passwd| wc -c
    2381
    4. запуск без аргументов
    $ cat /etc/passwd| wc
    46      62    2381
    """
    __slots__ = (
        'pipes',
    )

    def __init__(self, pipes):
        self.pipes = pipes

    @classmethod
    def h_func(cls):
        """Help function

        - вывод справочной информации
        """
        key, middle = r'\d\.\s+', "\n"
        messg = "$ cat tfile.txt | ./wc.py <option>\n$ ./wc.py <file> <option>"
        delim = findall(key, cls.__doc__)

        lines = [
            line for line in cls.__doc__.split('\n') if findall(key, line)
        ]

        result = middle.join(
            [val.split(delim[idx])[-1] for idx, val in enumerate(lines[:-1])]
        )

        return f"\n{messg}{middle*2}{result}\n"

    def l_func(self):
        """Line Counter
        """
        return len(self.pipes)

    def w_func(self):
        """Word Counter
        """
        return len("".join(self.pipes).split())

    def c_func(self):
        """Byte Counter
        """
        return sum([len(each.encode('utf-8')) for each in self.pipes])

    def gen_output(self):
        """Run without arguments
        """
        yield self.l_func()
        yield self.w_func()
        yield self.c_func()


def main():
    """Get pipes and call functions
    """
    try:
        # - возможность считывать как stdin, так и fileinput
        if not isatty(0):
            wc = WordCounter([line for line in sys.stdin])
        else:
            wc = WordCounter([line for line in fileinput.input(sys.argv[1])])
    except (IndexError, FileNotFoundError):
        # handle errors when script executed like: ./wc.py, ./wc.py <option>
        wc = WordCounter([None])
        sys.exit(wc.h_func())

    for arg in ['-l', '-w', '-c', '-h']:
        if arg in sys.argv:
            print(wc.__getattribute__(f'{arg[-1]}_func')())
            break
    else:
        template = "{:>6}"*3
        print(template.format(*[funcs for funcs in wc.gen_output()]))


if __name__ == '__main__':
    main()
