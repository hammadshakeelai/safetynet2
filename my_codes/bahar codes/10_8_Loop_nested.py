
counter = 0
for hour in range(12): # [0, 1, 2, .... 9]
    for minut in range(60): # [0, 1, 2, 3, 4]
        for second in range(60): # [0, 1, 2, 3, 4]
            print(hour, ":", minut, ":", second)
            counter+=1

print(counter)