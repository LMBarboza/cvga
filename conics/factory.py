from .elipse import Elipse
from .hiperbole import Hiperbole
from .circulo import Circulo
from .parabola import Parabola
from typing import Union


class ConicaFactory:
    @staticmethod
    def criarConica(
        A: float, B: float, C: float, D: float, E: float, F: float
    ) -> Union[Elipse, Hiperbole, Circulo, Parabola]:
        delta = B**2 - 4 * A * C
        if delta < 0:
            if A == C and B == 0:
                return Circulo(A, B, C, D, E, F)
            return Elipse(A, B, C, D, E, F)
        elif delta == 0:
            return Parabola(A, B, C, D, E, F)
        else:
            return Hiperbole(A, B, C, D, E, F)
