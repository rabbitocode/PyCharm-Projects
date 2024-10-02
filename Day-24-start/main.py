with open("my_file.txt") as file:
    contents = file.read()
    print(contents)



## TODO modes , "w" as write, "a" as append

with open("new_file.txt", mode="w") as file:
    file.write("New text file.")