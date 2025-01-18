import math

def calculate_pi(n):
    pi = 0
    for k in range(n):
        pi += (1 / (16 ** k)) * (
            (4 / (8 * k + 1)) -
            (2 / (8 * k + 4)) -
            (1 / (8 * k + 5)) -
            (1 / (8 * k + 6))
        )
    return pi
    