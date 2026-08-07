from multiprocessing import Process
import time

def task():
    time.sleep(2)
    print("Hello world")

if __name__ == "__main__":
    p1 = Process(target=task)
    print("This is regular world")

    p1.start()
    p1.join()
    print("This is always at last")



def process_image():
    print("Processing image")
    time.sleep(3)
    print("Image processed")

def render_video():
    print("video rending")
    time.sleep(2)
    print("video rendered")

if __name__=="__main__":
    p1= Process(target=process_image)
    p2=Process(target=render_video)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

print("all tasks completed")