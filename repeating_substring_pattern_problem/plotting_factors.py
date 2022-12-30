import matplotlib.pyplot as plt
import numpy as np


def get_factors(n: int) -> int:
    """
    Given a number N, get the number of factors it has, excluding itself
    """
    factors: int = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors += 1
    return factors


if __name__ == "__main__":
    # Define the data
    # N represents the highly-composite numbers
    # obtained from http://oeis.org/A002182
    N = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160]
    k = [get_factors(n) for n in N]

    # Plot the data
    plt.plot(N, k, "bo", label="k, number of factors of highly composite numbers")
    plt.xlabel("N")
    plt.ylabel("k")
    # Plot y2 = sqrt(N)
    y2: np.ndarray = np.sqrt(N)
    plt.plot(N, np.sqrt(N), "r", label="sqrt(N)")
    # Plot y3 = Log2N
    y3: np.ndarray = np.log2(N)
    plt.plot(N, np.log2(N), "g", label="Log2N")

    min_y2 = min(y2)
    min_y3 = min(y3)
    min_k = min(k)
    min_overall = min(min_y2, min_y3, min_k)

    max_y2 = max(y2)
    max_y3 = max(y3)
    max_k = max(k)
    max_overall = max(max_y2, max_y3, max_k)

    plt.ylim(min(min_overall,  - 10, max_overall + 10))
    plt.legend()
    plt.show()
