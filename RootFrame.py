from Tkinter import Frame, RAISED
from myapp import myapp

class RootFrame(Frame):
	def __init__(self, master=None, **options):

		Frame.__init__(self, master, **options)
		self.pack()

		#self.master.minsize(800, 600)

		myapp(self, borderwidth=2, relief=RAISED).pack()

		#myapp(self).pack()


if __name__ == "__main__":
	RootFrame().mainloop()
