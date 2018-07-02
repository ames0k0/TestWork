#!/usr/bin/env python3
# coding:utf-8

import argparse
import re
from bs4 import BeautifulSoup as bs
from requests import get


class UrlParser():

    def __init__(self):
        self.url = 'http://airindia.in/contact-details.htm'
        self.unique_emails = []
        self.email = None
        self.urls = None
        self.save = None

    def parser(self):
        """
        Find email and urls
        """
        if self.email or self.urls:         # if user wanna do requests for a site
            r = get(self.url).text
            soup = bs(r, 'lxml')

        if self.email:                      # if we need to find only emails
            print('\nEMAILS IN URL: ', self.url)
            k = re.findall(r'[\w.-]+\@[\w.-]+', soup.text)
            for email in k:
                if email not in self.unique_emails:
                    self.unique_emails.append(email)
                    print('    ', email)

        if self.urls:                       # if we need to find urls in site
            print('\nURLS IN URL: ', self.url)
            for links in soup.find_all('a'):
                try:
                    link = links.get('href')
                    if '/' in link and '.pdf' not in link:
                        if link.startswith('/'):                # link: /index.html
                            sw = f'http://airindia.in{link}'    # full link: http://airindia.in/index.html
                            print('    ', sw)
                        elif 'RouteMap' in link:
                            print(f'     http://airindia.in/{link}')
                        else:
                            print(f'    {link}')                # print all links
                except:
                    pass

        if self.save and self.email:        # save emails if was command for parse emails
            file_name = self.save + '.txt'
            with open(file_name, 'w') as file:
                for i in self.unique_emails:
                    file.write(i+'\n')

    def main(self):
        """
        Parse arguments from command line
        """
        # don't add --p to parse url pages
        # just can't find url where i can do url + '/paga/{}'.format(i for i in self.page)
        parser = argparse.ArgumentParser()
        parser.add_argument("--e", help="print emails", type=str)
        parser.add_argument("--u", help="print urls", type=str)
        parser.add_argument("--s", help="save emails to file", type=str)
        args = parser.parse_args()
        # example: --u _ --e ema --s res,  things after flags but 'None'

        # remember arguments
        self.email = args.e     # --e emails    NO '-- e emails.txt'
        self.urls = args.u
        self.save = args.s

        if args.e == args.u == args.s:  # if user don't know about arguments
            print('start_.py -h')


if __name__ == "__main__":
    obj = UrlParser()
    obj.main()
    obj.parser()
