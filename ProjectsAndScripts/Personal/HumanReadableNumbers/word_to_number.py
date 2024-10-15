#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

class RegisterNumber:
    """
    from __file__ import RegisterNumber
    rn = RegisterNumber()

    # 1065034002018 | 1 trillion 65 billion 34 million 2 thousand 18    | tr65bi34mi2th18
    # 1065034002018 | 1 trillion 65 billion 34 million 2 thousand ten 8 | tr65bi34mi2thte8

    rn.register('SECRET_KEY', 'tr65bi34mi2th18')    # REGISTER NUMBER TO KEY: SECRET_KEY
    rn.use('SECRET_KEY')                            # USE THIS KEY
    """
    __slots__ = ('nums', 'cache')

    def __init__(self):
        self.nums = {
            "te": "10",                 # ten
            "hu": "100",                # hundred
            "th": "1_000",              # thousand
            "mi": "1_000_000",          # million
            "bi": "1_000_000_000",      # billion
            "tr": "1_000_000_000_000",  # trillion
        }
        self.cache = {}

    def parse(self, msg):
        keys = []
        _int = ""
        _str = ""
        for fd in msg:
            try:
                _int += "{}".format(int(fd))
                if _str:
                    keys.append(_str)
                _str = ""
            except Exception:
                if len(_str) == 2:
                    keys.append(_str)
                    _str = fd
                else:
                    _str += fd
                if _int:
                    keys.append(int(_int))
                _int = ""
        if _int:
            keys.append(int(_int))
        if _str:
            keys.append(_str)
        hold = None
        result = 0
        for idx, key in enumerate(keys):
            if isinstance(key, int):
                if idx == (len(keys) - 1):
                    result += key
                else:
                    hold = key
            else:
                if hold:
                    result += int(str(hold) + self.nums[key][1:])
                    hold = None
                else:
                    result += int(self.nums[key])
        return result

    def register(self, key, value):
        """
        SRC:: http://mathforum.org/t2t/discuss/message.taco?thread=679&n=8
        """
        self.cache[key] = self.parse(value)

    def use(self, key):
        try:
            return self.cache[key]
        except Exception:
            return None
