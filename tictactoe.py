from tkinter import *
import tkinter.messagebox as msg
import random

bt={}
bt_obj=[]

def smartplay(played):
	global bt_obj
	
	if played != 4 and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
	
	elif len(bt_obj)==8 and played==4:
		choice=random.choice([bt[0], bt[2], bt[6], bt[8]])
		choice["image"]=circle
		bt_obj.remove(choice)
		
	elif (bt[0]["image"]==bt[8]["image"]=="pyimage1" or bt[2]["image"]==bt[6]["image"]=="pyimage1") and len(bt_obj)==6 :
		choice=random.choice([bt[1], bt[3], bt[5], bt[7]])
		choice["image"]=circle
		bt_obj.remove(choice)
		
	elif (bt[0]["image"]==bt[8]["image"]=="pyimage2" or bt[2]["image"]==bt[6]["image"]=="pyimage2") and played in [0, 2, 6, 8] and len(bt_obj)==6 and bt[4]["image"]=="pyimage1":
		for i in [bt[0], bt[2], bt[6], bt[8]]:
			if i in bt_obj:
				i["image"]=circle
				bt_obj.remove(i)
				break
				
	elif bt[0]["image"]==bt[1]["image"]=="pyimage3" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[1]["image"]==bt[2]["image"]=="pyimage3" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
	
	elif bt[0]["image"]==bt[2]["image"]=="pyimage3" and bt[1]["image"]=="pyimage2":
		bt[1]["image"]=circle
		bt_obj.remove(bt[1])
		
	elif bt[3]["image"]==bt[4]["image"]=="pyimage3" and bt[5]["image"]=="pyimage2":
		bt[5]["image"]=circle
		bt_obj.remove(bt[5])
		
	elif bt[4]["image"]==bt[5]["image"]=="pyimage3" and bt[3]["image"]=="pyimage2":
		bt[3]["image"]=circle
		bt_obj.remove(bt[3])
		
	elif bt[3]["image"]==bt[5]["image"]=="pyimage3" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[6]["image"]==bt[7]["image"]=="pyimage3" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[7]["image"]==bt[8]["image"]=="pyimage3" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[6]["image"]==bt[8]["image"]=="pyimage3" and bt[7]["image"]=="pyimage2":
		bt[7]["image"]=circle
		bt_obj.remove(bt[7])
	
	elif bt[0]["image"]==bt[3]["image"]=="pyimage3" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[3]["image"]==bt[6]["image"]=="pyimage3" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
		
	elif bt[0]["image"]==bt[6]["image"]=="pyimage3" and bt[3]["image"]=="pyimage2":
		bt[3]["image"]=circle
		bt_obj.remove(bt[3])
		
	elif bt[1]["image"]==bt[4]["image"]=="pyimage3" and bt[7]["image"]=="pyimage2":
		bt[7]["image"]=circle
		bt_obj.remove(bt[7])
		
	elif bt[4]["image"]==bt[7]["image"]=="pyimage3" and bt[1]["image"]=="pyimage2":
		bt[1]["image"]=circle
		bt_obj.remove(bt[1])
		
	elif bt[1]["image"]==bt[7]["image"]=="pyimage3" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[2]["image"]==bt[5]["image"]=="pyimage3" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[5]["image"]==bt[8]["image"]=="pyimage3" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[2]["image"]==bt[8]["image"]=="pyimage3" and bt[5]["image"]=="pyimage2":
		bt[5]["image"]=circle
		bt_obj.remove(bt[5])
		
	elif bt[0]["image"]==bt[4]["image"]=="pyimage3" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[4]["image"]==bt[8]["image"]=="pyimage3" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
		
	elif bt[0]["image"]==bt[8]["image"]=="pyimage3" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[2]["image"]==bt[4]["image"]=="pyimage3" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[4]["image"]==bt[6]["image"]=="pyimage3" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[2]["image"]==bt[6]["image"]=="pyimage3" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
		
		
		
	elif bt[0]["image"]==bt[1]["image"]=="pyimage1" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[1]["image"]==bt[2]["image"]=="pyimage1" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
	
	elif bt[0]["image"]==bt[2]["image"]=="pyimage1" and bt[1]["image"]=="pyimage2":
		bt[1]["image"]=circle
		bt_obj.remove(bt[1])
		
	elif bt[3]["image"]==bt[4]["image"]=="pyimage1" and bt[5]["image"]=="pyimage2":
		bt[5]["image"]=circle
		bt_obj.remove(bt[5])
		
	elif bt[4]["image"]==bt[5]["image"]=="pyimage1" and bt[3]["image"]=="pyimage2":
		bt[3]["image"]=circle
		bt_obj.remove(bt[3])
		
	elif bt[3]["image"]==bt[5]["image"]=="pyimage1" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[6]["image"]==bt[7]["image"]=="pyimage1" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[7]["image"]==bt[8]["image"]=="pyimage1" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[6]["image"]==bt[8]["image"]=="pyimage1" and bt[7]["image"]=="pyimage2":
		bt[7]["image"]=circle
		bt_obj.remove(bt[7])
	
	elif bt[0]["image"]==bt[3]["image"]=="pyimage1" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[3]["image"]==bt[6]["image"]=="pyimage1" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
		
	elif bt[0]["image"]==bt[6]["image"]=="pyimage1" and bt[3]["image"]=="pyimage2":
		bt[3]["image"]=circle
		bt_obj.remove(bt[3])
		
	elif bt[1]["image"]==bt[4]["image"]=="pyimage1" and bt[7]["image"]=="pyimage2":
		bt[7]["image"]=circle
		bt_obj.remove(bt[7])
		
	elif bt[4]["image"]==bt[7]["image"]=="pyimage1" and bt[1]["image"]=="pyimage2":
		bt[1]["image"]=circle
		bt_obj.remove(bt[1])
		
	elif bt[1]["image"]==bt[7]["image"]=="pyimage1" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[2]["image"]==bt[5]["image"]=="pyimage1" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[5]["image"]==bt[8]["image"]=="pyimage1" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[2]["image"]==bt[8]["image"]=="pyimage1" and bt[5]["image"]=="pyimage2":
		bt[5]["image"]=circle
		bt_obj.remove(bt[5])
		
	elif bt[0]["image"]==bt[4]["image"]=="pyimage1" and bt[8]["image"]=="pyimage2":
		bt[8]["image"]=circle
		bt_obj.remove(bt[8])
		
	elif bt[4]["image"]==bt[8]["image"]=="pyimage1" and bt[0]["image"]=="pyimage2":
		bt[0]["image"]=circle
		bt_obj.remove(bt[0])
		
	elif bt[0]["image"]==bt[8]["image"]=="pyimage1" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])
		
	elif bt[2]["image"]==bt[4]["image"]=="pyimage1" and bt[6]["image"]=="pyimage2":
		bt[6]["image"]=circle
		bt_obj.remove(bt[6])
		
	elif bt[4]["image"]==bt[6]["image"]=="pyimage1" and bt[2]["image"]=="pyimage2":
		bt[2]["image"]=circle
		bt_obj.remove(bt[2])
		
	elif bt[2]["image"]==bt[6]["image"]=="pyimage1" and bt[4]["image"]=="pyimage2":
		bt[4]["image"]=circle
		bt_obj.remove(bt[4])	
		
	elif (bt[0]["image"]=="pyimage1" or bt[2]["image"]=="pyimage1" or bt[6]["image"]=="pyimage1" or bt[8]["image"]=="pyimage1") and (bt[1]["image"]=="pyimage1" or bt[3]["image"]=="pyimage1" or bt[5]["image"]=="pyimage1" or bt[7]["image"]=="pyimage1") and len(bt_obj)==6 :
		for i in [bt[0], bt[2], bt[6], bt[8]]:
			if i==bt[0] and bt[8]["image"]=="pyimage1" and i in bt_obj:
				bt[0]["image"]=circle
				bt_obj.remove(i)
				break
			elif i==bt[2] and bt[6]["image"]=="pyimage1" and i in bt_obj:
				bt[2]["image"]=circle
				bt_obj.remove(i)
				break
			elif i==bt[6] and bt[2]["image"]=="pyimage1" and i in bt_obj:
				bt[6]["image"]=circle
				bt_obj.remove(i)
				break
			elif i==bt[8] and bt[0]["image"]=="pyimage1" and i in bt_obj:
				bt[8]["image"]=circle
				bt_obj.remove(i)
				break
			else:
				pass	
		
	else:
		botchoice=random.choice(bt_obj)
		botchoice["image"]=circle
		bt_obj.remove(botchoice)


