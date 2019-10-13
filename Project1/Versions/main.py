# team51:$1$hfT7jp2q$CD3hivje3TwA1E32pTFas/:16653:0:99999:7:::

import time
import string
from itertools import product
from string import ascii_lowercase
from hashlib import md5 # md5(string).digest()
import binascii
import multiprocessing

salt = 'hfT7jp2q'
magic = '$1$'
hashed_pass = 'CD3hivje3TwA1E32pTFas/'
b64='./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
password = ''

def cracker():
	for combo in product(ascii_lowercase, repeat = 6):
		password = ''.join(combo)

		alternate_sum = md5(password+salt+password)

		first_six = alternate_sum.digest()

		step5 = password[0] + '\0\0'

		Intermediate0 = md5(password+magic+salt+ first_six[0:6] + step5)

		Intermediate_i = Intermediate0

		for i in xrange(1000):
			temp = ''
			if i % 2 == 0: # Even
				temp = temp + Intermediate_i.digest()
			if i & 1: # Odd
				temp = temp + password
			if i % 3 != 0:
				temp = temp + salt
			if i % 7 != 0:
				temp = temp + password
			if i % 2 == 0:
				temp = temp + password
			if i & 1:
				temp = temp + Intermediate_i.digest()

			Intermediate_i = md5(temp)

		i = Intermediate_i.digest()
		reordered = i[11]+i[4]+i[10]+i[5]+i[3]+i[9]+i[15]+i[2]+i[8]+i[14]+i[1]+i[7]+i[13]+i[0]+i[6]+i[12]

		group0 = int(binascii.hexlify(reordered[13:16]),16)
		group1 = int(binascii.hexlify(reordered[10:13]),16)
		group2 = int(binascii.hexlify(reordered[7:10]),16)
		group3 = int(binascii.hexlify(reordered[4:7]),16)
		group4 = int(binascii.hexlify(reordered[1:4]),16)
		group5 = int(binascii.hexlify(reordered[0]),16)

		to_compare = ''

		for i in xrange(4):
			value = group0 & 0b00111111
			to_compare += b64[value]
			group0 = group0 >> 6

		for i in xrange(4):
			value = group1 & 0b00111111
			to_compare += b64[value]
			group1 = group1 >> 6

		for i in xrange(4):
			value = group2 & 0b00111111
			to_compare += b64[value]
			group2 = group2 >> 6

		for i in xrange(4):
			value = group3 & 0b00111111
			to_compare += b64[value]
			group3 = group3 >> 6

		for i in xrange(4):
			value = group4 & 0b00111111
			to_compare += b64[value]
			group4 = group4 >> 6

		for i in xrange(2):
			value = group5 & 0b00111111
			to_compare += b64[value]
			group5 = group5 >> 6

		if to_compare == hashed_pass:
			print 'Success!'
			print password
			f = open('passwd.txt', 'w')
			f.write(password)
			break
	return

# Start runtime clock
start = time.time()

cracker()

# Stop time
end = time.time()

# Run-time estimate
e_time = end - start;
print "Runtime was: ", e_time, "seconds " 