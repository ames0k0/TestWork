#!/usr/bin/env python3
# coding:utf-8

import argparse
from requests import get
from wget import download
from sys import exit


class Cobi_Cobi():
    """Download Cobi-tyan"""
    
    def __init__(self):
        self.c_link = None
        self.ch_link = None
        self.coub_info = None 
        self.download_coub_video = None
        self.download_coub_audio = None
        self.download_coub_audio_and_video = None
        self.channel_background_coub = None
        self.channel_info = None

    def link(self):
        r"""
        c    \
        dcv   \___ coub_link
        dca   /
        dcav /
        """
        if self.download_coub_video:
            self.c_link = self.download_coub_video
        elif self.download_coub_audio:
            self.c_link = self.download_coub_audio
        elif self.coub_info:
            self.c_link = self.coub_info
        elif self.download_coub_audio_and_video:
            self.c_link = self.download_coub_audio_and_video
        
        if self.channel_info:
            self.ch_link = self.channel_info
        elif self.channel_background_coub:
            self.ch_link = self.channel_background_coub

    def coub(self):
        if self.c_link:
            _id = self.c_link.split('/')[-1]
            _coub_id = "https://coub.com/api/v2/coubs/{}".format(_id)
            data = get(_coub_id).json()
            try:
                _catch_error_link = data['title']
            except KeyError:
                print("""
        Your link was not True!
        I'm waitin link like a: https://coub.com/view/t8rbd 
                      """)
                exit(0)
            _title = data['title']
            _channel_id = data['channel_id']
            _file = data['file_versions']
            _file_versions = data['file_versions']['html5']
            _video = str(_file_versions['video']).split("'")[1]
            _video_url = _file_versions['video'][_video]['url']
            _audio = str(_file_versions['audio']).split("'")[1]
            _audio_url = _file_versions['audio'][_audio]['url']
            _creator = data['channel']['title']
            _ttags = data['tags']
            _tags = []
            for tg in _ttags:
                _tags.append(tg['title'])

            _cre_msg = """
    _channel_id: {}
    _creator:--: {}
    _title:----: {}
    _video_url:: {}
    _audio_url:: {}
    _tags:-----: {}
            """.format(_channel_id, _creator, _title, _video_url, _audio_url, str(_tags).strip("[]"))
            if self.download_coub_video:
                print('\n[+] {}'.format(_video_url))
                download(_video_url)
                print('\n')
            if self.download_coub_audio:
                print('\n[+] {}'.format(_audio_url))
                download(_audio_url)
                print('\n')
            if self.coub_info:
                print(_cre_msg)
            if self.download_coub_audio_and_video:
                download(_audio_url)
                download(_video_url)
                print('\n')

    def channel(self):
        if self.ch_link:
            _id = self.ch_link.split('/')[-1]
            channel_id = "https://coub.com/api/v2/channels/{}".format(_id)
            data = get(channel_id).json()
            try:
                _catch_error_link = data['title']
            except KeyError:
                print("""
        Your link was not True!
        I'm waitin link like a: https://coub.com/knightofchaos
                      """)
                exit(0)
            _title = data['title']
            _description = data['description']
            _ccontacts = data['contacts']
            _contacts = []
            for cn in _ccontacts.values():
                if cn:
                    _contacts.append(cn)
            try:
                _bre = data['background_coub']['file_versions']['html5']['video']
                _br = str(_bre).split("'")[1]
                _background = _bre[_br]['url']
            except TypeError:
                _background = data['background_image']
            _cre_msg = """
    _title:---: {}
    _descr:---: {}
    _contacts:: {}
    _ch_bkg:--: {}
            """.format(_title, _description, str(_contacts).strip("[]"), _background)
            if self.channel_background_coub:
                print('\n[+] {}'.format(_background))
                download(_background)
                print('\n')
            if self.channel_info:
                print(_cre_msg)

    def activate(self):
        """ parse arguments in command line """
        parser = argparse.ArgumentParser()
        parser.add_argument("--c", help="coub info", type=str)
        parser.add_argument("--dcv", help="download coub video", type=str)
        parser.add_argument("--dca", help="download coub audio", type=str)
        parser.add_argument("--dcav", help="download coub audio and video", type=str)
        parser.add_argument("--ch", help="channel info", type=str)
        parser.add_argument("--chb", help="download channel background coub or pic", type=str)
        args = parser.parse_args()

        self.coub_info = args.c
        self.download_coub_video = args.dcv
        self.download_coub_audio = args.dca
        self.download_coub_audio_and_video = args.dcav
        self.channel_info = args.ch
        self.channel_background_coub = args.chb

        if args.c == args.dcv == args.dca == args.dcav == args.chb == args.ch:
            print("""
    req.py -h    helps, try it first

    exm:
    req.py --c   https://coub.com/coub
    req.py --ch  https://coub.com/channel
                  """)


if __name__ == "__main__":
    cyaaa = Cobi_Cobi()
    cyaaa.activate()
    cyaaa.link()
    cyaaa.coub()
    cyaaa.channel()

