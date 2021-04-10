row= int(input("Enter row:"))

r= 1

while r <= row:
    c= row
    while c>=r:
        print("*", end="")
        c= c-1
    print("")
    r= r+1