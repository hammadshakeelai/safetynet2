import random

random_number = random.randint(0, 5) # [0, 5] => Both 0 and 1 are included
print("Random randInt: ", random_number)

random_number = random.random() # [0.0, 1) => 0.0 is included, 1.0 is not included
print("Random random: ", random_number)

random_number = random.uniform(1, 2) # [0, 5] => Both 0 and 1 are included
print("Random uniform: ", random_number)