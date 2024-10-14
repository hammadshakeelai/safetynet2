from datetime import datetime

# Get current date and time
now = datetime.now()

# Open a file and write the formatted current date and time to it
with open("current_time.txt", "w") as file:
    file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
