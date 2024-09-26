#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import asyncio
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from collections import defaultdict


HTTP_METHODS = [
    "GET",
    "HEAD",
    "OPTIONS",
    "TRACE",
    "PUT",
    "DELETE",
    "POST",
    "PATCH",
    "CONNECT",
]
IGNORE_ERROR_STATUS_CODE = 405


async def make_request(link: str, method: str) -> int:
    request = urllib.request.Request(link, method=method)
    try:
        with urllib.request.urlopen(request) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.status


def parse_links(data: str) -> list[str]:
    links = []
    for line in data.strip().split("\n"):
        line = line.strip()
        link = urlparse(line)
        if not all((link.scheme, link.netloc)):
            print(f'Строка "{line}" не является ссылкой.', flush=True)
            continue
        links.append(line)
    return links


def bind_link_to_methods(links: list[str]) -> list[tuple[str]]:
    bind = []
    for link in links:
        for method in HTTP_METHODS:
            bind.append((link, method))
    return bind


async def main(input_data: str) -> defaultdict:
    output_data = defaultdict(dict)
    links = parse_links(input_data)
    links_and_methods = bind_link_to_methods(links)
    for link, method in links_and_methods:
        status = await asyncio.create_task(
            make_request(link, method)
        )
        if status == IGNORE_ERROR_STATUS_CODE:
            continue
        output_data[link][method] = status
    return output_data


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("./main.py N-строк")
        exit(0)

    input_data = sys.argv[1]
    output_data = asyncio.run(
        main(input_data)
    )
    print(
        json.dumps(output_data, indent=2)
    )

