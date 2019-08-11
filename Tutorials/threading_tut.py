# Threading - Basically running two programs at the same time

import threading

class MyMessenger(threading.Thread):

    def run(self):
        for _ in range(1000):
            print(threading.currentThread().getName())      # Remember the syntax

# 2 threads to send and receive msgs
x = MyMessenger(name = 'send out msgs')     # naming a thread
y = MyMessenger(name = 'receive msgs')

x.start()       # its a rule. The start() goes to run(). You cant run the run() directly
y.start()

#its cool. It starts executing object 'y' even before finishing object 'x'. Basically runs them parallely, and finishes it faster