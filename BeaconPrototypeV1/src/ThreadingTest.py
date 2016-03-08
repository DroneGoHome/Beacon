import threading,time
def lower():
    count=0
    while count<5:
        print(count)
        time.sleep(2.5)
        count+=1
def upper():
    count=10
    while count>5:
        print(count)
        time.sleep(1)
        count-=1
#threading._MainThread()
threading.Thread(target=upper).start()
threading.Thread(target=lower).start()
print("main thread")