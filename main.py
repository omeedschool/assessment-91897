from tkinter import *
from tkinter import messagebox

class PartyHire():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Party Hire")

        #Create labels and entry fields
        self.label_full_name = Label(root, text="Full Name:")
        self.label_full_name.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.entry_full_name = Entry(root)
        self.entry_full_name.grid(row=0, column=1, columnspan=2)

        self.label_receipt_number = Label(root, text="Receipt Number:")
        self.label_receipt_number.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        self.entry_receipt_number = Entry(root)
        self.entry_receipt_number.grid(row=1, column=1, columnspan=2)

        self.label_item = Label(root, text="Item:")
        self.label_item.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        self.entry_item = Entry(root)
        self.entry_item.grid(row=2, column=1, columnspan=2)

        self.label_quantity = Label(root, text="Quantity:")
        self.label_quantity.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
        self.entry_quantity = Entry(root)
        self.entry_quantity.grid(row=3, column=1, columnspan=2)

        #Create buttons
        self.button_add = Button(root, text="Submit", command=self.add_item)
        self.button_add.grid(row=4, column=0, padx=5, pady=5)

        self.button_remove = Button(root, text="Return", command=self.return_item)
        self.button_remove.grid(row=4, column=1, padx=5, pady=5)

        pass

    def add_item():
        pass

    def return_item():
        pass

root = Tk()
root.geometry(400)
window = PartyHire(root)
root.mainloop()