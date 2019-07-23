import string import ascii_lowercase
from words import get_random_word

def get_num_attempts():
	while True:
		num_of_attempts = input('How many incorrect attempts do you wish to allow? [1-25] ')
		try:
			num_attempts = int(num_attempts)
				if 1 <= num_attempts = num_of_attempts