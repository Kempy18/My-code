value=0
sum=0
Found = False
while Found == False:
    value=int(input("Enter a positive value:"))
    if value >0:
        Found = True
        for number in range(value):
            number=number+1
            print(number)
            sum+=number
    else:
        print("Invalid value")
print(sum)



    
