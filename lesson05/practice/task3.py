class MyContextManager():
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        print('Context Manager Openned')
        try:
            self.fp = open(self.file, self.flag)
        except IOError:
            self.fp = open(self.file, "w")
        return self.fp

    def __exit__(self, exc_type, exc_value, exc_tr):
        print(exc_type, exc_value, exc_tr)
        if exc_type is IOError:
            self.fp.close()
            return True
        self.fp.close()

with MyContextManager("my_file.txt", "w") as fp:
    fp.write("Hello, World!!!\n")