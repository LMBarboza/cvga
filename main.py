from conics.factory import ConicaFactory


def main() -> None:
    conic1 = ConicaFactory.criarConica(1, 0, 1, 0, 0, -4)
    conic2 = ConicaFactory.criarConica(5, 6, 5, 0, 0, -32)
    conic3 = ConicaFactory.criarConica(3, 1.732, 2, 0, 0, -6)
    conic4 = ConicaFactory.criarConica(7, 5, -7, 0, 0, -30)

    conic1.pontosEspeciais()
    conic1.plot()

    conic2.pontosEspeciais()
    conic2.plot()

    conic3.pontosEspeciais()
    conic3.plot()

    conic4.pontosEspeciais()
    conic4.plot()


if __name__ == "__main__":
    main()
