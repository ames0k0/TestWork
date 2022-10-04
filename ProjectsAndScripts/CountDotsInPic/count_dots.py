#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import numpy as np #-------------------#
from sys import argv #-----------------#
from PIL import Image #----------------#
from collections import Counter, deque #
from urllib.request import urlretrieve #


class CountDots:
    """
    I'm not sure about result, but _404_, mmmmmmm... idk :)
    I've opened pic with program PINTA,
        to see count of pixels in Dots and set limit DEEP (n122) and limit LENGTH (n68)
    """

    def __init__(self):
        # self.pico = self.get_image()
        self.pico = 'count_it.png'
        self.photo = Image.open(self.pico)
        self.photo = self.photo.convert('RGB')
        self.width = self.photo.size[0]
        self.height = self.photo.size[1]
        self.copied = np.zeros((self.height, self.width))
        self.deep = 1
        self.count = 1

    def get_image(self):
        url = "https://lh5.googleusercontent.com/yO12GARP3fqmNOZ00zM9Q_nyBVWWfR_xVu8skrvAmhB1hzSJyq_F593jhQqS48aWJyCZ5jzDAQ=w513"
        pico = 'count_it.png'
        urlretrieve(url, pico)
        return pico

    def checker(self, tar):
        """
        :tar:   column value
        """
        # 765 = 255, 255, 255 == white pixel, 0.? = value that we fill or we will
        if tar != 765.0 and not str(tar).startswith('0.'):
            return True
        return False

    def des(self, todow, kgs):
        """
        :todow:     row_id
        :kgs:       list with columns_id (indexes) from left() and right()

        cheking deep rows: and nah chenging counts of dots (flag='deep')
        """
        if kgs:
            for i in kgs:
                self.down(todow, i, "deep")

    def right(self, idi, idj, flag, to_fill):
        """
        :idi:       row_id
        :idj:       column_id
        :flag:      to return or not checked indexes
        :to_fill:   list from _left_ with checked indexes

        check RIGHT neighbors
        """
        r = True
        while r:
            if len(to_fill) <= 5 and idj < 513:
                point = self.copied[idi][idj]
                if self.checker(point):
                    self.copied[idi][idj] = float(f"0.{self.count}")
                    to_fill.append(idj)
            else:
                r = False
            idj += 1
        if flag == 'deep':
            return to_fill

    def left(self, idi, idj):
        """
        :idi:   row_id
        :idj:   column_id

        check LEFT neighbors
        """
        # idj+1 index to check 1lvl down
        km = [idj+1]

        # l - limit indexes we can check
        l = True
        while l:

            # < 5 and not negative index, :yes: append 5th
            if len(km) < 5 and 0 < idj:
                point = self.copied[idi][idj]
                if self.checker(point):
                    self.copied[idi][idj] = float(f"0.{self.count}")
                    km.append(idj)
            else:
                l = False

            # move 1 pixel left
            idj -= 1
        return self.right(idi, idj+1, 'deep', km)

    def down(self, idi, idj, flag):
        """
        :idi:   row_id
        :idj:   column_id
        :flag:  flag to break process _or_ go deeper with row_id
        """
        dw = self.copied[idi][idj]
        if self.checker(dw):
            self.copied[idi][idj] = float(f"0.{self.count}")
            rfpixels = self.left(idi, idj-1)

            # reset deep counter
            if flag == "root":
                self.deep = 1

            # go deeper
            elif flag == "deep":
                self.deep += 1

            # limit value to go down: if 5x5 then: self.deep <= 5
            if self.deep <= 5:
                self.des(idi+1, rfpixels)

    def get_index_of_pixels(self):
        """
        we can't change pic indexes with PIL.Image
        we can copy values of pic to numpy.array and change it
        """
        for y in range(0, self.height):
            for x in range(0, self.width):
                RGB = self.photo.getpixel((x,y))
                self.copied[y][x] = sum(RGB)

    def start(self):
        self.get_index_of_pixels()
        for idi, i in enumerate(self.copied[:]):
            for idj, j in enumerate(i):
                if self.checker(j):
                    self.copied[idi][idj] = float(f"0.{self.count}")
                    self.right(idi, idj+1, 'root', to_fill=[])
                    if idi+1 < 354:   # height: 353
                        down = self.copied[idi+1][idj]
                        if self.checker(down):
                            self.down(idi+1, idj, 'root')
                            self.count += 1
        print('total count: ', self.count)


if __name__ == "__main__":
    cd = CountDots()
    cd.start()
