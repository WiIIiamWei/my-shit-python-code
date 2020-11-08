#Completely useless stream bot for osu! by William Wei
import time
print("Welcome to use Stream Bot!")
bpm=float(input("Please input song BPM: "))
cnt=float(input("Please input total notes count: "))
ch=[0.125,0.03125,0.0625,0.125,0.25,0.5,1]
dmc=(input("Please input stream tempo [1]1/32 [2]1/16 [3]1/8 [4]1/4 [5]1/2 [6]1, Default 1/8: "))
if dmc=="":
	dmc=0
else:
	dmc=int(dmc)
t=60/bpm*(ch[dmc])
interval=t*(cnt-1)
sec=t
cnts=cnt
print("Calculated press interval:",sec,"seconds.")
#The following conversion code is from the Internet.
def convert(t): 
	t = t % (24 * 3600) 
	hour = t // 3600
	t %= 3600
	minutes = t // 60
	t %= 60
	return "%d:%02d:%02d" % (hour, minutes, t)
bpm=str(bpm)
cnt=str(cnt)
txt=str(("You entered "+bpm+" BPM and "+cnt+" notes. Estimated finish time is "+convert(interval)+". Press Enter to start..."))
input(txt)
if cnts%2==1:
	for i in range(int(cnts/2)):
		print("z")
		time.sleep(sec)
		print("x")
		time.sleep(sec)
else:
	for i in range(int((cnts-1)/2)):
		print("z")
		time.sleep(sec)
		print("x")
		time.sleep(sec)
	print("z")
print("Stream ended. I gave that an 800pp.")
input("Press Enter to exit...")
