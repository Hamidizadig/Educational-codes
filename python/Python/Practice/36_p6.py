class Files:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_object = None

    def __enter__(self):
        self.file_object = open(self.file_name, self.file_mode)
        return self.file_object

    def __exit__(self, *exc):
        if self.file_object:
            self.file_object.close()


def writeLineToFile(filename, text):
    with Files(filename, 'a') as f1:
        f1.write(text)


try:
    flag1 = False
    flag2 = False
    with Files('36_courses_program.txt', 'r') as file1:
        while file1:
            line = file1.readline()
            if line == 'Python Basic for Beginners\n':
                flag1 = True
            elif line == 'Python for Engineers and Scintists\n':
                flag2 = True
            if line == '\n':
                flag2 = False
                flag1 = False
            if flag1 == True:
                writeLineToFile('file1.txt', line)
            elif flag2 == True:
                writeLineToFile('file2.txt', line)
            if line == '':
                break
            print(line, end='')
except Exception as error:
    print('Enter : ', error)
