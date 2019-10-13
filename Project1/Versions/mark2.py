# https://stackoverflow.com/questions/16347583/how-to-generate-all-possible-strings-in-python
# https://rsmitty.github.io/MD5-password-cracker-in-python/

# team51:$1$hfT7jp2q$CD3hivje3TwA1E32pTFas/:16653:0:99999:7:::

import time
import string
from itertools import product
from string import ascii_lowercase
from hashlib import md5 # md5(string).digest()
import binascii

salt = 'hfT7jp2q'
magic = '$1$'
hashed_pass = 'CD3hivje3TwA1E32pTFas/'
b64='./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

print '\n',

# Start runtime clock
start = time.time()

'''
for combo in product(ascii_lowercase, repeat = 1):
	print ''.join(combo)
'''

password = 'abcdef'

alternate_sum = md5(password+salt+password)
print "Alternate : " + alternate_sum.hexdigest() + '\n'

first_six = alternate_sum.digest()
#print 'temp: ' + first_six[0:6]

step5 = password[0] + '\0\0'

# Input to intermediate0
print ('Input inter0: ' + ":".join("{:02x}".format(ord(c)) for c in password+magic+salt+ first_six[0:6] + step5))
#print '\n'

Intermediate0 = md5(password+magic+salt+ first_six[0:6] + step5)
#Intermediate_hex = Intermediate0.hexdigest()
print 'intermediate0: ' + Intermediate0.hexdigest() + '\n'

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

print "Intermediate 1000: " + Intermediate_i.hexdigest() + '\n'

i = Intermediate_i.digest()
reordered = i[11]+i[4]+i[10]+i[5]+i[3]+i[9]+i[15]+i[2]+i[8]+i[14]+i[1]+i[7]+i[13]+i[0]+i[6]+i[12]
print 'Reordered: ' + reordered +'\n'

group0 = int(binascii.hexlify(reordered[13:16]),16)
print group0
group1 = int(binascii.hexlify(reordered[10:13]),16)
print group1
group2 = int(binascii.hexlify(reordered[7:10]),16)
print group2
group3 = int(binascii.hexlify(reordered[4:7]),16)
print group3
group4 = int(binascii.hexlify(reordered[1:4]),16)
print group4
group5 = int(binascii.hexlify(reordered[0]),16)
print group5

print '\n'

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

print to_compare

if to_compare == hashed_pass:
	f = open('passwd.txt', 'w')
	f.write(password)




'''
to_shift = int(binascii.hexlify(reordered),16)
print 'to_shift: '
print to_shift


for i in xrange(22,0,-1):
	bits = to_shift #& 63
	print bits
	to_shift = to_shift >> 6
	print to_shift
	bit_group = int(binascii.hexlify(bits),16) & 0b00111111
	print bin(int(bit_group))
'''

# Stop time
end = time.time()

# Run-time estimate
e_time = end - start;
print "Runtime was: ", e_time, "seconds " 