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
    "-Amount",
    dest="Amount",
    help="How many numbers you want the program to sort, default is 50",
    type=int,
    default=50,
)

parser.add_argument(
    "-novis",
    dest="novis",
    help="Let you choose not to visualize the sorting",
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
                    time.sleep(0.01)
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
            animate(nums)
            time.sleep(0.01)

    return nums


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
    global screen, postColor, postWidth, screenWidth, screenHeight, white
    # debugging = open(r"C:\Users\Herman\Development\debugging.txt", "a")

    pos = 2
    screen.fill(white)
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
            postColor,
            (
                # X
                (pos),
                # Y
                (screenHeight - (num * 10) - 2),
                # Bredde
                postWidth,
                # Høyde
                num * 10,
            ),
        )
        pygame.display.update()
        pos = pos + postWidth + 2

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
    postColor = (0, 0, 128)
    white = (255, 255, 255)
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Visualization tool")
    screen.fill(white)

# debugging = open(r"C:\Users\Herman\Development\debugging.txt", "w")
# debugging.write("")
# debugging.close()

if __name__ == "__main__":
    main()
