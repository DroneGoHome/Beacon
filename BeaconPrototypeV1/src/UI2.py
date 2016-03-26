from Tkinter import *#@UnusedWildImport
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")

master = Tk()
fields=["Name:","Number:","Email:"]
carriers=["verizon","at&t","boost","sprint","t-mobile","virgin mobile","none"]
entries=[]
rbsel=StringVar()
def save_entry_fields():  
    fileText=""
    for x in range(0,len(entries)):
        fileText=fileText+str(fields[x])+str(entries[x].get())+"\n"
    fileText=fileText+"Carrier:"+rbsel.get().upper()+"\n"
    with open("C:\\Users\\Taylor\\Documents\\UI Files\\UI1.txt",'w') as myfile:
        myfile.write(fileText)
    master.destroy()

    


for field in range(0,len(fields)):
    Label(master,text=fields[field]).grid(row=field)
    entries.append(field)
    entries[field]=Entry(master)
    entries[field].grid(row=field,column=1)
 
for carrier in range(0,len(carriers)):
    carrierRB=Radiobutton(master,text=carriers[carrier].upper(), variable=rbsel, value=carriers[carrier].upper())
    carrierRB.grid(row=len(entries),column=carrier)
    Radiobutton.select(carrierRB)


Button(master, text='Quit', command=master.quit).grid(row=len(entries)+1, column=0, sticky=W, pady=4)
Button(master, text='Save', command=save_entry_fields).grid(row=len(entries)+1, column=1, sticky=W, pady=4)

mainloop()