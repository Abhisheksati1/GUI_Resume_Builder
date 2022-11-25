from tkinter import *
from tkinter import ttk

def Show():
    E1.delete("1.0",END)
    s="\t           MY RESUME \n"
    line="\n"+"*"*60
    s+=line+"\n"
    s+="\n Name: "+T1.get()+"\n"
    s+="\n Age: "
    s+=S1.get()
    s+="\n"
    qu=Li1.curselection()
    s+="\n Qualification: \n"
    for i in qu:
        s+="\t          "
        s+=Li1.get(i)
        s+="\n"
    s+="\n Gender: "
    if r.get()==1:
        s+="Male"
        s+="\n"
    else:
        s+="Female"
        s+="\n"
    s+="\n Marital Status:  "
    if d.get()==1:
        s+="Marride \n"
    else:
        s+="Unmarride \n"
    s+="\n Country: "
    s+=t.get()
    s+"\n"
    s+="\n"+"*"*60
    s+="\n"
    s+="\t     THANK YOU    "
    E1.insert(END,s)

root=Tk()
root.title("RESUME BUILDER")
root.geometry("900x600")

r=IntVar()
d=IntVar()
t=StringVar()

L1=Label(root,text="RESUME BUILDER",font=('Arial',25),bg="Black",fg="White")
L2=Label(root,text="Name",font=('Arial',10))
L3=Label(root,text="Gender",font=('Arial',10))
L4=Label(root,text="Marital Status",font=('Arial',10))
L5=Label(root,text="Country",font=('Arial',10))
L6=Label(root,text="Qualification",font=('Arial',10))
L7=Label(root,text="Age",font=('Arial',10))
L1.grid(row=0,column=1)
L2.grid(row=1,column=0)
L3.grid(row=2,column=0)
L4.grid(row=3,column=0)
L5.grid(row=4,column=0)
L6.grid(row=5,column=0)
L7.grid(row=6,column=0)

T1=Entry(root,width=50)
T1.grid(row=1,column=1)

R1=Radiobutton(root,text="Male",variable=r,value=1)
R2=Radiobutton(root,text="Female",variable=r,value=2)
R1.grid(row=2,column=1)
R2.grid(row=2,column=2)

C1=Checkbutton(root,text="Married",variable=d)
C1.grid(row=3,column=1)

Cb1=ttk.Combobox(root,textvariable=t)
Cb1['values']=("India","Pakistan","China","Nepal","Japan","USA","Bangladesh","Bhutan")
Cb1.grid(row=4,column=1)

Li1=Listbox(root,selectmode=MULTIPLE)
Li1.insert(1,"10")
Li1.insert(2,"10+2")
Li1.insert(3,"Btech")
Li1.insert(4,"BCA")
Li1.insert(5,"MCA")
Li1.insert(6,"B.com")
Li1.insert(7,"BSC")
Li1.insert(8,"Others")
Li1.grid(row=5,column=1)

S1=Spinbox(root,from_=1, to=80)
S1.grid(row=6,column=1)

B1=Button(root,text="Show",command=Show)
B1.grid(row=7,column=0)

E1=Text(root,height=30,width=45,bg="Black",fg="White",font='Arial')
E1.grid(row=0,column=3,rowspan=8)

root.mainloop()
