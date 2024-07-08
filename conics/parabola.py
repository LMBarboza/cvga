from .conica import Conica

class Parabola(Conica):
    def pontosEspeciais(self) -> None:
        self.centro = None
        self.vertices = None
        self.foco = None
