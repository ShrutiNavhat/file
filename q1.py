# f = open("shruti.txt", "w")
# file_data=f.write("my\nname\nis\nshruti")
# f.close()

digit=int(input("enter the number:"))
chr=(input("enter the chr:"))
sc=(input("enter the sc"))
if digit>=9 and digit<=0:
    print("digit")
    if chr<="a" and chr>="z" or chr<="A" and chr>="Z":
        print("characters")
        if sc=="@" and sc=="#" and sc=="$":
            print("special characters")
            sp=digit+chr+sc:
            print(sp)
        else:
            print("no")
    else:
        print("no")
else:
    print("no")   