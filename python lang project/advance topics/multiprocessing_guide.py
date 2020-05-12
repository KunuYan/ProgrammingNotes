import concurrent.futures as cf
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return(f'Done Sleeping...{seconds}')

# context manager automatically joined or process
with cf.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # running submit once at a time
    #results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs) # return result in order they were started
    # results are in order of wich ever finished first

    #for f in cf.as_completed(results):
    #    print(f.result())
    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

'''
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return(f'Done Sleeping...')

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

print(processes)

for processe in processes:
    processe.join()
    
#p1 = multiprocessing.Process(target=do_something)
#p2 = multiprocessing.Process(target=do_something)


#p1.start()
#p2.start()

#p1.join()
# p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
'''