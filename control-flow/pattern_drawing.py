#!/usr/bin/env python3
# pattern_drawing.py
# Draws a square pattern of asterisks using nested loops

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return

        row = 0
        while row < size:
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
