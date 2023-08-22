from tkinter import *




""" function add 
    get : n1, n2
    return: n1 + n2
"""
def add():
    result.set( float(n1.get()) + float(n2.get()) )
    delete()


""" function subtract
    get : n1, n2
    return: n1 - n2
"""
def subtract():
    result.set( float(n1.get()) - float(n2.get()) )
    delete()

def multiple():
    result.set( float(n1.get()) * float(n2.get()) )
    delete()

def split():
    result.set( float(n1.get()) / float(n2.get()) )
    delete()

def delete():
    n1.set("")
    n2.set("")

# set root
root = Tk()
root.title("Calculator")
root.config(bd=50)
root.config(bg="lightblue")
root.config(relief="sunken") 


#variables
n1 = StringVar()
n2 = StringVar()
result = StringVar()



Entry(root, justify="center", textvariable=n1).pack(pady=5)



Entry(root, justify="center", textvariable=n2).pack(pady=5)

Label(root,text="=").pack()
Entry(root, justify="center", textvariable=result, state="disabled").pack(padx=10)

#Button
Button(root, background="white", font="bold", text="+", command=add).pack(side="left", padx=5)
Button(root, background="white", font="bold", text="-", command=subtract).pack(side="left", padx=5)
Button(root, background="white", font="bold", text="*", command=multiple).pack(side="left", padx=5)
Button(root, background="white", font="bold", text="/", command=split).pack(side="left", padx=5)



# bucle
root.mainloop()