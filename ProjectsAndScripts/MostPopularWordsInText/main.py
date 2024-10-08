#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'
# __license__ = 'MIT'

"""
Prints `3` most popular words in text with length __gt__ `7`
"""

import re
import random
import requests
from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import TweetTokenizer


class TextGenerator:
    """Text generator to test the code

    """
    ONLINE_TEXT_SOURCES = [
        "https://genius.com/Halsey-control-lyrics",
    ]

    def from_url(self) -> str:
        """Returns parsed text from an online source

        """
        random.shuffle(self.ONLINE_TEXT_SOURCES)

        text = ""
        lyrics_containers = BeautifulSoup(
            markup=requests.get(
                url=self.ONLINE_TEXT_SOURCES[0]
            ).text,
            features="lxml",
        ).find_all(
            name="div",
            attrs=re.compile(r"Lyrics__Container*"),
        )

        for container in lyrics_containers:
            for line in container.find_all(
                    name="a"
            ):
                # XXX: https://stackoverflow.com/questions/30694558/beautifulsoup-split-text-in-tag-by-br
                line = line.get_text(
                    separator="\n",
                    strip=True,
                )
                text += f"{line}\n"

        return text


def main(
        text: str,
        word_length_gt: int,
        words_output_limit: int,
) -> None:
    """Prints the most popular words

    Parameters
    ----------
    text : str - input text to parse
    word_length_gt : int - filter, `word length greater than`
    words_output_limit: int - filter, most popular words to print

    Returns
    -------
    None

    Example Output
    --------------
    list[tuple[str, int]] - [('villains', 2), ('diamonds', 1), ('monsters', 1)]

    """
    token = TweetTokenizer()
    print(
        Counter(
            [word for word in token.tokenize(text) if len(word) > word_length_gt]
        ).most_common(
            n=words_output_limit
        )
    )


if __name__ == "__main__":
    WORD_LENGTH_GREATER_THAN = 7
    WORDS_OUTPUT_LIMIT = 3

    tg = TextGenerator()

    main(
        text=tg.from_url(),
        word_length_gt=WORD_LENGTH_GREATER_THAN,
        words_output_limit=WORDS_OUTPUT_LIMIT,
    )
