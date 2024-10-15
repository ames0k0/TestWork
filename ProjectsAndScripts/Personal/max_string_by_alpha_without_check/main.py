#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
|a|aa
|a|ba
 +---> 0 -> reposition ?? (Noi)

a|a|b
a|b|a
  +--> 1 -> reposition
  tindex -> to_position[1] -> 1 -> not_changed

aa|b|
ab|a|
   +--> 1 -> reposition
   tindex -> to_position[0] -> 1 -> [a, b] -> do_reposition (??)


a = 'aba'
b = 'aaaa'
    by alpha <a> the max one, but by whole length result will be <b>

    to change it, ^do_reposition may help :: ^do_reposition -> found the greather one
"""


a = 'aba'
b = 'aaaa'

inputs = [a, b]

inc_index = 0
positions = {}

do_calc = True
do_reposition = True


while do_calc:
    reposition = 0
    change_me = inputs[:]

    for tindex, target in enumerate(change_me):
        try:
            # char of target: a|b -> char
            has_char = target[inc_index]
            greather = (ord(has_char) + 1) % 2

            # skip
            reposition += greather

            # new position for target: a|b :: input[*greather] = target ||
            positions[tindex] = greather

        except IndexError:
            change_me.pop(tindex)
            del positions[tindex]


    inc_index += 1
    do_calc = False

    # 0 -> skip
    for _ in range(len(change_me)-1):
        do_calc = True

        # 0 -> skip
        for _ in range(reposition):

            while do_reposition:
                do_reposition = False

                last_pos = inputs[:]

                for key, value in positions.items():
                    inputs[value] = last_pos[key]


# XXX, but not result index :: a|b ?
print('and the result is:', change_me[0])
