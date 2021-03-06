from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='Hello, World!')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Execute', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)



app = Application()

app.master.title('Hello World')

app.mainloop()
