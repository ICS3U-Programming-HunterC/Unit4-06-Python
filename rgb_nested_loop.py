#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 28, 2022
# This program uses nested loops to print out all the valid RGB colours from 200 - 255


def main():
    for counter1 in range(200, 256):
        for counter2 in range(200, 256):
            for counter3 in range(200, 256):
                print("RGB({0}, {1}, {2})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
