with open('new_canvas.txt') as file_object:
    # Read the entire file into memory
    contents = file_object.read()

    file_object.seek(0)  # rewind to the beginning
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    
    print(contents)

word = "Python"


contents = contents.replace(word, "PHP" )

for line in contents.splitlines():
    print(line)
