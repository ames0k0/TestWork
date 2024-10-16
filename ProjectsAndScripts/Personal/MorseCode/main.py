"""

# Character from Dots and Dashes
# Delimiter as a Code stop \n|\0

# TODO
# __mul__
# __add__
# __eq__
# __contains__

# Generate a Character and then use it to check
# - Save and Load Characters ?!

"""

class Character:
    __slots__ = (
        "symbols",
    )
    def __init__(self):
        self.symbols = []

    # TODO: '....' -> '...-'
    # def __lshift__(self, other):
    #     print('Catch:', other)
    #     self.symbols.append(other)
    #     return self

    def __add__(self, other: list):
        # dot, (dot, dot, ...)
        self.symbols.extend(other)


class Dot:
    __slots__ = (
        "char",
        "symbol", "count"
    )
    def __init__(self):
        self.char = None
        self.symbol = "."
        self.count = 1

    def __mul__(self, other) -> list:
        # (dot, dot, ...)
        a = [
            self for _ in range(other)
        ]
        return a

    def __truediv__(self, other):
        self.char = None
        self.count = 1

    def __add__(self, other):
        # TODO: catching a *delimiter
        # XXX: delimiter
        # XXX: dot * 4 + delimiter + dot * 4 + delimiter
        # dot, dash - character
        # delimiter - word, sentence

        # XXX: init character
        if self.char is None:
            self.char = Character()

        # XXX: same symbol
        if self is other:
            # dot2 + dot2
            other.count += self.count
            # dot2
            return other

        if isinstance(other, Dash):
            # dot2 + dash
            self.char + (self * self.count)
            # maybe create a character in *other
            other.char = self.char
            # dash
            return other

        # got *dash
        if isinstance(other, Delimiter):
            # delimiter
            self.char + (self * self.count)
            return other & self

        raise NotImplementedError("Not Itself, Dot or Delimiter!", self)


class Dash:
    __slots__ = (
        "char",
        "symbol", "count"
    )
    def __init__(self):
        self.char = None
        self.symbol = "-"
        self.count = 1

    def __mul__(self, other) -> list:
        # (dot, dot, ...)
        a = [
            self for _ in range(other)
        ]
        return a

    def __truediv__(self, other):
        self.char = None
        self.count = 1

    def __add__(self, other):
        # TODO: catching a *delimiter
        # XXX: delimiter
        # XXX: dot * 4 + delimiter + dot * 4 + delimiter
        # dot, dash - character
        # delimiter - word, sentence

        # XXX: init character
        if self.char is None:
            self.char = Character()

        # XXX: same symbol
        if self is other:
            # dot2 + dot2
            other.count += self.count
            # dot2
            return other

        if isinstance(other, Dot):
            # dot2 + dash
            self.char + (self * self.count)
            # maybe create a character in *other
            other.char = self.char
            # dash
            return other

        # got *dash
        if isinstance(other, Delimiter):
            # delimiter
            self.char + (self * self.count)
            return other & self

        raise NotImplementedError("Not Itself, Dot or Delimiter!", self)


class Delimiter:
    __slots__ = (
        "word", "sentence",
    )
    def __init__(self):
        # [char, char, ...]
        # TODO: instance ?
        self.word = None
        # XXX: [word, word, ...]
        self.sentence = []

    def __and__(self, other):
        # delimiter + delimiter -> space -> word
        # .... + delimiter -> char
        # if self.word:
        #     # delimiter + delimiter => [[]]
        #     self.sentence.append(word)
        #     self.word.clear()
        if self.word is None:
            self.word = Word()

        self.word + other.char

        # XXX: clear chars
        dot / 0
        dash / 0

        # self.sentence.append()
        #     print('!!!', self.sentence)
        return self

    def __add__(self, other):
        # XXX: word is read, so it will go to a *sentence
        if isinstance(other, Delimiter):
            # self -> delimiter1
            # other -> delimiter2
            self.sentence.append(self.word)
            self.word = None

        # NOTE: returning the next *other
        # *other could be delimiter itself
        return other


class Word:
    __slots__ = (
        "characters",
    )
    def __init__(self):
        self.characters = []
    def __add__(self, other):
        self.characters.append(other)


class Sentence: pass

if __name__ == "__main__":
    dot = Dot()
    dash = Dash()

    # NOTE: single instance for all words / sentence
    delimiter = Delimiter()

    # char = Character()
    # word = Word()
    sentence = Sentence()

    # A = Char + Dot + Dash
    # Word +
    # A = delimiter + delimiter
    # A = dot + dash + dash # + delimiter()

    #   A                        E
    s = dot + dash + delimiter + dot + delimiter + delimiter
    #   E                 T
    s + dot + delimiter + dash + delimiter + delimiter

    # print('@@@', s)
    # print(s.word, '::', s.sentence)
    for word in s.sentence:
        print('!', word)
        for char in word.characters:
            print('\t>', char)
            for sym in char.symbols:
                print('\t\t>', sym)
