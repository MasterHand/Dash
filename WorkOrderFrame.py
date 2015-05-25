#!/usr/bin/python
import Tkinter
from Tkinter import StringVar, Label, RAISED, GROOVE, Toplevel, Button, Frame, Checkbutton, Entry, X, BOTH, CENTER
from tkMessageBox import showinfo

class WorkOrderFrame(Frame):

	def __init__(self, master=None, **options):

		Frame.__init__(self, master, **options)
		self.pack()

		Label(self, text="Work order frame").grid()









if __name__ == '__main__':
	WorkOrderFrame.mainloop()

