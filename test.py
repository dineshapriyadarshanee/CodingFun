import tkinter
class ProgramGUI: # define a ProgramGUI class
     def __init__(self):
         self.main = tkinter.Tk()
         self.main.geometry('100x100')
         self.f1 = tkinter.Frame(self.main)
         self.f2 = tkinter.Frame(self.main)

         self.l1 = tkinter.Label(self.f1, text='NW', width=2, bg='pink')
         self.l2 = tkinter.Label(self.f1, text='NE', width=2, bg='pink')
         self.l1.pack(side='left')
         self.l2.pack(side='right')
         self.l3 = tkinter.Label(self.f2, text='SW', width=2, bg='pink')
         self.l4 = tkinter.Label(self.f2, text='SE', width=2, bg='pink')
         self.l3.pack(side='left')
         self.l4.pack(side='right')
         self.f1.pack(side='top')
         self.f2.pack(side='bottom')

         tkinter.mainloop()
         
gui = ProgramGUI() 
