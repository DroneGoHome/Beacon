from Tkinter import *
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")

def save_entry_fields():
    with open("C:\\Users\\Taylor\\Documents\\UI Files\\UI1.txt",'w') as myfile:
        myfile.write("Name:%s\nPhone Number:%s\nCellular Provider:%s\nEmail:%s" %(e1.get(), e2.get(),e3.get(),e4.get()))
    master.destroy()

master = Tk()
Label(master, text="Name:   ").grid(row=0)
Label(master, text="Phone Number:   ").grid(row=1)
Label(master, text="Cellular Provider:   ").grid(row=2)
Label(master, text="Email:   ").grid(row=3)
e1=Entry(master)
e1.grid(row=0, column=1)
e2=Entry(master)
e2.grid(row=1, column=1)
e3=Entry(master)
e3.grid(row=2, column=1)
e4=Entry(master)
e4.grid(row=3, column=1)

Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Save', command=save_entry_fields).grid(row=4, column=1, sticky=W, pady=4)

mainloop( )