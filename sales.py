from tkinter import *
from tkinter import ttk


def v():
    root = Tk()
    root.title("BOOK SALES")
    root.geometry("600x250")
    root.configure(bg="#f5f5f5")

    style = ttk.Style()
    style.theme_use("alt")
    style.configure("TButton",foreground="White",background="#007acc",font=("Arial",10,"bold"))
    style.configure("TLabel", foreground="#333", font=("Arial", 10))
    style.configure("TCombobox", font=("Arial", 10))
    
    input_frame = Frame(root, bg="#f5f5f5")
    input_frame.grid(column=1,row=1,pady=20)
    pr = ttk.Label(root,text="150")
    pr.grid(row=0,column=2)
    l =  ttk.Label(input_frame,text="Select Item: ")
    l.grid(row=0,column=0 ,padx= 10, pady= 5,sticky=W)
    lq = ttk.Label(input_frame,text="Quantity:")
    lq.grid(row=0,column=1,padx=10,pady=5,sticky=W)
    
    def view():
        fram = Toplevel(root)
        fram.title("Saved Qunatities")
        fram.geometry("400x200")
        
        scrollbar = Scrollbar(fram)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(fram,yscrollcommand=scrollbar.set,
        font=("Helvetica",12),
        bg="#ffffff",
        fg="#333333",
        selectbackground="#cce5ff",
        selectforeground="#000000",
        relief=FLAT,
        borderwidth=2
        )
        with open("data/databook.csv","r") as file:
            content =  file.readlines()
        for i in content:
            mylist.insert(END, i.strip())
        mylist.pack(side=LEFT,fill=BOTH,expand=True)
        scrollbar.config(command=mylist.yview)
    def save():
        book = com.get()
        quan = int(quantity.get())
        f = False
        try:
            with open("data/databook.csv","r") as file:
                content = file.readlines()
    # print(content)
        except:
            with open("data/databook.csv","w") as file:
                for i in content:
                    if book != i.split(":")[0]:
                        print(book)
                        file.write(i)
                    elif book == i.split(":")[0]:
                        p =  int(i.split(":")[1]) 
                        p -= quan
                        p1 += quan 
                        file.write(f"{book.split(":")[0]}:{p}\n")
                        with open("data/sale.csv","a") as file1 :
                            file1.writelines(f"{book.split(":")[0]},{quan}\n") 
                    f = True
            # with open("data/databook.csv","") as file:
            #     content = file.readlines()
        with open("data/databook.csv","r") as file:
                content = file.readlines()
        with open("data/databook.csv","w") as file:
            for i in content:
                if book != i.split(":")[0]:
                    print(book)
                    file.write(i)
                elif book == i.split(":")[0]:
                    p =  int(i.split(":")[1]) 
                    p -= quan
                    file.write(f"{book.split(":")[0]}:{p}\n")
                    with open("data/sale.csv","a") as file1 :
                        file1.writelines(f"{book.split(":")[0]},{quan}\n") 
                    f = True
            if not f:
                file.write(f"{book}:{quan}")
        quantity.delete(0,END)
    def select(event):
        selectitem = com.get()
        l.config(text="select Item: " + selectitem)
    with open("data/data.csv","r") as file:
        con = file.readlines()
        content = [i.strip().split(",") for i in con]
        
    list = []
    for i in content:
        list.append(i[0].split(":")[0])

    quantity = Entry(input_frame,font=("Arial",10))
    quantity.grid(row=1,column=1,padx=5,pady=5)
    com= ttk.Combobox(input_frame,values=list,state='readonly')
    com.grid(row=1,column=0, padx=5,pady=5)
    com.set(list[0])
    com.bind("<<ComboboxSelected>>",select)
    busave = ttk.Button(input_frame,text= 'Save', width=15,command=save)
    busave.grid(row=2,column=1,pady=10)
    vbu =  ttk.Button(input_frame,text="View quantity",width=15,command=view)
    vbu.grid(row = 3, column=2 ,padx=10)
    
    root.mainloop()