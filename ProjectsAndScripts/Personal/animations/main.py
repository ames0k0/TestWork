import sys
from time import sleep


def fp(s, fp_speed):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        if fp_speed:
        	sleep(1./fp_speed)
        else:
        	sleep(1./500)

def right():
	""" ---M ++GM -PGM RPGM """
	ww = input('__word__: ')
	ne = []
	gl = len(ww) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in ww:
				if tin % 2 == 0:
					li = "+" * gl
				else:
					li = "-" * gl
				gn = ww[-tin:]
				ne.append(li+gn)
				tin += 1
				gl -= 1
		else:
			break
	ke = "\r".join(ne)
	return ke

def right_left():
	""" ---R ++RP -RPG RPGM """
	ww = input('__word__: ')
	ne = []
	gl = len(ww) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in ww:
				if tin % 2 == 0:
					li = "+" * gl
				else:
					li = "-" * gl
				gn = ww[:tin] 
				ne.append(li+gn)
				tin += 1
				gl -= 1
		else:
			break
	ke = "\r".join(ne)
	return ke

def left():
	""" M--- GM++ PGM- RPGM """
	ww = input('__word__: ')
	ne = []
	gl = len(ww) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in ww:
				if tin % 2 == 0:
					li = "+" * gl
				else:
					li = "-" * gl
				gn = ww[-tin:]
				ne.append(gn+li)
				tin += 1
				gl -= 1
		else:
			break
	ke = "\r".join(ne)
	return ke

def left_left():
	""" R--- RP++ RPG- RPGM """
	ww = input('__word__:')
	ne = []
	gl = len(ww) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in ww:
				if tin % 2 == 0:
					li = "+" * gl
				else:
					li = "-" * gl
				gn = ww[:tin] 
				ne.append(gn + li)
				tin += 1
				gl -= 1
		else:
			break
	ke = "\r".join(ne)
	return ke

def load_anim(count):
	""" Rpgm rPgm rpGm rpgM """
	_for_list = []
	# ww = 'rpgm'
	w = input('__word__: ')
	ww = w.lower()
	l = len(ww)
	for i in range(l):
		if i >= 0:
			_do_up = ww[i].upper()	# lower() - for UPPER words
			_for_list.append(ww[:i] + _do_up + ww[i+1:] + '\r')
			i -= 1
	_for_list.append(ww + '\r')		# rpgm
	ke = "".join(_for_list)
	return ke * count


def anim_plus_minus(count):
	plus = '++++++++++++++++++++++++++++++'
	pluses = []
	leno = len(plus) - 1
	tin = 1
	while True:
		if tin <= leno:
			for i in plus:
				gn = plus[:tin]
				pluses.append(gn + '\r')
				tin += 1
				leno -= 1
		else:
			break
	plu = "".join(pluses)

	minus = '------------------------------'
	ne = []
	gl = len(minus) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in minus:
				gn = minus[:tin]
				li = "+" * gl
				ne.append(li + gn + '\r')
				tin += 1
				gl -= 1
		else:
			break
	minu = "".join(ne)
	merge = plu+minu
	return merge*count

def anim_side(count):
	plus = '++++++++++++++++++++++++++++++'
	pluses = []
	leno = len(plus) - 1
	tin = 1
	while True:
		if tin <= leno:
			for i in plus:
				gn = plus[:tin]
				pluses.append(gn + '\n')
				tin += 1
				leno -= 1
		else:
			break
	plu = "".join(pluses)

	minus = '------------------------------'
	ne = []
	gl = len(minus) - 1
	tin = 1
	while True:
		if tin <= gl:
			for i in minus:
				gn = minus[:tin]
				li = "+" * gl
				ne.append(li + gn + '\n')
				tin += 1
				gl -= 1
		else:
			break
	minu = "".join(ne)
	merge = plu+minu
	return merge*count

if __name__ == '__main__':
	plano = """
				__word__: RPGM

1:  ---M	2:  ---R 	3:  Rpgm 	4:  M--- 	5:  R--- 	6:  my_anim
    ++GM 	    ++RP 	    rPgm 	    GM++	    RP++	7:  anim_side
    -PGM 	    -RPG 	    rpGm 	    PGM- 	    RPG-
    RPGM 	    RPGM 	    rpgM 	    RPGM 	    RPGM
	"""
	speed = input('__set_speed: number from 2 to (999999) += n:_ ')
	if speed:
		try:
			true_speed = int(speed)
		except ValueError:
			print('Only number')
			raise
		print(plano)
	else:
		true_speed == None
	while True:
		que = input("?: ")
		if que:
			if que == '1':
				fp(right(), true_speed)
			elif que == '2':
				fp(right_left(), true_speed)
			elif que == '3':
				count = input('how much time do UPPER all symbols:_ ')
				try:
					true_count = int(count)
				except:
					print('    Only number')
					break
				fp(load_anim(true_count), true_speed)
			elif que == '4':
				fp(left(), true_speed)
			elif que == '5':
				fp(left_left(), true_speed)
			elif que == '6':
				fp(anim_plus_minus(4), None)
			elif que == '7':
				fp(anim_side(4), 800)
			else:
				pass
		else:
			break
