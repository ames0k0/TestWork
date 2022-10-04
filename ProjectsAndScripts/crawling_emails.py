#!/usr/bin/env python3
# coding:utf-8

import re #-------------------------#
import argparse #-------------------#
from bs4 import BeautifulSoup as bs #
from requests import get #----------#
from contextlib import suppress #---#


class UrlParser:
    __slots__ = ('url', 'unique_emails', 'email', 'urls', 'save', 'base')

    def __init__(self):
        self.url = 'http://airindia.in/contact-details.htm'
        self.unique_emails = []
        self.email = None
        self.urls = None
        self.save = None
        self.base = 'http://airindia.in'

    def parser(self):
        """Find email and urls
        """
        if self.email or self.urls:
            r = get(self.url).text
            soup = bs(r, 'lxml')

        if self.email:
            print('\nEMAILS IN URL:', self.url)
            for email in re.findall(r'[\w.-]+\@[\w.-]+', soup.text):
                if email not in self.unique_emails:
                    self.unique_emails.append(email)
                    print('   ', email)

        if self.urls:
            print('\nURLS IN URL: ', self.url)
            for links in soup.find_all('a'):
                with suppress(TypeError):
                    link = links.get('href')
                    if '/' in link and '.pdf' not in link:
                        if link.startswith('/'):
                            print('   ', f'{self.base}{link}')
                        elif 'RouteMap' in link:
                            print(f'    {self.base}/{link}')
                        else:
                            print(f'    {link}')

        if self.save and self.email:
            file_name = self.save + '.txt'
            with open(file_name, 'w') as file:
                for i in self.unique_emails:
                    file.write(i+'\n')

    def main(self):
        """Parse arguments from command line
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--e", help="print emails", type=str)
        parser.add_argument("--u", help="print urls", type=str)
        parser.add_argument("--s", help="save emails to file", type=str)
        args = parser.parse_args()
        # example: --u _ --e ema --s res, any value for arguments but 'None'

        self.email = args.e     # --e emails    NO '-- e emails.txt'
        self.urls = args.u
        self.save = args.s

        if args.e == args.u == args.s:  # if user don't know about arguments
            print('crawling_emails -h')

        self.parser()


if __name__ == "__main__":
    obj = UrlParser()
    obj.main()
