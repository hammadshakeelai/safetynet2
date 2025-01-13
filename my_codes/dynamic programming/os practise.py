import os
print(os.getcwd()) #get current working directory
os.chdir('D:/ ') #cd == change directory 
print(os.listdir()) # list of directory's
os.mkdir('github2') #make directory
os.makedirs('github2/git1') #make directory and directory inside directory
os.removedirs('github2/')
os.rename('github2', 'GitHub-2') #rename directory
print(os.stat('github2'))#stats of this directory
print(os.stat('github2').st_size)#size of this directory
print(os.stat('github2').st_mtime)#time of last modification of this directory
from datetime import datetime 
print(datetime.fromtimestamp(os.stat('github2').st_mtime))#time of last modification human readable
for dirpath, dirnames, filenames in  os.walk('D:/github2/git1'):
    print('current path;',dirpath)
    print('directories;',dirnames)
    print('files;',filenames)
    print()
