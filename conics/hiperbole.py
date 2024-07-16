from .conica import Conica
import numpy as np
import math
from typing import Optional, Tuple, List


class Hiperbole(Conica):
    def pontosEspeciais(self) -> None:
        x0: float = (2 * self.C * self.D - self.B * self.E) / (
            self.B**2 - 4 * self.A * self.C
        )
        y0: float = (2 * self.A * self.E - self.B * self.D) / (
            self.B**2 - 4 * self.A * self.C
        )
        self.centro = (x0, y0)

        theta = -0.5 * math.atan2(-self.B, self.C - self.A)
        num = 2 * (self.A * x0**2 + self.B * x0 * y0 + self.C * y0**2 - self.F)
        denom1 = self.A + self.C - math.sqrt((self.A - self.C) ** 2 + self.B**2)
        denom2 = -(self.A + self.C) - math.sqrt((self.A - self.C) ** 2 + self.B**2)

        a = math.sqrt(num / abs(denom1))
        b = math.sqrt(num / abs(denom2))

        if a > b:
            v1x = (a - x0) * np.cos(theta) - (y0 * np.sin(theta))
            v1y = -(a - x0) * np.sin(theta) - (y0 * np.cos(theta))

            v2x = (-a - x0) * np.cos(theta) - (y0 * np.sin(theta))
            v2y = -(-a - x0) * np.sin(theta) - (y0 * np.cos(theta))

            self.vertices = [(v1x, v1y), (v2x, v2y)]

            c = np.sqrt(a**2 + b**2)

            f1x = (c - x0) * np.cos(theta) - (y0 * np.sin(theta))
            f1y = -(c - x0) * np.sin(theta) - (y0 * np.cos(theta))

            f2x = (-c - x0) * np.cos(theta) - (y0 * np.sin(theta))
            f2y = -(-c - x0) * np.sin(theta) - (y0 * np.cos(theta))

            self.foco = [(f1x, f1y), (f2x, f2y)]

        else:
            v1x = -x0 * np.cos(theta) + ((b - y0) * np.sin(theta))
            v1y = x0 * np.sin(theta) + ((b - y0) * np.cos(theta))

            v2x = -x0 * np.cos(theta) + ((-b - y0) * np.sin(theta))
            v2y = x0 * np.sin(theta) + ((-b - y0) * np.cos(theta))

            self.vertices = [(v1x, v1y), (v2x, v2y)]

            c = np.sqrt(b**2 + a**2)

            f1x = -x0 * np.cos(theta) + ((c - y0) * np.sin(theta))
            f1y = x0 * np.sin(theta) + ((c - y0) * np.cos(theta))

            f2x = -x0 * np.cos(theta) + ((-c - y0) * np.sin(theta))
            f2y = x0 * np.sin(theta) + ((-c - y0) * np.cos(theta))

            self.foco = [(f1x, f1y), (f2x, f2y)]
