import conics.ConicaFactory


def main() -> None:
    conic = ConicaFactory.criarConica(1, 0, 1, 0, 0, -4)  # Parameters for a circle x^2 + y^2 - 4 = 0
    conic.pontosEspeciais()
    conic.plot()

if __name__ == "__main__":
    main()
