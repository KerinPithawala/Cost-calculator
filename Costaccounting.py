import tkinter as t
#Main Window for storing components
w1=t.Tk()
w1.title("Cost accounting calculator")
#Creating Labels and text fields for GUI Input and Output
l2=t.Label(w1,text="Opening Stock of raw materials")
l2.grid(column=0,row=0)
tf1=t.Entry(w1)
tf1.grid(column=1,row=0)
l3=t.Label(w1,text="Closing Stock of raw materials")
l3.grid(column=0,row=1)
tf2=t.Entry(w1)
tf2.grid(column=1,row=1)
l4=t.Label(w1,text="Materials purchased")
l4.grid(column=0,row=2)
tf3=t.Entry(w1)
tf3.grid(column=1,row=2)
l5=t.Label(w1,text="Carriage Inward")
l5.grid(column=0,row=3)
tf4=t.Entry(w1)
tf4.grid(column=1,row=3)
tf5=t.Entry(w1)
tf5.grid(column=1,row=4)
l6=t.Label(w1,text="Direct Wages")
l6.grid(column=0,row=5)
tf6=t.Entry(w1)
tf6.grid(column=1, row=5)
l7=t.Label(w1,text="Direct Expenses")
l7.grid(column=0,row=6)
tf7=t.Entry(w1)
tf7.grid(column=1, row=6)
tf8=t.Entry(w1)
tf8.grid(column=1,row=7)
l8=t.Label(w1,text="Enter factory overheads")
l8.grid(column=0,row=8)
tf9=t.Entry(w1)
tf9.grid(column=1,row=8)
tf10=t.Entry(w1)
tf10.grid(column=1,row=9)
l9=t.Label(w1,text="Office and Administration overheads")
l9.grid(column=0,row=10)
tf11=t.Entry(w1)
tf11.grid(column=1,row=10)
tf12=t.Entry(w1)
tf12.grid(column=1,row=11)

l10=t.Label(w1,text="Selling and distribution overheads")
l10.grid(column=0,row=12)
tf13=t.Entry(w1)
tf13.grid(column=1,row=12)
l11=t.Label(w1,text="Opening stock of finished goods")
l11.grid(column=0,row=13)
tf14=t.Entry(w1)
tf14.grid(column=1,row=13)
l12=t.Label(w1,text="Closing stock of finished goods")
l12.grid(column=0,row=14)
tf15=t.Entry(w1)
tf15.grid(column=1,row=14)



tf16=t.Entry(w1)
tf16.grid(column=1,row=15)

l13=t.Label(w1,text="Enter Profit")
l13.grid(column=0,row=16)
tf17=t.Entry(w1)
tf17.grid(column=1,row=16)
tf18=t.Entry(w1)
tf18.grid(column=1, row=17)

#Declaring functions
#For calculating materials consumed
def ms():
    num1=float(tf1.get())
    num2=float(tf2.get())
    num3=float(tf3.get())
    num4=float(tf4.get())
    sum1=str(num1-num2+num3+num4)
    tf5.insert(0,sum1)
#For calculating Prime Cost
def pc():
    num1=float(tf1.get())
    l=[]
    for i in (tf7.get().split(" ")):
        l.append(float(i))
    num3=float(tf5.get())
    sum2=num1+sum(l)+num3
    tf8.insert(0,sum2)
#For calculating Factory Cost
def fc():
    l1=[]
    for i in (tf9.get().split(" ")):
        l1.append(float(i))
    sum3=float(tf8.get())+sum(l1)
    tf10.insert(0,sum3)
#For calculating cost of production
def cp():
    l2=[]
    for i in (tf11.get().split(" ")):
        l2.append(float(i))
    sum4=float(tf10.get())+sum(l2)
    tf12.insert(0,sum4)

def tc():
    l3=[]
    for i in (tf13.get().split(" ")):
        l3.append(float(i))
    sum5=float(tf12.get())+sum(l3)+float(tf14.get())-float(tf15.get())
    tf16.insert(0,sum5)

def ts():
    sum6=float(tf16.get())+float(tf17.get())
    tf18.insert(0,sum6)

#Declaring buttons
b1=t.Button(w1, text="Calculate materials comsumed",command=ms)
b1.grid(column=0,row=4)
b2=t.Button(w1,text="Calculate Prime cost",command=pc)
b2.grid(column=0,row=7)
b3=t.Button(w1,text="Calculate Factory Cost", command=fc)
b3.grid(column=0, row=9)
b4=t.Button(w1,text="Calculation Cost of Production", command=cp)
b4.grid(column=0,row=11)
b4=t.Button(w1,text="Total cost", command=tc)
b4.grid(column=0,row=15)
b5=t.Button(w1,text="Total Sales",command=ts)
b5.grid(column=0,row=17)



w1.mainloop()
    
    
    
    
