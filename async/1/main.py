import time
import threading
from multiprocessing import Process
import math

def fact():
    return math.factorial(10)

if __name__ == '__main__':

    t = threading.Thread(target = fact)
    tt = time.monotonic()
    t.start()
    print(time.monotonic() - tt)


    m = Process(target = fact)
    mt = time.monotonic()
    m.start()
    print(time.monotonic() - mt)
