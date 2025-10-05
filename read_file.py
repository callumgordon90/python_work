with open('new_canvas.txt') as file_object:
    # Read the entire file into memory
    contents = file_object.read()

    file_object.seek(0)  # rewind to the beginning
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    
    print(contents)


for line in contents.splitlines():
    print(line)
