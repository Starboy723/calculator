from tkinter import *
win=Tk()
		
def bclick(num):
	fnum=lab.get()
	lab.delete(0,END)
	try:
		if num=='+'or num=='-' or num=='*' or num=='/' or num=='%':
			if fnum[-1]=='+' or fnum[-1]=='-' or fnum[-1]=='*' or fnum[-1]=='/' or fnum[-1]=='%':
				fnum=fnum.replace(fnum[-1],'')
		enum=fnum+num
		lab.insert(0,enum)
	except:
		lab.insert(0,'')
	
def equal():
	try:
		result=eval(lab.get())
		lab.delete(0,END)
		lab.insert(0,result)
	except:
		lab.insert(0,"")
	
#widgets.
lab=Entry(win,width=10,font=("Arial",30),justify=RIGHT)
button7=Button(win,text="7",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("7"),activeforeground="white",activebackground="grey",relief=SOLID)
button8=Button(win,text="8",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("8"),relief=SOLID,activeforeground="white",activebackground="grey")
button9=Button(win,text="9",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("9"),relief=SOLID,activeforeground="white",activebackground="grey")
button4=Button(win,text="4",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("4"),relief=SOLID,activeforeground="white",activebackground="grey")
button5=Button(win,text="5",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("5"),relief=SOLID,activeforeground="white",activebackground="grey")
button6=Button(win,text="6",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("6"),relief=SOLID,activeforeground="white",activebackground="grey")
button1=Button(win,text="1",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("1"),activeforeground="white",activebackground="grey",relief=SOLID)
button2=Button(win,text="2",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("2"),activeforeground="white",activebackground="grey",relief=SOLID)
button3=Button(win,text="3",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("3"),activeforeground="white",activebackground="grey",relief=SOLID)
button0=Button(win,text="0",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("0"),activeforeground="white",activebackground="grey" ,relief=SOLID)
badd=Button(win,text="+",font=("Arial",15),padx=100,pady=60,command=lambda:bclick("+"),activeforeground="white",activebackground="grey",relief=SOLID)
bsub=Button(win,text="-",font=("Arial",15),padx=120,pady=60,command=lambda:bclick("-"),activeforeground="white",activebackground="grey",relief=SOLID)
bmul=Button(win,text="*",font=("Arial",15),padx=120,pady=60,command=lambda:bclick("*"),activeforeground="white",activebackground="grey",relief=SOLID)
bdiv=Button(win,text="÷",font=("Arial",15),padx=115,pady=60,command=lambda:bclick("/"),activeforeground="white",activebackground="grey",relief=SOLID)
bmod=Button(win,text="%",font=("Arial",15),padx=115,pady=60,command=lambda:bclick("%"),activeforeground="white",activebackground="grey",relief=SOLID)
bclear=Button(win,text="clear",font=("Arial",15),padx=210,pady=60,command=lambda:lab.delete(0,END),activeforeground="white",activebackground="grey",relief=SOLID)
bequal=Button(win,text="=",font=("Arial",15),padx=275,pady=180,command=equal,activeforeground="white",activebackground="grey",relief=SOLID)
#packing
lab.grid(row=0,column=0,columnspan=15,padx=60,pady=30)
button7.grid(row=1,column=0,padx=50)
button8.grid(row=1,column=1,padx=50)
button9.grid(row=1,column=2,padx=60)
button4.grid(row=2,column=0,pady=30)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button1.grid(row=3,column=0,pady=30)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button0.grid(row=4,column=1,pady=30)
badd.grid(row=4,column=2)
bsub.grid(row=4,column=0)
bmul.grid(row=5,column=0)
bdiv.grid(row=6,column=0,pady=30)
bmod.grid(row=7,column=0,)
bclear.grid(row=5,column=1,columnspan=5)
bequal.grid(row=6,column=1,columnspan=5,rowspan=2)
win.mainloop()