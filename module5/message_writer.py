class MessageWriter(object):
    def __init__(self, filename):
        self.filename =filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


with MessageWriter("my_file.txt") as xfile:
    xfile.write("hello AB")
