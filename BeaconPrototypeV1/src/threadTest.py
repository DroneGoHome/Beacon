import thread,time
def lower():
	count=0
	while count<5:
		print(count)
		time.sleep(1)
		count+=1		
def upper():
	count2=10
	while count2>5:
		print(count2)
		time.sleep(0.5)
		count2-=1
thread.start_new_thread(lower,())
time.sleep(1)
print('test')
time.sleep(1)
thread.start_new_thread(upper,())
time.sleep(10)