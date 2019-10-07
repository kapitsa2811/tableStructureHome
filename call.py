import multiprocessing
import time
import os

# Your foo function
def foo(n):
    for i in range(10000 * n):
        #print "Tick"
        os.system("python processCordinates_22.py")
        time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(1000000000,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(5)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()