import time 
from tkinter import *

class Chronometre:

    def __init__(self):
        self.flag = 0
        self.depart = 0

    def lancer_chrono(self):
        self.flag = 1
        self.depart = time.time()
        self.chrono()

    def stopper_chrono(self):
        self.flag = 0

    def reset_chrono(self):
        self.depart = time.time()

    def chrono(self):
        y = time.time() - self.depart    
        minutes = time.localtime(y)[4]
        secondes = time.localtime(y)[5]
        if self.flag :
            self.message.configure(text = "%i ' %i '' " %(minutes,secondes))
        self.fenetre.after(1000, self.chrono)

    def start(self):
        self.fenetre = Tk()
        self.fenetre.title('Chronomètre')

        self.message = Label(self.fenetre, font=('sans', 20, 'bold'), text="Chrono prêt")
        self.message.grid(row=1)

        Button(self.fenetre, text='GO !', command=self.lancer_chrono).grid(row=2)
        Button(self.fenetre, text='STOP !', command=self.stopper_chrono).grid(row=3)
        Button(self.fenetre, text='RESET', command=self.reset_chrono).grid(row=4)

        self.fenetre.mainloop()

if __name__ == '__main__':
    Chronometre().start()
