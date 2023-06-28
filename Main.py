from tkinter import *
from tkinter import messagebox

items = []
item_dictionary = {}

root = Tk()
root.geometry('500x500')

def add_item():
    full_name = entry_full_name.get()
    receipt_number = entry_receipt_number.get()
    item = entry_item.get()
    quantity = entry_quantity.get()
    # Validate the input
    if not full_name:
        messagebox.showerror("Error", "Please enter customer full name.")
        return
    
    if not receipt_number.isdigit():
        messagebox.showerror("Error", "Please enter a valid receipt number.")
        return
    
    if not item:
        messagebox.showerror("Error", "Please enter the item that is hired.")
        return
    
    if not quantity.isdigit() or int(quantity) < 1 or int(quantity) > 500:
        messagebox.showerror("Error", "Please enter a valid quantity (1-500).")
        return
    new_item = f"{full_name} - {item} - {quantity} - {receipt_number}"
    items.append(new_item)
    listbox.insert(END, new_item)
        
def return_item():
    selection = listbox.curselection()
    if not selection:
        messagebox.showerror("Error", "Please select an item to return.")
        return
    
    listbox.delete(selection)

Entry_Frame = Frame(root, padx=10, pady=10)
Entry_Frame.grid(row=0,column=0, sticky=N)
Search_Frame = Frame(root, padx=10, pady=10)
Search_Frame.grid(row=0, column=1, sticky=N)
label_full_name = Label(Entry_Frame, text="Full Name:")
label_full_name.grid(row=1, column=0, padx=5, pady=5)
entry_full_name = Entry(Entry_Frame)
entry_full_name.grid(row=1, column=1)
label_receipt_number = Label(Entry_Frame, text="Receipt Number:")
label_receipt_number.grid(row=2, column=0, padx=5, pady=5)
entry_receipt_number = Entry(Entry_Frame)
entry_receipt_number.grid(row=2, column=1)
label_item = Label(Entry_Frame, text="Item:")
label_item.grid(row=3, column=0, padx=5, pady=5)
entry_item = Entry(Entry_Frame)
entry_item.grid(row=3, column=1)
label_quantity = Label(Entry_Frame, text="Quantity:")
label_quantity.grid(row=4, column=0, padx=5, pady=5)
entry_quantity = Entry(Entry_Frame)
entry_quantity.grid(row=4, column=1)

button_add = Button(Entry_Frame, text="Add", command=add_item)
button_add.grid(row=5, column=0, padx=5, pady=5)
button_remove = Button(Entry_Frame, text="Return", command=return_item)
button_remove.grid(row=5, column=1, padx=5, pady=5)

search_entry = Entry(Search_Frame)
search_entry.pack(pady=5)
search_label = Button(Search_Frame, text="Search")
search_label.pack(pady=5)
    
listbox = Listbox(Search_Frame, width=35)
listbox.pack()

root.mainloop()
