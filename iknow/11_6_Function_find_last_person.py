def find_last_person(n):
    my_list = [i for i in range(1, n+1)]
    print(my_list, "- Sword with", my_list[0])

    flag = True
    while(len(my_list) > 1):
        temp_list = []
        for item in my_list:
            if flag:
                temp_list.append(item)
            flag = not flag
        my_list = temp_list
        if flag:
            print(my_list, "- Sword with", my_list[0])
        else:
            print(my_list, "- Sword with", my_list[-1])
    return my_list[0]

print("The last person", find_last_person(10))
def find_last_person9(n):
    # Start with a list of people numbered from 1 to n
    people = list(range(1, n + 1))
    
    # Initialize the starting index (the person who holds the "sword")
    index = 0

    # Continue until only one person remains
    while len(people) > 1:
        # Eliminate the next person (every second person)
        people.pop((index + 1) % len(people))
        
        # Move the sword to the next person (new "index" after removal)
        index = (index + 1) % len(people)
        
        # Display the current list of people and the person holding the sword
        print(f"{people} - Sword with {people[index]}")

    # The last remaining person
    return people[0]

