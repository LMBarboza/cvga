import math
import pandas as pd


def sin_metade(a: float, cosenos: dict) -> float:
    return math.sqrt((1 - cosenos[2 * a]) / 2)


def cos_metade(a: float, cosenos: dict) -> float:
    return math.sqrt((1 + cosenos[2 * a]) / 2)


def sin(a: int, b: int, senos: dict, cosenos: dict) -> float:
    return senos[a] * cosenos[b] + cosenos[a] * senos[b]


def cos(a: int, b: int, senos: dict, cosenos: dict) -> float:
    return cosenos[a] * cosenos[b] - senos[a] * senos[b]


def main(Q: int = 1) -> None:
    senos_py = {i: math.sin(math.radians(i)) for i in range(1, 91)}
    cosenos_py = {i: math.cos(math.radians(i)) for i in range(1, 91)}

    if Q == 1:
        sin_1 = math.sin(math.radians(1))
        cos_1 = math.cos(math.radians(1))

    else:
        senos_t = {90 * 2 / 2: 1}
        cosenos_t = {90 * 2 / 2: 0}
        sin_1 = 0
        cos_1 = 0
        for i in range(1, 9):
            a = 90 / (2**i)
            senos_t[a] = sin_metade(a, cosenos_t)
            cosenos_t[a] = cos_metade(a, cosenos_t)
            if i == 8:
                sin_1 = sin(a, a * 2, senos_t, cosenos_t)
                cos_1 = cos(a, a * 2, senos_t, cosenos_t)

    senos = {1: sin_1}
    cosenos = {1: cos_1}

    for i in range(1, 90):
        senos[i + 1] = sin(i, 1, senos, cosenos)
        cosenos[i + 1] = cos(i, 1, senos, cosenos)

    df = pd.DataFrame(
        {
            "Seno": senos,
            "Seno_Python": senos_py,
            "Coseno": cosenos,
            "Coseno_Python": cosenos_py,
        }
    )
    df["Erro_seno"] = (df["Seno"] - df["Seno_Python"]).abs()
    df["Erro_coseno"] = (df["Coseno"] - df["Coseno_Python"]).abs()

    print(df)


if __name__ == "__main__":
    main(1)
    main(2)
