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

""" function multiply
    get : n1, n2
    return: n1 * n2
"""
def multiply():
    result.set( float(n1.get()) * float(n2.get()) )
    delete()

""" function division
    get : n1, n2
    return: n1 / n2
"""
def division():
    result.set( float(n1.get()) / float(n2.get()) )
    delete()

""" function delete
    clear variable
"""
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



Entry(root, justify="center", textvariable=n1).pack(pady=5, expand=1)

Entry(root, justify="center", textvariable=n2).pack(pady=5, expand=1)


Label(root,text="=").pack( expand=1)

Entry(root, justify="center", textvariable=result, state="disabled").pack(padx=10, expand=1)

#Button

Button(root, background="white", fg="blue", font="bold", text="+", command=add).pack(side="left", padx=5, expand=1)
Button(root, background="white", fg="blue", font="bold", text="-", command=subtract).pack(side="left", padx=5, expand=1)
Button(root, background="white", fg="blue", font="bold", text="*", command=multiply).pack(side="left", padx=5, expand=1)
Button(root, background="white", fg="blue", font="bold", text="/", command=division).pack(side="left", padx=5, expand=1)



# bucle
root.mainloop()