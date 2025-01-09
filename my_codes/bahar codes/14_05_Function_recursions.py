import os
path = '../VSCODE'
total_space = 0
def list_file(directory):
    global total_space
    for item in os.listdir(directory):
        rel_path = os.path.join(directory, item) 
        if os.path.isdir(rel_path):
            list_file(rel_path)
        else:
            #abs_path = os.path.abspath(os.path.join(directory, item))
            total_space += os.path.getsize(rel_path)

list_file(path)
print("Total Space: ", total_space)
