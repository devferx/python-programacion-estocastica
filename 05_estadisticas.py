import random
import statistics


def media(X):
    return sum(X) / len(X)


if __name__ == "__main__":
    X = [random.randint(1, 21) for _ in range(20)]
    mu = media(X)

    print(X)
    print(mu)
    print(statistics.mean(X))
