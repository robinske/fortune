import sys
import random

def read_file(filename):
	with open(filename, 'r') as f:
		fortunes = f.read()
	f.closed
	return fortunes

def parse_fortunes(unparsed):
	return unparsed.split('%')

def choose_random(fortunes):
	random_idx = random.randint(0, len(fortunes)-1)
	return fortunes[random_idx]

def main():
	try:
		filename = sys.argv[1]
	except IndexError:
		filename = 'fortunes.txt'

	unparsed = read_file(filename)
	parsed = parse_fortunes(unparsed)
	fortune = choose_random(parsed)
	print fortune

if __name__ == '__main__':
	main()