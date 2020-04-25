import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    #f1 = executor.submit(do_something, 2)
    #f2 = executor.submit(do_something, 2)

    #print(f1.result())
    #print(f2.result())

    # to run our method multiple times, way #1
    #results = [executor.submit(do_something, 2) for _ in range(10)]

    #for f in concurrent.futures.as_completed(results):
        #print(f.result())

    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')





"""import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done Sleeping...")


#t1 = threading.Thread(target=do_something)
#t2 = threading.Thread(target=do_something)

#t1.start()
#t2.start()

#t1.join()
#t2.join()

threads = []
for _ in range(10): # _ is a throw away variable
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')"""

