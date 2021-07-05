from tkinter import Button, Checkbutton, Entry, IntVar, Label, Tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal
from sympy import Symbol, parse_expr

class Solver:
    def __init__(self):
        self.n = 1
        self.pot = "1"
        self.range = 1

    def _init(self, n, pot, dis):
        self.pot = pot
        self.range = dis
        x = Symbol('x')
        pot = parse_expr(self.pot)
        self.n = n
        self.dy = 1/n
        self.y = np.linspace(0, 1, n+1)
        v = []
        for i in self.y:
            v.append((self.range)**2*pot.subs(x, i))
        self.V = np.array(v, dtype=float)
        self.solve()

    def solve(self):
        d = 1/self.dy**2 + self.V[1:-1]
        e = -1/(2*self.dy**2) * np.ones(len(d)-1)
        self.energy, self.vector = eigh_tridiagonal(d, e)
    
    def plopoten(self):
        plt.plot(self.y, self.V, label="potential")
        plt.legend()
    def plot(self, wave, number):
        if not wave:
            plt.plot(self.vector.T[number]**2, label=f"energy={self.energy[number]}")
        else:
            plt.plot(self.vector.T[number], label=f"energy={self.energy[number]}")
        plt.legend()

    def plot_energy(self, numbers):
        plt.bar(np.arrange(0, numbers, 1), self.energy[:numbers])

    def show(self):
        plt.show()


q = Solver()
def show_plot():
    if accur_entry.get().isdigit():
        n = int(accur_entry.get())
    else:
        messagebox.showerror(message="put integer")
        return
    potential = pot.get()
    if wave.get().isdigit():
        number = int(wave.get())
    else:
        messagebox.showerror(message="put integer")
        return
    if spread.get().isdigit():
        s = int(spread.get())
    else:
        messagebox.showerror(message="put integer")
        return
    if n != q.n or potential != q.pot or s != q.range:
        print(accur_entry.get(), q.n)
        print(potential, q.pot)
        print(s, q.range)
        q._init(n, potential, s)
    if pp.get() == 1:
        q.plopoten()
        q.show()
    if pi.get() == 1:
        if ow.get() == 1:
            for i in range(number):
                q.plot(False, i)
        else:
            q.plot(False, number)
    else:
        if ow.get() == 1:
            for i in range(number):
                q.plot(True, i)
        else:
            q.plot(True, number)
    q.show()

window = Tk()
window.title("stationary state grapher")
ow = IntVar()
pi = IntVar()
pp = IntVar()
window.config(padx=20, pady=20)
accur = Label(text="give number of grid points")
accur_entry = Entry()
accur_entry.insert(0, "2000")
pot_lab = Label(text="give potential")
wave_lab = Label(text="wave number ")
wave = Entry()
spread_lab = Label(text="give the bounded range ")
spread = Entry()
spread.insert(0, "100")
prob = Checkbutton(text="see probability ", variable=pi, onvalue=1, offvalue=0)
only_wave = Checkbutton(text="see all the waves upto that number", variable=ow, onvalue=1, offvalue=0)
plot = Button(text="show the plot", width=32, command=show_plot)
pot = Entry()
pot.focus()
potplot = Checkbutton(text="plot potential function ", variable=pp, onvalue=1, offvalue=0)
# grid
accur.grid(row=0, column=0)
accur_entry.grid(row=0, column=1)
pot_lab.grid(row=1, column=0)
pot.grid(row=1, column=1)
wave_lab.grid(row=3, column=0)
wave.grid(row=3, column=1)
spread_lab.grid(row=2, column=0)
spread.grid(row=2, column=1)
prob.grid(row=4, column=0, columnspan=2)
only_wave.grid(row=5, column=0, columnspan=2)
potplot.grid(row=6, column=0, columnspan=2)
plot.grid(row=7, column=0, columnspan=2)
window.mainloop()