def final():
	global bt_obj
	quitchoice=msg.askquestion("Match Over", "Do you want to quit?")
	if quitchoice=='yes':
		quit()
	else:
		bt_obj=list(bt.values())
		for obj in bt_obj:
			obj["image"]=blank
			obj["bg"]="white"
	
def final_result():
	if result():
		final()
		return True
	else:
		return False

def play(event):

	if event.widget["image"]=="pyimage2":
		global bt_obj
			
		bt_values=list(bt.values())

		if len(bt_obj)==0:
			bt_obj=list(bt.values())
		
		event.widget["image"]=cross
		bt_obj.remove(event.widget)
		
		if final_result():
			return
		"""	
		botchoice=random.choice(bt_obj)
		botchoice["image"]=circle
		bt_obj.remove(botchoice)
		"""
		smartplay(bt_values.index(event.widget))
		
		if final_result():
			return
		
		if len(bt_obj)==1:
			bt_obj[0]["image"]=cross
			bt_obj=[]
			final_result()
			
	
def result():
	if bt[0]["image"]==bt[1]["image"]==bt[2]["image"]=="pyimage1":
		bt[0]["bg"]=bt[1]["bg"]=bt[2]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[3]["image"]==bt[4]["image"]==bt[5]["image"]=="pyimage1":
		bt[3]["bg"]=bt[4]["bg"]=bt[5]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[6]["image"]==bt[7]["image"]==bt[8]["image"]=="pyimage1":
		bt[6]["bg"]=bt[7]["bg"]=bt[8]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[0]["image"]==bt[3]["image"]==bt[6]["image"]=="pyimage1":
		bt[0]["bg"]=bt[3]["bg"]=bt[6]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[1]["image"]==bt[4]["image"]==bt[7]["image"]=="pyimage1":
		bt[1]["bg"]=bt[4]["bg"]=bt[7]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[2]["image"]==bt[5]["image"]==bt[8]["image"]=="pyimage1":
		bt[2]["bg"]=bt[5]["bg"]=bt[8]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[0]["image"]==bt[4]["image"]==bt[8]["image"]=="pyimage1":
		bt[0]["bg"]=bt[4]["bg"]=bt[8]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[2]["image"]==bt[4]["image"]==bt[6]["image"]=="pyimage1":
		bt[2]["bg"]=bt[4]["bg"]=bt[6]["bg"]="green"
		msg.showinfo("Won", "Hurrah! you won the match.")
		return True
	elif bt[0]["image"]==bt[1]["image"]==bt[2]["image"]=="pyimage3":
		bt[0]["bg"]=bt[1]["bg"]=bt[2]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[3]["image"]==bt[4]["image"]==bt[5]["image"]=="pyimage3":
		bt[3]["bg"]=bt[4]["bg"]=bt[5]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[6]["image"]==bt[7]["image"]==bt[8]["image"]=="pyimage3":
		bt[6]["bg"]=bt[7]["bg"]=bt[8]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[0]["image"]==bt[3]["image"]==bt[6]["image"]=="pyimage3":
		bt[0]["bg"]=bt[3]["bg"]=bt[6]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[1]["image"]==bt[4]["image"]==bt[7]["image"]=="pyimage3":
		bt[1]["bg"]=bt[4]["bg"]=bt[7]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[2]["image"]==bt[5]["image"]==bt[8]["image"]=="pyimage3":
		bt[2]["bg"]=bt[5]["bg"]=bt[8]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[0]["image"]==bt[4]["image"]==bt[8]["image"]=="pyimage3":
		bt[0]["bg"]=bt[4]["bg"]=bt[8]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt[2]["image"]==bt[4]["image"]==bt[6]["image"]=="pyimage3":
		bt[2]["bg"]=bt[4]["bg"]=bt[6]["bg"]="red"
		msg.showinfo("Lose", "Alas! you lost the match.")
		return True
	elif bt_obj==[]:
		for i in range(len(bt)):
			if bt[i]["image"]=="pyimage3":
				bt[i]["bg"]="yellow"
			else:
				bt[i]["bg"]="blue"
		msg.showinfo("Tied", "Match has been Tied!")
		return True
	else:
		return False
	
