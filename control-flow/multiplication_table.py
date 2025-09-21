#!/usr/bin/env python3
# multiplication_table.py
# Generates a multiplication table for a given number

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
