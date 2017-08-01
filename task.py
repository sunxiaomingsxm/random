#task.py
##encoding: utf-8 默认编码
import time
from celery import Celery

app = Celery('task',backend='redis://localhost:6379/0',broker='redis://localhost:6379/0')#配置好celery的backend和broker
 
@app.task
def add(x,y):
	return x + y

@app.task(bind=True)
def test_mes(self):
	for i in xrange(1,11):
		time.sleep(0.1)
		self.update_state(state='PROGRESS',meta={'p':i*10})
	return 'finish'