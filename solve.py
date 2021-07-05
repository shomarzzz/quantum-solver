
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
