import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from typing import Optional, Tuple, List

class Conica(ABC):
    def __init__(self, A: float, B: float, C: float, D: float, E: float, F: float):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.centro: Optional[Tuple[float, float]] = None
        self.vertices: Optional[List[Tuple[float, float]]] = None
        self.foco: Optional[List[Tuple[float, float]]] = None

    @abstractmethod
    def pontosEspeciais(self) -> None:
        pass

    def plot(self) -> None:
        x = np.linspace(-10, 10, 400)
        y = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x, y)
        Z = self.A*X**2 + self.B*X*Y + self.C*Y**2 + self.D*X + self.E*Y + self.F
        
        plt.contour(X, Y, Z, levels=[0], colors="b")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Cônica: {self.__class__.__name__}")
        plt.grid(True)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.gca().set_aspect("equal", adjustable="box")

        if self.center:
            plt.plot(*self.center, "ro", label="Centro")
        if self.vertices:
            for v in self.vertices:
                plt.plot(*v, "go", label="Vertice")
        if self.foci:
            for f in self.foci:
                plt.plot(*f, "mo", label="Foco")
        
        plt.legend()
        plt.show()
