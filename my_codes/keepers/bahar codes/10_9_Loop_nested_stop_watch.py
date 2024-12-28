import time

counter = 0
for hour in range(12): # [0, 1, 2, .... 11]
    counter+=1
    for minut in range(60): # [0, 1, 2, 3, 4, ....59]
        for second in range(60): # [0, 1, 2, 3, 4, ....59]
            time.sleep(1) 
            print(hour, ":", minut, ":", second)
print(counter)
