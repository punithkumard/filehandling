import os
print("**************************************************")
print("*       file handling                            *")
print("**************************************************")
def fi():
    print("1.create file")
    print("2.list file")
    print("3.edit file")
    print("4.delete file")
    print("5.read file")
    print("6.program stopped")
    a=input("enter your choice")
    match a:
        case"1":
            print("__________________________________________________")
            print("file created")
            print("__________________________________________________")
            print("enter your file name \n")
            f=input("")
            h=f+".txt"
            with open(h,'x')as file:
                print(f,"file is created successfilly")
        case"2":
            print("__________________________________________________")
            print("listing file")
            print("__________________________________________________")
            path="D\python sql connector"
            file=os.listdir(path)
            for file in file:
                print(file)
        case"3":
            print("__________________________________________________")
            print("editing file")
            print("__________________________________________________")
            name=input("enter the file name that you want to edit \n:")
            name=name+".txt"
            print(file.write("word"))
            print("edited the file")
        case"4":
            print("__________________________________________________")
            print("deleting file")
            print("__________________________________________________")
            name=input("enter the file name that you want to delete \n:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"deleted successfully")
        case"5":
            print("__________________________________________________")
            print("reading file")
            print("__________________________________________________")
            print("reading file \n")
            print("..................................................")
            print("enter the file name that you want to read\n")
            f=input("")
            with open(f+".txt",'r')as file:
                print(file.read())
                print("the file read successfully\n")
        case"6":
            print("__________________________________________________")
            print("program stopped")
            print("__________________________________________________")
while True :
    fi()
print("**************************************************")