if __name__=="__main__":	
		
	root=Tk()
	
	root.title("TicTacToe - By Hammad Ali")
	root.geometry("636x636")
	root.maxsize(636,636)
	root.minsize(636,636)
	
	chance=StringVar()
	chance.set("")
	cross=PhotoImage(file="x-mark-128.png")
	blank=PhotoImage(file="blank.png")
	circle=PhotoImage(file="circle-outline-128.png")
	
	f1=Frame(root, bg="Black")
	f1.pack(side=TOP, fill=X)
	
	bt[0]=Button(f1, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[0].bind("<Button-1>", play)
	bt[0].pack(side=LEFT)
	
	bt[1]=Button(f1, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[1].bind("<Button-1>", play)
	bt[1].pack(side=LEFT)
	
	bt[2]=Button(f1, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[2].bind("<Button-1>", play)
	bt[2].pack(side=LEFT)
	
	f2=Frame(root, bg="Black")
	f2.pack(side=TOP, fill=X)
	
	bt[3]=Button(f2, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[3].bind("<Button-1>", play)
	bt[3].pack(side=LEFT)
	
	bt[4]=Button(f2, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[4].bind("<Button-1>", play)
	bt[4].pack(side=LEFT)
	
	bt[5]=Button(f2, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[5].bind("<Button-1>", play)
	bt[5].pack(side=LEFT)
	
	f3=Frame(root, bg="Black")
	f3.pack(side=TOP, fill=X)
	
	bt[6]=Button(f3, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[6].bind("<Button-1>", play)
	bt[6].pack(side=LEFT)
	
	bt[7]=Button(f3, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[7].bind("<Button-1>", play)
	bt[7].pack(side=LEFT)
	
	bt[8]=Button(f3, textvariable=chance, padx=3, pady=3, height=206, width=206, image=blank)
	bt[8].bind("<Button-1>", play)
	bt[8].pack(side=LEFT)
	
	root.mainloop()