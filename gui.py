from tkinter import Button, Checkbutton, Entry, IntVar, Label, Tk
from tkinter import messagebox
from solve import Solver
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
