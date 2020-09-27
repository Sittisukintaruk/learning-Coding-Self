import os

def Writefiledemofile2():
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    #open and read the file after the appending:
    f = open("demofile2.txt", "r")
    print(f.read())


def Writefiledemofile3():
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

    #open and read the file after the appending:
    f = open("demofile3.txt", "r")
    print(f.read())



def CreateNewFile():
    f = open("myfile.txt" , "w")
    print(f.read())


def delete_check():
    # os.remove("myfile.txt")
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
         print("The file does not exist")

def delectFolder():
    os.rmdir("myfolder")


def check_direatory():
    t  = os.getcwd()
    print(f'{t}')


check_direatory()