#usr/bin/env python
#Python program to create a .fly2 file, which is used by SIMION to define particles that it flies
#Last run with the arguments: 81.65 7 42 18 1000, for the scaled ionizer .iob


import sys
import numpy as np
import random

def main():
	X_INTERCEPT = float(sys.argv[1])
	THETA_MIN = float(sys.argv[2])*(np.pi/180)
	THETA_MAX = float(sys.argv[3])*(np.pi/180)
	RADIUS = float(sys.argv[4])
	NUM_IONS = int(sys.argv[5])
	print 'particles {'
	print '  coordinates = 0,'	
	separation = (THETA_MAX-THETA_MIN)/14.0	

	for i in range(NUM_IONS):
		print '  standard_beam {'
		print '    n = 1,'
		print '    tob = 0,'
		print '    mass = 133,'
		print '    charge = 1,' 
		phi = random.random() * 2*np.pi
		u = random.random()*(np.cos(THETA_MIN)-np.cos(THETA_MAX))+np.cos(THETA_MAX)
		theta = arccos(u)
		z = RADIUS*np.cos(theta)
		y = RADIUS*np.sin(theta)*np.sin(phi)
		x = RADIUS*np.sin(theta)*np.cos(phi)
		c = int((theta - THETA_MIN)/ separation)
		print '    x = {},'.format(z + X_INTERCEPT - RADIUS)
		print '    y = {},'.format(y)
		print '    z = {},'.format(x)
		print '    ke = gaussian_distribution {'
		print '      mean = 300,'
		print '      fwhm = 1'
		print '    },'
		print '    cwf = 1,'
		print '    color = {},'.format(c)
		print '    direction = vector(-1, 0, 0)'
		if i==NUM_IONS-1 :
			print '  }'
		else:
			print '  },'
	print '}'



if __name__ == "__main__":
	main()
