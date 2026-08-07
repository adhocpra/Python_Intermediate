from threading import Thread
import time

def download():
    print("File downloading:")
    time.sleep(3)
    print("file downloaded.")

def email():
    print("sending email:")
    time.sleep(2)
    print("email sent")


t1= Thread(target=download)
t2= Thread(target=email)

t1.start()
t2.start()


t1.join()
t2.join()

print("Both task done")

