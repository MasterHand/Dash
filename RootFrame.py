from Tkinter import Frame, RAISED, RIDGE, Button, Label
from CustomerFrame import CustomerFrame
from navBar import navBar
from WorkOrderFrame import WorkOrderFrame

class RootFrame(Frame):
	def __init__(self, master=None, **options):

		Frame.__init__(self, master, **options)
		self.pack()

		#self.master.minsize(800, 600)
		
		navBar(self, borderwidth=5, relief=RIDGE).pack()


		CustomerFrame(self, borderwidth=2, relief=RAISED).pack()
		WorkOrderFrame(self, borderwidth=2, relief=RAISED).pack()



	def hide(event):
		event.widget.pack_forget()

	def show(event):
		event.widget.pack()

if __name__ == "__main__":
	RootFrame().mainloop()
