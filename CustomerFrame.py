#!/usr/bin/python
import Tkinter
from Tkinter import StringVar, Label, RAISED, Toplevel, Button, Frame, Checkbutton, Entry, X, BOTH
from tkMessageBox import showinfo

from datastore import Customer

#extends the Frame class to inherit the mainloop function

class CustomerFrame(Frame):

	def __init__(self, master = None, **options):

		#construct the frame object
		Frame.__init__(self, master, **options)
		self.pack(expand=True, fill= BOTH)

		#self.master.minsize(400, 300)


		Label(self, text="Full Name").grid()
		Label(self, text="Email").grid()


		self.fn=StringVar()
		self.em=StringVar()
		self.fullname = Entry(self, textvariable = self.fn).grid(row=0, column=1)
		self.email = Entry(self, textvariable = self.em).grid(row=1, column=1)

		Button(self, text="Save", \
			command=self.saveCustData).grid(row=3, column=1, sticky = 'e')


	



	def saveCustData(self):

		self.fn = self.fn.get()
		self.em = self.em.get()

		
		newcust= Customer(name=self.fn, email=self.em)
		print newcust
		newcust.newCustomer()
		






	def new_window(self):
		top = Toplevel(master=self)
		b = Button(top, text = "Quit", \
			command=top.quit).pack()

	def popup(self):
		showinfo("Popup Title", "Error! not really")

if __name__ == "__main__":
	CustomerFrame().mainloop()

