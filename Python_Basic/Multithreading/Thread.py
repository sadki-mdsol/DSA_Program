from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.2)


t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

t1.join()
t1.join()

print("Existed from Main")