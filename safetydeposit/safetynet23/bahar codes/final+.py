def remove_deleted():
    files=("course.txt","student.txt")
    for file in files:
        fileData=""
        file_output=open(file,"r+")
        lines=file_output.readlines()
        for line in lines:
            if line.strip().split(", ")[0]=='0':
                continue
            fileData+=line
        file_output.seek(0)
        file_output.writelines(fileData)
        file_output.close