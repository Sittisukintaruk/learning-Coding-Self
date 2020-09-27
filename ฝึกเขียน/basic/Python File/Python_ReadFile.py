# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

def openfile():
    f = open("demofile.txt" ,"rt")
    text = f.read()
    print(f'{text}')


def ReadOnly():
    f = open("demofile.txt" ,"r")
    text = f.read(5)
    print(f'{text}')


def ReadLines():
    f = open("demofile.txt" ,"r")
    text = f.readline()
    text1 = f.readline()
    print(f'{text}{text1}')
    
def loopfile():
    f = open("demofile.txt", "r")
    for x in f:
        print(x)
    f.close()

loopfile()