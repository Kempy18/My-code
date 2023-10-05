def Createplayers():
    f=open("User.txt","w")
    for i in range (2):
        name=str(input("Enter a name"))
        password=str(input("Enter a password"))
        f.write(name)
        f.write(" ")
        f.write(password + "\n")
    f.close()
Createplayers()
