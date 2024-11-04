import logging
import time
import re

logging.basicConfig(level=logging.INFO, format ='[%(asctime)s] [ - %(name)s - %(levelname)s ] %(message)s')
logger = logging.getLogger(__name__)

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	PINK = '\33[101m'

	FUP = '\33[92m'
	FNORM = '\33[34m'
	FDOWN = '\33[91m'

o = ['-18.800000','2.83220000','-4.0489000','0.63049999','-465.46632','1.15','-0.45','1.41','1.564','0.45','-15','-422.6861', '0.0', '-0.0', '0.2', '54', '545','0.547']
A = 'MY LIFE'

upup = r'\d+'
uplvl = r'\d+\.\d{2,10}'
normlvl = r'0\.0'
downlvl = r'\-+\d+\.\d{2,10}'

pic = '''
|------------------------|---------------------|----------------------|
|	    {}*UP{}	  	 |	  {}*NORM{}        |        {}*DOWN{}         |
|________________________|_____________________|______________________|
'''.format(color.FUP,color.END,color.FNORM,color.END,color.FDOWN,color.END)
print(pic)

for i in o:
	u = re.findall(uplvl, i)
	m = re.findall(upup, i)
	if i in u or i in m:
		gs = i.replace('[]\'','')
		logging.info('{}:{} +{} {}'.format(A, color.FUP, gs, color.END))
		time.sleep(1)

	n = re.findall(normlvl, i)
	if i in n:
		gs = i.replace('[]\'','')
		logging.info('{}:{}  {} {}'.format(A, color.FNORM, gs, color.END))
		time.sleep(1)


	d = re.findall(downlvl, i)
	if i in d:
		gs = i.replace('[]\'','')
		logging.info('{}:{} {} {}'.format(A, color.FDOWN, gs, color.END))
		time.sleep(1)