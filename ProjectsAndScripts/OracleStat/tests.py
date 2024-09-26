import asyncio

from main import (
    parse_links, bind_link_to_methods,
    make_request, main
)


def test_get_links():
    assert parse_links("") == []


def test_bind_link_to_methods():
    assert bind_link_to_methods([]) == []


def test_make_requests():
    assert asyncio.run(make_request("https://ya.ru", "GET")) == 200

