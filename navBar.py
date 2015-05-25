#!/usr/bin/python
import Tkinter
from Tkinter import StringVar, Label, RAISED, GROOVE, Toplevel, Button, Frame, Checkbutton, Entry, X, BOTH, CENTER
from tkMessageBox import showinfo


class navBar(Frame):

	def __init__(self, master=None, **options):

		Frame.__init__(self, master, **options)
		self.pack(fill='x')

		Label(self, text="Dash Navigation").grid(rowspan=1, columnspan=6, sticky='nsew')
		#Label(self, text = " ").grid(rowspan=1)
		
		b=Button(self, text="Dashboard").grid(row=1, column=0)
		Button(self, text="Customers").grid(row=1, column=1)
		Button(self, text="Vehicles").grid(row=1, column=2)
		Button(self, text="Workorders").grid(row=1, column=3)
		Button(self, text="Services").grid(row=1, column=4)
		Button(self, text="settings").grid(row=1, column=5)







if __name__ == '__main__':
	navBar.mainloop()

