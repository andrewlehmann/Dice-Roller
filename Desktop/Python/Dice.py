import sys
from random import randint

def main():
	cont = 'y'
	while cont == 'y' or cont == 'Y':
		firstInput = raw_input('Enter the number of sides on the die you would like to roll: ')
		try:
			roll(int(firstInput))
		except ValueError:
			print 'Invalid number of sides, please try again.'
		cont = raw_input('Enter \'y\' to roll another die, or any other key to exit:')
	sys.exit()

def roll(input):
	output = randint(1, input)
	print 'You have rolled: ' + str(output)
	return

if __name__ == '__main__':
	main()