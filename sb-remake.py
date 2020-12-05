#sb.cpp remake (v.2 improved code)
#Made by William Wei
import time
p=str(input("Please enter a name: "))
if p=="YHN" or p=="YHNdnzj" or p=="Mike Yuan" or p=="yhn" or p=="yhndnzj" or p=="mike yuan":
	#That's the best I can do. Using a lot of "or"s.
	print(p,"is totally an SB.")
	ans=str(input("Do you want to upgrade his/her brain? (Y/n):"))
	if ans=="" or ans=="y" or ans=="Y":
		for i in range(1,6):
			i=str(i)
			print("Attempting to upgrade his/her brain...(" + i + "/5)")
			time.sleep(1)
		print("E: Failed to upgrade his/her brain: Object is too dumb")
		print(p + "'s brain has been permanently damaged!")
	elif ans=="n" or ans=="N":
		print("Canceled upgrade,",p,"will be an SB forever!")
	else:
		print("Invalid choice!")
else:
	print(p,"is not an SB.")
input("Press Enter to exit...")
