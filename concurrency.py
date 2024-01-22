import threading
import time
import datetime
import queue
import random

def task(task_queue, start_times, end_times):
    while not task_queue.empty():
        try:
            num = task_queue.get_nowait()
        except queue.Empty:
            break

        start_times[num] = datetime.datetime.now()
        
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)

        end_times[num] = datetime.datetime.now()
        print(f"Task {num} completed in {sleep_time} seconds.")
        task_queue.task_done()

def print_task_times(start_times, end_times):
    for i in range(10):
        if start_times[i]:
            print(f"Task {i}, Start Time: {start_times[i].strftime('%H:%M:%S')}, End Time: {end_times[i].strftime('%H:%M:%S')}")

def main():
    task_queue = queue.Queue()
    start_times = [None] * 10
    end_times = [None] * 10

    for i in range(10):
        task_queue.put(i)

    threads = [threading.Thread(target=task, args=(task_queue, start_times, end_times)) for _ in range(5)]

    for thread in threads:
        thread.start()

    task_queue.join()

    for thread in threads:
        thread.join()

    print_task_times(start_times, end_times)
    print("All threads finished their tasks")

if __name__ == "__main__":
    main()
