# https://stackoverflow.com/questions/16347583/how-to-generate-all-possible-strings-in-python
# https://rsmitty.github.io/MD5-password-cracker-in-python/

# team51:$1$hfT7jp2q$CD3hivje3TwA1E32pTFas/:16653:0:99999:7:::

import time
import string
from itertools import product
from string import ascii_lowercase
from hashlib import md5 # md5(string).digest()

salt = 'hfT7jp2q'
magic = '$1$'
hashed_pass = 'CD3hivje3TwA1E32pTFas/'

print '\n',

# Start runtime clock
start = time.time()

'''
for combo in product(ascii_lowercase, repeat = 1):
	print ''.join(combo)
'''

password = 'abcdef'
'''
temp1 = md5(password+magic+salt).hexdigest()
print 'temp: ' + temp1 + '\n'
'''
alternate_sum = md5(password+salt+password)
print "Alternate : " + alternate_sum.hexdigest() + '\n'

first_six = alternate_sum.digest()
#print 'temp: ' + first_six[0:6]

# Input to intermediate0
print ('Input inter0: ' + ":".join("{:02x}".format(ord(c)) for c in password+magic+salt+ first_six[0:6] + 'a\0\0'))
#print '\n'

Intermediate0 = md5(password+magic+salt+ first_six[0:6] + 'a\0\0')
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



# Stop time
end = time.time()

# Run-time estimate
e_time = end - start;
print "Runtime was: ", e_time, "seconds " 