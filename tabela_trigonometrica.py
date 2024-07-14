import math
import pandas as pd


def sin(a: int, b: int, senos: dict, cosenos: dict) -> float:
    return senos[a] * cosenos[b] + cosenos[a] * senos[b]


def cos(a: int, b: int, senos: dict, cosenos: dict) -> float:
    return cosenos[a] * cosenos[b] - senos[a] * senos[b]


def main() -> None:
    senos_py = {i: math.sin(math.radians(i)) for i in range(1, 91)}
    cosenos_py = {i: math.cos(math.radians(i)) for i in range(1, 91)}

    sin_1 = math.sin(math.radians(1))
    cos_1 = math.cos(math.radians(1))

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
    main()
