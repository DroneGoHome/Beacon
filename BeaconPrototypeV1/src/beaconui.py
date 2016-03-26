from Tkinter import *#@UnusedWildImport
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")

master = Tk()
fields=["Shape:","Behavior:","Radius:","Retry:"]
shapes=["Other","Rectangle","Cylinder"]
behavior=["Land","RTL"]
menshape=StringVar()
menshape.set("Cylinder")
menbehave=StringVar()
menbehave.set("RTL")
menrad=StringVar()
menrad.set("15")
menretry=StringVar()
menretry.set("5")
def save_entry_fields():  
    fileText="Shape:"+menshape.get().upper()+"\n"+"Behavior:"+menbehave.get().upper()+"\n"+"Radius:"+menrad.get()+"\n"+"Retry:"+menretry.get()+"\n"
    with open("C:\\Users\\Taylor\\Documents\\UI Files\\BeaconUI.txt",'w') as myfile:
        myfile.write(fileText)
    master.destroy()

    


for field in range(0,len(fields)):
    Label(master,text=fields[field]).grid(row=field)
''' 
for shape in range(0,len(shapes)):
    shapeRB=Radiobutton(master,text=shapes[shape].upper(), variable=rbshape, value=shapes[shape].upper())
    shapeRB.grid(row=0,column=shape+1)
    Radiobutton.select(shapeRB)
    
for behave in range(0,len(behavior)):
    behaveRB=Radiobutton(master,text=behavior[behave].upper(), variable=rbbehave, value=behavior[behave].upper())
    behaveRB.grid(row=1,column=behave+1)
    Radiobutton.select(behaveRB)
    '''

OptionMenu(master, menshape, "Cylinder","Rectangle","Other").grid(row=0,column=1)
OptionMenu(master, menbehave, "RTL","Land").grid(row=1,column=1)
OptionMenu(master, menrad, 10,15,25,50,100).grid(row=2,column=1)
OptionMenu(master, menretry, 3,5,10).grid(row=3,column=1)
Button(master, text='Quit', command=master.quit).grid(row=len(fields)+1, column=0, sticky=W, pady=4,padx=4)
Button(master, text='Save', command=save_entry_fields).grid(row=len(fields)+1, column=1, sticky=W, pady=4)

mainloop()