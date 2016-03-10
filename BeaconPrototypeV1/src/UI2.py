from Tkinter import *#@UnusedWildImport
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")

fields=["Name:","Number:","Carrier:","Email:"]
entries=[]


def save_entry_fields():
    
    fileText=""
    for x in range(0,len(entries)):
        fileText=fileText+str(fields[x])+str(entries[x].get())+"\n"
    with open("C:\\Users\\Taylor\\Documents\\UI Files\\UI1.txt",'w') as myfile:
        myfile.write(fileText)
    master.destroy()
  

master = Tk()
for n in range(0,len(fields)):
    Label(master,text=fields[n]).grid(row=n)
    entries.append(n)
    entries[n]=Entry(master)
    entries[n].grid(row=n,column=1)
    
Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Save', command=save_entry_fields).grid(row=4, column=1, sticky=W, pady=4)

mainloop( )