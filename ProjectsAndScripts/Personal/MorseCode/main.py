"""
# Character from Dots and Dashes
# Delimiter as a Code stop \n|\0

# TODO
# __eq__
# __contains__

# Generate a Character and then use it to check
# - Save and Load Characters ?!
"""


class Character:
    """
    """
    __slots__: tuple[str, ...] = (
        "symbols",
    )
    def __init__(self):
        # XXX: [dot, dash, ...]
        self.symbols = []   # TODO: instance

    def __lshift__(self, other):
        raise NotImplementedError("'....' -> '...-'")

    def __add__(self, other: list):
        self.symbols.extend(other)


class Delimiter:
    """
    """
    __slots__: tuple[str, ...] = (
        "word", "sentence",
    )
    def __init__(self):
        # XXX: [char, char, ...]
        self.word = None
        # XXX: [word, word, ...]
        self.sentence = []  # TODO: instance

    def __and__(self, other):
        if self.word is None:
            self.word = Word()

        self.word + other.char

        # XXX: clear chars
        dot / dot
        dash / dash

        return self

    def __add__(self, other):
        # XXX: delimiter + delimiter -> *sentence
        if isinstance(other, Delimiter):
            self.sentence.append(self.word)
            self.word = None

        # NOTE: returning the next *other
        # *other could (and will) be a delimiter itself
        return other


class _Symbol:
    """
    Dot1[char1] -> Dash1[char1] -> ...
    """
    __slots__: tuple[str, ...] = (
        "symbol",
        "char",
    )
    SYMBOLS: dict[str, int] = {}

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.SYMBOLS[symbol] = 1
        # ...
        self.char = None

    def __mul__(self, other: int) -> list:
        """Returns `list[ContinuousSymbol] * self.count`
        """
        return [self] * other

    def __truediv__(self, _):
        """Reset `char` and `count`
        """
        self.char = None
        self.SYMBOLS[self.symbol] = 1

    def __add__(self, other):
        """Adding `ContinuousSymbol` and `Delimiter`

        Example
            dot * 3 + dash + delimiter + delimiter
        """
        if self.char is None:
            self.char = Character()
        if isinstance(other, Delimiter):
            self.char + (
                self * self.SYMBOLS[self.symbol]
            )
            # XXX: characters -> word
            other & self
        elif self is other:
            self.SYMBOLS[other.symbol] += self.SYMBOLS[self.symbol]
        else:
            self.char + (
                self * self.SYMBOLS[self.symbol]
            )
            other.char = self.char

        return other


class Dot(_Symbol):
    """
    """
    def __init__(self):
        super().__init__(symbol=".")


class Dash(_Symbol):
    """
    """
    def __init__(self):
        super().__init__(symbol="-")


class Word:
    """
    """
    __slots__: tuple[str, ...] = (
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

    #   A                        E
    s = dot + dash + delimiter + dot + delimiter + delimiter
    #   E                 T
    s + dot + delimiter + dash + delimiter + delimiter

    for word in s.sentence:
        print(word)
        for char in word.characters:
            print('\t', char)
            for sym in char.symbols:
                print('\t\t', sym)
