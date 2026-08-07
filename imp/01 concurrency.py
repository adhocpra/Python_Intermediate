#multiple tasks at a same time but with wait (switching)
#GIL-mechanism in cpython allows only one thread to execute at a time even on a multi-core CPU. 
#Purpose is to make memory management thread-
from threading import Thread
import time


def task():
    print(" First thread to run")
#thread object 
t1= Thread(target=task)

#start and join
t1.start()
t1. join()
print(" Because of join this runs second")


def greet ():
    time.sleep(2)
    print("Good Morning")
t1= Thread(target=greet)
t1.start()
print(" Hello world")  #this comes have come first
t1.join()


def greet ():
    time.sleep(2)
    print("Good Morning")
t1= Thread(target=greet)
t1.start()
t1.join() #ensures to finish first
print(" Hello world") 


def download():
    time.sleep(3)
    print("File Downloaded")

t1= Thread(target=download)
t1.start()
print("Downloading program")
t1.join()


