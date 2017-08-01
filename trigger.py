import os
import sys
import time
sys.path.append(os.path.abspath('.'))
#trigger.py
from  task import add,test_mes
def pm(body):
	res = body.get('result')
	if body.get('status') == 'PROGRESS':
		sys.stdout.write('\rtask progress {0}%'.format(res.get('p')))
		sys.stdout.flush()
	else:
		print '\r'
		print res
r = test_mes.delay()
print r.get(on_message=pm,propagate=False)
#result = add.delay(3,4)
#while not result.ready():
#	time.sleep(1)
#print result.get()