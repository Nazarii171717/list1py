from typing import List, Tuple
import matplotlib.pyplot as plt
import random


def weekday(d, m, y):
    """Figures out the day of the week with provided data.

    Args:
    d (int): day of the month (1-31)
    m (int): month of the year (1-12)
    y (int): year of the date (>=0)

    Returns:
    The day of the week as a string.

    Raises:
    ValueError: if the input data is not valid.
    """
    # Validation of the data
    if d > 31 or d <= 0 or m > 12 or m <= 0 or y < 0:
        raise ValueError("The input data is incorrect")
    if d >= 29 and m == 2 and y % 4 != 0:
        raise ValueError("The input data is incorrect")
    # Days of the week mapping
    days_of_week = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }

    # Calculation based on provided data and Georgian calendar formula
    y0 = y - ((14 - m) // 12)
    x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
    m0 = m + (12 * ((14 - m) // 12)) - 2
    d0 = (d + x + (31 * m0 // 12)) % 7




    # Return the day of the week
    return days_of_week.get(d0)


def segment_length(Ap, Ak, Bp, Bk):
    """Calculates the intersection of two line segments

    Args:
    Ap (int): left border of the first line segment
    Ak (int): right border of the first line segment
    Bp (int): left border of the second line segment
    Bk (int): right border of the second line segment

    Returns:
    The intersection of two line segments as a string.
    """
    if (Ap > Ak or Bp > Bk):
        raise ValueError("The input data is incorrect")

    # Determination of the left border
    if (Bp >= Ap):
        leftBorder = Bp
    else:
        leftBorder = Ap

    # Determination of the right border
    if (Bk >= Ak):
        rightBorder = Ak
    else:
        rightBorder = Bk

    # Return None if two line segments don't intersect
    if (rightBorder < leftBorder):
        return None

    # Return the intersection of two line segments as a string
    else:
        return "(" + leftBorder.__str__() + ", " + rightBorder.__str__() + ")"


def random_walk(n) -> List[Tuple[int, int]]:
    """Simulates a random walk on a 2D grid starting at the origin (0, 0)
    until any coordinate (x or y) reaches the boundary value 'n'.

    Parameters:
    n (int): The boundary value at which the random walk should stop.

    Returns:
    List[Tuple[int, int]]: A list of tuples representing the coordinates visited during the random walk.
    """
    coordinates: List[Tuple[int, int]] = []

    # Starts at the origin
    walkers_coor_x = 0
    walkers_coor_y = 0
    coordinates.append((walkers_coor_x, walkers_coor_y))

    is_not_reach = True

    while is_not_reach:
        x = 0
        y = 0

        # Generates random number from 1 to 4
        # 1 is left, 2 is right, 3 is up, 4 is down
        decision = random.randint(1, 4)

        if decision == 1:
            x = walkers_coor_x
            y = walkers_coor_y - 1
        elif decision == 2:
            x = walkers_coor_x
            y = walkers_coor_y + 1
        elif decision == 3:
            x = walkers_coor_x + 1
            y = walkers_coor_y
        elif decision == 4:
            x = walkers_coor_x - 1
            y = walkers_coor_y

        # Updates walker's coordinates
        walkers_coor_x = x
        walkers_coor_y = y
        coordinates.append((walkers_coor_x, walkers_coor_y))

        # Once x or y equals n, the walk ends
        if x == n or y == n:
            is_not_reach = False

    return coordinates


def dec2bin(x):
    """Converts an integer to its binary representation.

    Args:
    x: An integer that needs to be converted to binary.

    Returns:
    A string representing the binary equivalent of the integer.
    """
    binary = ""

    # While the number is not 0, continue dividing it by 2
    while x // 2 != 0:
        binary += str(x % 2)
        x = x // 2

    # Adds the remainder of the last division
    if x // 2 == 0:
        binary += str(x % 2)

    # In case the input number is 0
    if x == 0:
        binary = "0"

    # Returns the reverse string that corresponds to the binary representation
    return binary[::-1]


def dna_complement(orig_strand):
    """Returns the complementary strand of a DNA sequence.

    Args:
    orig_strand: A DNA strand string containing only 'A', 'T', 'C', and 'G'.

    Returns:
    The complementary DNA strand.

    Raises:
    ValueError: If the input contains any character other than 'A', 'T', 'C', or 'G'.
    """
    compl_strand = ""

    for i in range(len(orig_strand)):
        if orig_strand[i] == 'A':
            compl_strand += 'T'
        elif orig_strand[i] == 'T':
            compl_strand += 'A'
        elif orig_strand[i] == 'C':
            compl_strand += 'G'
        elif orig_strand[i] == 'G':
            compl_strand += 'C'
        else:
            raise ValueError("Illegal argument: character not recognized in DNA strand")

    return compl_strand



if __name__ == '__main__':
    print(dec2bin(0))
    print(weekday(29, 2, 2025))