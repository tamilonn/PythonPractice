import time
from concurrent.futures import ThreadPoolExecutor
def wait_on_b():
    time.sleep(5)
    # print(b.result(1))  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result(1))  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)