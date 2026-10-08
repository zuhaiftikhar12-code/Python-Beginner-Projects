import time

my_time = int(input("Enter time in seconds "))
for i in reversed(range(1,my_time)):
    sec=int(i%60)
    min = int(i/60) % 60
    hours=int(i%3600)
    print(f"00:{min:02}:{sec:02}")
    time.sleep(1)
print("Times up")
