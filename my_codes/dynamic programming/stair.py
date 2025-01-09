def stairs_climbed(no_of_stairs):
    if no_of_stairs <= 2:
        return 1
    else:
        return stairs_climbed(no_of_stairs-2)+1
print(stairs_climbed(7))

