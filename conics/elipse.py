from .conica import Conica
import numpy as np
from typing import Optional, Tuple, List

class Elipse(Conica):
    def pontosEspeciais(self) -> None:
        x0: float = (2 * self.C * self.D - self.B * self.E) / (self.B**2 - 4 * self.A * self.C)
        y0: float = (2 * self.A * self.E - self.B * self.D) / (self.B**2 - 4 * self.A * self.C)
        self.centro = (x0, y0)

        num: float = 2 * (self.A * self.E**2 + self.C * self.D**2 + \
                          self.F * self.B**2 - 2 * self.B * self.D * self.E - self.A * self.C * self.F)

        denom1: float = (self.B**2 - 4 * self.A * self.C) * \
        ((self.C - self.A) * np.sqrt(1 + 4 * self.B**2 / ((self.A - self.C)**2)) - (self.C + self.A))

        denom2: float = (self.B**2 - 4 * self.A * self.C) * \
        ((self.A - self.C) * np.sqrt(1 + 4 * self.B**2 / ((self.A - self.C)**2)) - (self.C + self.A))
        a: float = np.sqrt(num / denom1)
        b: float = np.sqrt(num / denom2)

        self.vertices = [(x0 - a, y0), (x0 + a, y0), (x0, y0 - b), (x0, y0 + b)]

        c: float = np.sqrt(a**2 - b**2)
        self.foco = [(x0 - c, y0), (x0 + c, y0)]
