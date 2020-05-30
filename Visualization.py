import random
import time
import pygame
import argparse
import sys
import os
import logging


parser = argparse.ArgumentParser(description="Visualize different sorting-algoritms")

parser.add_argument(
    "Algorithm", help="What algorithm you want the program to use (Bubble, Selection)"
)

parser.add_argument(
    "-amount",
    "--amount",
    dest="Amount",
    help="How many numbers you want the program to sort, default is 50",
    type=int,
    default=100,
)

parser.add_argument(
    "-novis",
    "--novis",
    dest="novis",
    nargs="?",
    help="Let you choose not to visualize the sorting",
    const=True,
    default=False,
    required=False,
)

args = parser.parse_args()

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.Algorithm:
    print("Please include what algorithm you want to visualize")
    parser.print_help()
    sys.exit(1)

if not args.novis:
    try:
        import pygame

        pygame.init()

    except ImportError:
        logging.error("Pygame Library Not Available!")


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]
    return nums


# Bubblesort algorithm
def bubblesort(nums):
    global novis

    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)

                if not novis:
                    if len(nums) < 200:

                        time.sleep(0.005)
                    animate(nums)

    return nums


# Selectionsort algorithm
def selectionsort(nums):
    global novis

    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        swap(nums, minpos, i)

        if not novis:
            if len(nums) < 200:

                time.sleep(0.005)
            animate(nums)

    return nums


def partition(nums, low, high):
    global novis
    i = low - 1  # index of smaller element
    pivot = nums[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if nums[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
            if not novis:
                animate(nums)

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    if not novis:
        animate(nums)
    return i + 1


# Function to do Quick sort
def quickSort(nums, low, high):
    global novis
    if not novis:
        animate(nums)

    if low < high:

        # pi is partitioning index, nums[p] is now
        # at right place
        pi = partition(nums, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(nums, low, pi - 1)
        quickSort(nums, pi + 1, high)


def merge(nums, l, m, r):
    global novis

    if not novis:
        animate(nums)

    n1 = m - l + 1
    n2 = r - m

    # create temp numsays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp numsays L[] and R[]
    for i in range(0, n1):
        L[i] = nums[l + i]
        if not novis:
            animate(nums)

    for j in range(0, n2):
        R[j] = nums[m + 1 + j]
        if not novis:
            animate(nums)

    # Merge the temp numsays back into nums[l..r]
    i = 0  # Initial index of first subnumsay
    j = 0  # Initial index of second subnumsay
    k = l  # Initial index of merged subnumsay

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1

        else:
            nums[k] = R[j]
            j += 1

        if not novis:
            animate(nums)
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        nums[k] = L[i]
        if not novis:
            animate(nums)
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        nums[k] = R[j]
        if not novis:
            animate(nums)
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-numsay of nums to be sorted
def mergeSort(nums, l, r):
    global novis

    if not novis:
        animate(nums)

    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(nums, l, m)
        mergeSort(nums, m + 1, r)
        merge(nums, l, m, r)


def insertionSort(nums):
    global novis

    for i in range(1, len(nums)):
        j = i - 1
        nxt_element = nums[i]
        if not novis:
            animate(nums)
        # Compare the current element with next one

        while (nums[j] > nxt_element) and (j >= 0):
            nums[j + 1] = nums[j]
            j = j - 1
            if not novis:
                animate(nums)
        nums[j + 1] = nxt_element
        if not novis:
            animate(nums)


def write_to_file(nums, sort):
    file1 = open(r"C:\Users\Herman\Development\write_file1.txt", "w")

    file1.write(sort + str(nums))

    file1.close()

    file1 = open(r"C:\Users\Herman\Development\write_file1.txt", "r")
    file = open(r"C:\Users\Herman\Development\write_file.txt", "a")

    for line in file1:
        file.write(line.replace(" ", "\n"))

    file.close()
    file1.close()
    os.remove(r"C:\Users\Herman\Development\write_file1.txt")


# Function that can be called to visualize the sorting algorithm
def animate(nums):
    # Do something here:
    global screen, postColor, postWidth, screenWidth, screenHeight, backgroundColor, postHeight_multiplier
    # debugging = open(r"C:\Users\Herman\Development\debugging.txt", "a")

    pos = 1
    for num in nums:

        # For debugging purposes only
        # debugging.write("\nITERATION: " + str(iteration) + "\n\n")
        # debugging.write("Index: " + str(nums.index(num)) + "\n")
        # debugging.write("postWidth: " + str(postWidth) + "\n")
        # debugging.write("pos: " + str(pos) + "\n")
        # debugging.write("width: " + str(postWidth) + "\n")
        # debugging.write("heigth: " + str(num * 10) + "\n")
        # debugging.write("nums: " + str(nums) + "\n\n")

        pygame.draw.rect(
            screen,
            backgroundColor,
            (
                # X
                (pos),
                # Y
                0,
                # Bredde
                postWidth,
                # Høyde
                screenHeight,
            ),
        )

        pygame.draw.rect(
            screen,
            postColor,
            (
                # X
                (pos),
                # Y
                (screenHeight - (num * postHeight_multiplier) - 1),
                # Bredde
                postWidth,
                # Høyde
                num * postHeight_multiplier,
            ),
        )
        pygame.display.update()
        pos = pos + postWidth + 1

    # debugging.close()


def main():

    global algorithm
    global nums

    # Tømmer output filen
    file = open(r"C:\Users\Herman\Development\write_file.txt", "w")
    file.write("")

    # Skriver den usorterte listen til output filen
    write_to_file(nums, "Unsorted:\n")

    if algorithm == "Bubble":
        bubblesort(nums)

    if algorithm == "Selection":
        selectionsort(nums)

    # Skriver den sorterte listen til output filen
    write_to_file(nums, "\n Sorted:\n")
    if not novis:
        running = True
        while running == True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    raise SystemExit
    pygame.quit()


amount = args.Amount
algorithm = args.Algorithm
novis = args.novis


# Genererer en liste med alle tallene fra 1 til og med amount
nums = random.sample(range(1, amount + 1), amount)

if not novis:
    screenWidth = 640
    screenHeight = 480
    postWidth = int(screenWidth / len(nums))

    postHeight_multiplier = 0
    postHeight = 0

    while postHeight < screenHeight:
        postHeight_multiplier += 0.1
        postHeight = max(nums) * postHeight_multiplier

    postHeight_multiplier = int(postHeight_multiplier)

    postColor = (13, 59, 102)
    backgroundColor = (250, 240, 202)
    screen = pygame.display.set_mode(
        ((screenWidth + (1 * len(nums)) - 37), screenHeight)
    )
    clock = pygame.time.Clock()
    pygame.display.set_caption("Visualization tool")
    screen.fill(backgroundColor)

# debugging = open(r"C:\Users\Herman\Development\debugging.txt", "w")
# debugging.write("")
# debugging.close()

if __name__ == "__main__":
    main()
