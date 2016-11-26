import os
import sys
import time
from datetime import datetime

print('1 == sys.stdout.fileno(): %s' %(1 == sys.stdout.fileno()))

for i in range(5):
    os.write(1, "\r[%d, %.3f]" %(i, time.time()))	# where 1 == sys.stdout.fileno()
    sys.stdout.flush()
    time.sleep(1)	# sleep 1 second

print('\nend flush')

for i in range(1000):
	sys.stdout.write('\ri=%d, %s' %(i, datetime.now()))
	sys.stdout.flush()
	time.sleep(0.001)

print('\nflush demo done...')