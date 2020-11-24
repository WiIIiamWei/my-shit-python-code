a=[6,2,5,5,4,5,6,3,7,9]
num=int(input("Please input a number:"))
num=list(str(num))
total=0
for i in range(len(num)):
    total=total+a[int(num[i])]
print("Total match used:",total)
input("Press Enter to exit...")
