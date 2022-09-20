# just some equations from special relativity to save time

import math

def lorentz_factor(v: float) -> float:
    """
    Return the Lorentz factor
    """
    return 1 / math.sqrt(1 - v ** 2)

def time_dilation(t: float, v: float) -> float:
    """
    Return the time dilation
    """
    return t * lorentz_factor(v)

def length_contraction(l: float, v: float) -> float:
    """
    Return the length contraction
    """
    return l / lorentz_factor(v)

def get_space_based_on_c(time: float) -> float:
    """
    Return the space based on c
    """
    return time * 299792458

def get_time_based_on_c(space: float) -> float:
    """
    Return the time based on c
    """
    return space / 299792458

def main() -> int:
    """
    Main function
    """
    print(5/lorentz_factor(.943))
    return 0

if __name__ == "__main__":
    exit(main())