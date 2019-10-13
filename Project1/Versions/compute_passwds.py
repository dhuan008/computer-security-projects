# https://stackoverflow.com/questions/16347583/how-to-generate-all-possible-strings-in-python
# https://rsmitty.github.io/MD5-password-cracker-in-python/

# team51:$1$hfT7jp2q$CD3hivje3TwA1E32pTFas/:16653:0:99999:7:::


import time
from itertools import product
from string import ascii_lowercase
from hashlib import md5 # md5(string).digest()

salt = 'hfT7jp2q'

# Start runtime clock
start = time.time()
'''
for combo in product(ascii_lowercase, repeat = 6):
	print ''.join(combo)
	password = ''.join(combo)
	alternate_sum = md5(password+salt+password)
	Intermediate0 = 
'''
f = open('passwd.txt', 'w')
for combo in product(ascii_lowercase, repeat = 6):
	f.write( ''.join(combo)+',')
	#print (''.join(combo))
	
# Stop time
end = time.time()

# Run-time estimate
e_time = end - start;
print ("Runtime was: ", e_time, "seconds ")
