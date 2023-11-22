import os


def create_file(filename):
    try:
        with open('tex.txt', 'w') as file:
            file.write("Hello, world!\n")
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error : Could not create file " + filename)


def read_file(filename):
    try:
        with open('tex.txt', 'r') as file:
            contents = file.read()
            print(contents)
    except IOError:
        print("Error: Could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text)
        print("text append to the file " + filename + " successful.")
    except IOError:
        print("Error: cound not append to file" + filename)


def rename_file(file_name, new_name):
    try:
        os.rename(file_name, new_name)
        print("file " + file_name + "has been renamed to " + new_name)
    except IOError:
        print("Error : could not rename the file " + file_name)


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " has been deleted successfully.")
    except IOError:
        print("Error: Could not delete file " + filename)


if __name__ == '__main__':
    filename = "old.txt"
    new_filename = "new_file.txt"

    # create_file(filename)
    read_file(filename)
    append_file(filename, "this is new data appeded to file \n")
    read_file(filename)
    # rename_file(filename,new_filename)
    # read_file(new_filename)
    # delete_file(new_filename)
