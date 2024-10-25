import time

counter = 0
for hour in range(12): # [0, 1, 2, .... 9]
    counter+=1
    for minut in range(60): # [0, 1, 2, 3, 4]
        for second in range(60): # [0, 1, 2, 3, 4]
            time.sleep(1) 
            print(hour, ":", minut, ":", second)
print(counter)
