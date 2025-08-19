import time

print(time)  # Prints the module object

# Get info about the 'time' clock
print(time.get_clock_info('time'))

# Print the current time in seconds since the epoch
print(time.time())

# print perf_counter_ns
t0 = time.perf_counter_ns()
print(f"t0 is : {t0}")
time.sleep(3)

t1 = time.perf_counter_ns()
print(f"t1 is : {t1}")

diff = t1 - t0
print(f"time diff in nano seconds:  {diff}")

print(f"time diff in seconds: {diff/1000000000}")

arrt = array[1, 0]
print(arrt)
