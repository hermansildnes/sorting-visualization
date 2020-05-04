import random
import time
import pygame as p
import argparse
import sys
import logging

parser = argparse.ArgumentParser(description="Visualize different sorting-algoritms")

parser.add_argument(
    "Algorithm", help="What algorithm you want the program to use (Bubble, Selection)"
)

parser.add_argument(
    "Amount",
    help="How many numbers you want the program to sort, default is 30",
    default=30,
    type=int,
)

parser.add_argument(
    "-novis",
    dest="novis",
    help="Let you choose not to visualize the sorting",
    default=False,
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
    except ImportError:
        logging.error("Pygame Library Not Available!")


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]
    return nums


# Bubblesort algorithm
def bubblesort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
                animate(nums)
    return nums


# Selectionsort algorithm
def selectionsort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        swap(nums, minpos, i)
        animate(nums)
    return nums


# Function that can be called to visualize the sorting algorithm
def animate(nums):
    # Do something here:
    i = 0
    for num in nums:
        p.draw.rect(
            screen,
            postColor,
            (
                (int((postWidth + (screenWidth / (0.2 / len(nums)))) * i)),
                470,
                postWidth,
                nums[i],
            ),
        )  # (x, y , bredde, høyde)
        p.display.update()
        i += 1


def main():
    amount = args.amount
    algorithm = args.algorithm


# Main part/where the code actually is run

nums = random.sample(range(1, args.Amount + 1), args.Amount)

p.init()

screenWidth = 640
screenHight = 480
postWidth = int((screenWidth - (screenWidth / 0.2)) / len(nums))
screen = p.display.set_mode((screenWidth, screenHight))
postColor = (0, 0, 128)


if __name__ == "__main__":
    main()
